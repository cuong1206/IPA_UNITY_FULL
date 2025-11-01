# Cách chạy GitHub Actions Workflow

## Vấn đề: Không thấy nút "Run workflow"

Nút **"Run workflow"** không xuất hiện trên trang **"All workflows"**. Bạn cần vào trang chi tiết của từng workflow.

## Cách tìm và chạy workflow

### Bước 1: Vào trang chi tiết của workflow

**Cách 1: Click vào tên workflow trong sidebar (Dễ nhất)**

1. Ở tab **Actions**, nhìn vào **sidebar bên trái**
2. Bạn sẽ thấy: `.github/workflows/build-ipa.yml`
3. **Click vào đó** (click vào text `.github/workflows/build-ipa.yml`)
4. Trang sẽ chuyển sang trang chi tiết của workflow này

**Cách 2: Click vào workflow run đã có**

1. Ở trang "All workflows", bạn thấy workflow run "Initial commit"
2. **Click vào tên run đó** (dòng "Initial commit" với icon X đỏ)
3. Sau đó click vào tab **workflow name** ở trên cùng (hoặc quay lại sidebar)

### Bước 2: Tìm nút "Run workflow"

Sau khi vào trang chi tiết của workflow:

1. **Nhìn góc phải trên cùng** của trang
2. Bạn sẽ thấy nút **"Run workflow"** màu xanh lá hoặc xanh dương
3. Click vào đó

### Bước 3: Chọn options và chạy

Sau khi click "Run workflow", bạn sẽ thấy popup:

1. **Branch**: Chọn `main` (hoặc branch bạn muốn)
2. **Build configuration**: 
   - Chọn `Release` (khuyến nghị)
   - Hoặc `Debug` (nếu muốn build debug)
3. Click nút **"Run workflow"** màu xanh ở dưới popup

## Hình minh họa đường đi

```
Tab Actions
  ↓
Sidebar: Click ".github/workflows/build-ipa.yml"
  ↓
Trang chi tiết workflow (tên "Build iOS IPA")
  ↓
Góc phải trên: Nút "Run workflow" 
  ↓
Popup: Chọn branch + config → "Run workflow"
```

## Kiểm tra workflow đã được cấu hình đúng chưa

Workflow của bạn đã có `workflow_dispatch` nên nút "Run workflow" sẽ xuất hiện khi vào trang chi tiết.

**Nếu vẫn không thấy nút "Run workflow":**

1. **Kiểm tra file workflow**:
   - Vào tab **Code**
   - Đường dẫn: `.github/workflows/build-ipa.yml`
   - Đảm bảo có phần:
     ```yaml
     on:
       workflow_dispatch:
     ```

2. **Refresh trang**: Nhấn `Ctrl+F5` hoặc `Cmd+Shift+R` để hard refresh

3. **Kiểm tra quyền**: Đảm bảo bạn là owner/collaborator của repo

## Cách chạy tự động khi push code

Workflow cũng được cấu hình để **tự động chạy** khi:
- Push code lên branch `main` hoặc `master`
- Thay đổi files trong thư mục `XCODE/**`

Vậy nên nếu bạn push code mới, workflow sẽ tự động chạy mà không cần click "Run workflow".

## Troubleshooting

### Không thấy workflow trong sidebar?

1. Kiểm tra file có tồn tại không:
   - Tab Code → `.github/workflows/build-ipa.yml`
2. Đảm bảo file có syntax đúng YAML
3. Refresh trang Actions

### Nút "Run workflow" không hiện?

1. Vào trang chi tiết workflow (click vào tên trong sidebar)
2. Đảm bảo bạn có quyền edit repo
3. Kiểm tra workflow có `workflow_dispatch` trong phần `on:`

### Workflow chạy nhưng fail?

Xem logs để biết lỗi:
1. Click vào workflow run đã fail
2. Click vào job `build-ipa`
3. Xem logs từng step để tìm lỗi

## Tóm tắt nhanh

1. Tab **Actions**
2. Sidebar bên trái → Click **`.github/workflows/build-ipa.yml`**
3. Góc phải trên → Click **"Run workflow"**
4. Chọn branch `main` + config `Release`
5. Click **"Run workflow"** màu xanh

