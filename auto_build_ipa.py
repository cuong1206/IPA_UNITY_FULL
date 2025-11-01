#!/usr/bin/env python3
"""
Auto Build IPA Tool
Tự động: Push code → Trigger workflow → Đợi build xong → Download IPA về máy
"""

import os
import sys
import time
import json
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("❌ Cần cài đặt thư viện requests:")
    print("   pip install requests")
    sys.exit(1)

# ============== CẤU HÌNH ==============
REPO_OWNER = "cuong1206"
REPO_NAME = "IPA_UNITY_FULL"
WORKFLOW_FILE = "build-ipa.yml"
OUTPUT_DIR = "output"
BRANCH = "main"

# GitHub API endpoints
API_BASE = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

class Colors:
    """ANSI color codes"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(step_num, message):
    """In ra bước thực hiện"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}[Bước {step_num}]{Colors.ENDC} {message}")

def print_success(message):
    """In thông báo thành công"""
    print(f"{Colors.GREEN}✅ {message}{Colors.ENDC}")

def print_error(message):
    """In thông báo lỗi"""
    print(f"{Colors.RED}❌ {message}{Colors.ENDC}")

def print_info(message):
    """In thông tin"""
    print(f"{Colors.CYAN}ℹ️  {message}{Colors.ENDC}")

