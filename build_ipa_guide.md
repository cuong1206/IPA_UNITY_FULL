# Hướng dẫn Build IPA từ Unity Xcode Project

## Tổng quan

Hướng dẫn này giúp bạn tạo file IPA từ Unity Xcode project mà **không cần**:
- Tài khoản Apple Developer trả phí
- Máy Mac
- Chứng chỉ iOS (bạn sẽ ký lại sau bằng cách của riêng bạn)

## Giải pháp: GitHub Actions

### Cách hoạt động

1. Upload Xcode project lên GitHub (private hoặc public repo)
2. GitHub Actions tự động build IPA trên macOS runner (miễn phí)
3. Download file IPA từ GitHub Actions artifacts
4. Ký lại IPA bằng công cụ của bạn (nếu cần)

### Yêu cầu

- Tài khoản GitHub (miễn phí)
- Xcode project từ Unity (đã có trong thư mục `XCODE`)

## Hướng dẫn từng bước

### Bước 1: Tạo GitHub Repository

1. Đăng nhập GitHub và tạo repository mới
2. Chọn **Private** (khuyến nghị) hoặc Public
3. Copy repository URL

### Bước 2: Upload code lên GitHub

```bash
# Khởi tạo git repository (nếu chưa có)
cd E:\IOSBUILD
git init

# Thêm remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Commit và push
git add .
git commit -m "Initial commit: Unity iOS project"
git branch -M main
git push -u origin main
```

**Lưu ý**: File `.github/workflows/build-ipa.yml` đã được tạo sẵn, commit nó cùng với code.

### Bước 3: Kích hoạt GitHub Actions

1. Vào repository trên GitHub
2. Tab **Actions**
3. Chấp nhận điều khoản GitHub Actions (nếu lần đầu)
4. Workflow sẽ tự động chạy khi push code

### Bước 4: Chạy Workflow thủ công (Optional)

1. Vào tab **Actions**
2. Chọn workflow **Build iOS IPA**
3. Click **Run workflow**
4. Chọn build configuration (Release hoặc Debug)
5. Click **Run workflow**

### Bước 5: Download IPA

1. Vào tab **Actions**
2. Click vào run vừa hoàn thành
3. Cuộn xuống phần **Artifacts**
4. Click **ios-ipa** để download
5. Giải nén file ZIP
6. File IPA nằm trong thư mục `XCODE/build/export/`

## Cấu trúc Project

```
E:\IOSBUILD\
├── .github\
│   └── workflows\
│       └── build-ipa.yml    # GitHub Actions workflow
├── XCODE\                    # Unity Xcode project
│   ├── Unity-iPhone.xcodeproj
│   ├── Classes\
│   ├── Data\
│   └── ...
├── build_ipa_guide.md         # File này
└── README.md                  # Tóm tắt dự án
```

## Cấu hình dự án

Dự án Unity của bạn có cấu hình:
- **Scheme**: `Unity-iPhone`
- **Bundle ID**: `com.NROFLY.NRO-FLY`
- **Product Name**: `NROFLY`
- **Xcode Project**: `Unity-iPhone.xcodeproj`

Các giá trị này đã được cấu hình sẵn trong workflow. Nếu bạn thay đổi Unity project, có thể cần cập nhật workflow.

## Troubleshooting

### Lỗi: "No such module"

- Kiểm tra xem có thiếu dependencies không
- Đảm bảo tất cả frameworks đã được link đúng trong Xcode project

### Lỗi: "Code signing required"

Workflow đã được cấu hình để build không cần code signing. Nếu vẫn gặp lỗi:
- IPA sẽ được tạo thủ công từ .app bundle
- File IPA có thể cần ký lại bằng công cụ của bạn

### Lỗi: "Archive failed"

- Kiểm tra logs trong GitHub Actions
- Đảm bảo Xcode project hợp lệ
- Thử build với configuration Debug trước

### IPA không xuất hiện trong artifacts

- Workflow sẽ tạo IPA từ .app bundle thủ công nếu exportArchive fail
- Kiểm tra logs để xem bước nào bị lỗi
- IPA sẽ được tạo với tên `NROFLY.ipa` trong `build/export/`

## Tùy chỉnh Workflow

Nếu cần thay đổi cấu hình:

1. Mở file `.github/workflows/build-ipa.yml`
2. Tìm các biến:
   - `SCHEME`: Tên scheme trong Xcode
   - `BUILD_CONFIG`: Release hoặc Debug
3. Chỉnh sửa và commit lại

## Code Signing

File IPA được tạo **không có code signing** (unsigned). Bạn cần:

1. Download IPA từ GitHub Actions
2. Sử dụng công cụ của bạn để ký lại IPA
3. Cài đặt lên thiết bị

**Lưu ý**: Một số công cụ sideload (như AltStore, Sideloadly) có thể tự động ký IPA khi cài đặt.

## Giới hạn GitHub Actions

- **macOS runners miễn phí**: 2000 phút/tháng cho private repos
- **Public repos**: Không giới hạn
- Mỗi build thường mất 10-20 phút

## Tài liệu tham khảo

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Xcode Build Documentation](https://developer.apple.com/documentation/xcode)
- [Unity iOS Build Documentation](https://docs.unity3d.com/Manual/iphone-player.html)