def print_warning(message):
    """In cảnh báo"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.ENDC}")

def get_github_token():
    """Lấy GitHub token từ environment hoặc user input"""
    token = os.environ.get('GITHUB_TOKEN')
    
    if not token:
        print_warning("Chưa có GitHub Personal Access Token!")
        print_info("Tạo token tại: https://github.com/settings/tokens")
        print_info("Quyền cần thiết: repo, workflow, actions:read")
        token = input(f"{Colors.CYAN}Nhập GitHub Token: {Colors.ENDC}").strip()
    
    if not token:
        print_error("Không có token, không thể tiếp tục!")
        sys.exit(1)
    
    return token

def run_command(cmd, check=True, capture_output=False):
    """Chạy command và trả về kết quả"""
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, check=check, 
                                  capture_output=True, text=True, encoding='utf-8')
            return result.stdout.strip()
        else:
            subprocess.run(cmd, shell=True, check=check)
            return None
    except subprocess.CalledProcessError as e:
        if check:
            print_error(f"Lỗi khi chạy command: {cmd}")
            print_error(f"Error: {e}")
            sys.exit(1)
        return None

def git_push(branch=BRANCH, force=False):
    """Push code lên GitHub"""
    print_step(1, "Đẩy code lên GitHub...")
    
    # Kiểm tra có thay đổi không
    status = run_command("git status --porcelain", capture_output=True)
    
    if not status:
        print_info("Không có thay đổi để commit")
    else:
        # Add và commit
        print_info("Đang commit thay đổi...")
        run_command("git add -A")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"Auto build IPA - {timestamp}"
        run_command(f'git commit -m "{commit_msg}"', check=False)
    
    # Push
    print_info(f"Đang push lên branch {branch}...")
    push_cmd = f"git push origin {branch}"
    if force:
        push_cmd += " --force"
    
    run_command(push_cmd)
    print_success(f"Đã push code lên {branch}!")

def trigger_workflow(token, build_config="Release"):
    """Trigger GitHub Actions workflow"""
    print_step(2, f"Kích hoạt workflow build IPA (config: {build_config})...")
    
    url = f"{API_BASE}/actions/workflows/{WORKFLOW_FILE}/dispatches"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "ref": BRANCH,
        "inputs": {
            "build_configuration": build_config
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 204:
        print_success("Đã kích hoạt workflow!")
        # Đợi 3 giây để workflow được tạo
        time.sleep(3)
        return True
    else:
        print_error(f"Lỗi khi trigger workflow: {response.status_code}")
        print_error(response.text)
        return False

def get_latest_workflow_run(token):
    """Lấy workflow run mới nhất"""
    url = f"{API_BASE}/actions/workflows/{WORKFLOW_FILE}/runs"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "branch": BRANCH,
        "per_page": 1
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['workflow_runs']:
            return data['workflow_runs'][0]
    
    return None

def wait_for_workflow_completion(token, run_id, timeout=3600):
    """Đợi workflow hoàn thành"""
    print_step(3, "Đang đợi workflow build xong...")
    
    url = f"{API_BASE}/actions/runs/{run_id}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    start_time = time.time()
    last_status = None
    
    while True:
        if time.time() - start_time > timeout:
            print_error(f"Timeout sau {timeout}s!")
            return False
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print_error(f"Lỗi khi check status: {response.status_code}")
            return False
        
        run_data = response.json()
        status = run_data['status']
        conclusion = run_data.get('conclusion')
        
        # In progress nếu status thay đổi
        if status != last_status:
            elapsed = int(time.time() - start_time)
            print_info(f"Status: {status} | Đã chạy: {elapsed}s | URL: {run_data['html_url']}")
            last_status = status
        
        if status == 'completed':
            if conclusion == 'success':
                print_success(f"Build thành công! (Thời gian: {int(time.time() - start_time)}s)")
                return True
            else:
                print_error(f"Build thất bại! Conclusion: {conclusion}")
                print_error(f"Chi tiết: {run_data['html_url']}")
                return False
        
        # Đợi 10s trước khi check lại
        time.sleep(10)

def list_artifacts(token, run_id):
    """Liệt kê artifacts của workflow run"""
    url = f"{API_BASE}/actions/runs/{run_id}/artifacts"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()['artifacts']
    
    return []

def download_artifact(token, artifact_id, artifact_name, output_dir):
    """Download artifact từ GitHub"""
    print_step(4, f"Đang tải file {artifact_name}...")
    
    # Tạo thư mục output
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Download artifact (ZIP format)
    url = f"{API_BASE}/actions/artifacts/{artifact_id}/zip"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
    
    if response.status_code == 200:
        # Lưu file
        zip_file = output_path / f"{artifact_name}.zip"
        
        with open(zip_file, 'wb') as f:
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r   Đang tải: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='')
        
        print()  # New line
        print_success(f"Đã tải về: {zip_file}")
        
        # Giải nén nếu cần
        if artifact_name.endswith('.ipa'):
            # Artifact là .ipa nhưng GitHub wrap trong ZIP
            # Giải nén để lấy file IPA
            import zipfile
            try:
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    # Lấy tên file đầu tiên trong zip
                    file_list = zip_ref.namelist()
                    if file_list:
                        ipa_file = file_list[0]
                        zip_ref.extract(ipa_file, output_path)
                        
                        # Đổi tên nếu cần
                        extracted_path = output_path / ipa_file
                        final_ipa = output_path / artifact_name
                        
                        if extracted_path != final_ipa:
                            extracted_path.rename(final_ipa)
                        
                        print_success(f"File IPA: {final_ipa}")
                        
                        # Xóa file ZIP
                        zip_file.unlink()
                        
                        return str(final_ipa)
            except Exception as e:
                print_warning(f"Không thể giải nén: {e}")
                print_info(f"File ZIP vẫn có tại: {zip_file}")
        
        return str(zip_file)
    else:
        print_error(f"Lỗi khi tải artifact: {response.status_code}")
        return None

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Auto Build IPA Tool - Tự động build và download IPA từ GitHub Actions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python auto_build_ipa.py                    # Build Release (mặc định)
  python auto_build_ipa.py --config Debug     # Build Debug
  python auto_build_ipa.py --no-push          # Chỉ trigger workflow, không push code
  python auto_build_ipa.py --output myipa     # Lưu IPA vào thư mục myipa/
  
Biến môi trường:
  GITHUB_TOKEN    GitHub Personal Access Token
        """
    )
    
    parser.add_argument('--config', '-c', 
                       choices=['Release', 'Debug'],
                       default='Release',
                       help='Build configuration (mặc định: Release)')
    
    parser.add_argument('--no-push', 
                       action='store_true',
                       help='Không push code, chỉ trigger workflow')
    
    parser.add_argument('--output', '-o',
                       default=OUTPUT_DIR,
                       help=f'Thư mục lưu IPA (mặc định: {OUTPUT_DIR})')
    
    parser.add_argument('--force-push', '-f',
                       action='store_true',
                       help='Force push code (cẩn thận!)')
    
    parser.add_argument('--no-wait',
                       action='store_true',
                       help='Không đợi build xong, chỉ trigger và thoát')
    
    args = parser.parse_args()
    
    # Banner
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}🚀 AUTO BUILD IPA TOOL 🚀{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n")
    
    print_info(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print_info(f"Branch: {BRANCH}")
    print_info(f"Build Config: {args.config}")
    print_info(f"Output: {args.output}/")
    
    # Lấy GitHub token
    token = get_github_token()
    
    # Bước 1: Push code (nếu cần)
    if not args.no_push:
        git_push(branch=BRANCH, force=args.force_push)
    else:
        print_info("Bỏ qua push code (--no-push)")
    
    # Bước 2: Trigger workflow
    if not trigger_workflow(token, args.config):
        sys.exit(1)
    
    # Lấy workflow run mới nhất
    print_info("Đang tìm workflow run...")
    run = get_latest_workflow_run(token)
    
    if not run:
        print_error("Không tìm thấy workflow run!")
        sys.exit(1)
    
    run_id = run['id']
    print_success(f"Workflow Run ID: {run_id}")
    print_info(f"URL: {run['html_url']}")
    
    # Bước 3: Đợi workflow hoàn thành
    if args.no_wait:
        print_info("Không đợi build xong (--no-wait)")
        print_info(f"Theo dõi tại: {run['html_url']}")
        sys.exit(0)
    
    if not wait_for_workflow_completion(token, run_id, timeout=3600):
        sys.exit(1)
    
    # Bước 4: Download artifacts
    print_info("Đang tìm artifacts...")
    artifacts = list_artifacts(token, run_id)
    
    if not artifacts:
        print_warning("Không tìm thấy artifacts!")
        sys.exit(1)
    
    print_success(f"Tìm thấy {len(artifacts)} artifact(s)")
    
    downloaded_files = []
    for artifact in artifacts:
        artifact_name = artifact['name']
        artifact_id = artifact['id']
        
        # Chỉ download IPA artifacts
        if 'ipa' in artifact_name.lower():
            file_path = download_artifact(token, artifact_id, artifact_name, args.output)
            if file_path:
                downloaded_files.append(file_path)
    
    # Kết quả
    print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.GREEN}🎉 HOÀN TẤT! 🎉{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.ENDC}\n")
    
    if downloaded_files:
        print_success(f"Đã tải về {len(downloaded_files)} file:")
        for file_path in downloaded_files:
            print(f"   📦 {file_path}")
            print_info(f"      Kích thước: {os.path.getsize(file_path) / (1024*1024):.2f} MB")
    else:
        print_warning("Không có file nào được tải về!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⚠️  Bị hủy bởi người dùng{Colors.ENDC}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Lỗi không mong đợi: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

