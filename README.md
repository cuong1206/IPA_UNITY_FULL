# Build iOS IPA từ Unity - Không cần Mac

Dự án này giúp bạn tạo file IPA từ Unity Xcode project mà **không cần**:
- ✅ Tài khoản Apple Developer trả phí
- ✅ Máy Mac
- ✅ Chứng chỉ iOS (bạn có cách ký riêng)

## Phương pháp

Sử dụng **GitHub Actions** với macOS runner miễn phí để tự động build IPA trên cloud.

## Đánh giá dự án iOS_iPA

Dự án [iOS_iPA](https://github.com/AmirBayat0/iOS_iPA) của AmirBayat0:
- ❌ **KHÔNG giúp được** cho Unity project
- Chỉ là Flutter project mẫu
- Không có automation tools cho Unity/Xcode

**Kết luận**: Dự án iOS_iPA chỉ phù hợp với Flutter, không áp dụng được cho Unity.

## Giải pháp được triển khai

✅ **GitHub Actions Workflow** tự động:
- Build Xcode project trên macOS runner
- Tạo file IPA không cần code signing
- Upload IPA dưới dạng artifact để download

## 🚀 Hướng dẫn sử dụng nhanh

### Cách 1: Tự động hoàn toàn (Khuyến nghị) ⚡

**Chỉ cần 1 lệnh, nhận IPA tự động!**

```bash
# Cài đặt thư viện (chỉ lần đầu)
pip install -r requirements.txt

# Tạo GitHub token tại: https://github.com/settings/tokens
# Quyền cần: repo, workflow, actions:read

# Set token (Windows PowerShell)
$env:GITHUB_TOKEN="ghp_your_token_here"

# Build IPA tự động (push → build → download)
python auto_build_ipa.py

# File IPA sẽ ở: output/NROFLY.ipa
```

📖 **Chi tiết**: Xem [AUTO_BUILD_GUIDE.md](AUTO_BUILD_GUIDE.md)

---

### Cách 2: Thủ công qua GitHub Actions

1. Vào GitHub repository → Tab **Actions**
2. Click **Run workflow** → Chọn configuration → **Run workflow**
3. Đợi build hoàn thành (10-20 phút)
4. Download IPA từ **Artifacts**

### 3. Sử dụng IPA

- File IPA được tạo **unsigned** (không có code signing)
- Sử dụng công cụ của bạn để ký lại và cài đặt

## Cấu trúc dự án

```
E:\IOSBUILD\
├── .github/
│   └── workflows/
│       └── build-ipa.yml           # GitHub Actions workflow
├── XCODE/                           # Unity Xcode project
│   ├── Unity-iPhone.xcodeproj
│   └── ...
├── auto_build_ipa.py                # 🚀 Tool tự động build IPA
├── AUTO_BUILD_GUIDE.md              # Hướng dẫn tool tự động
├── requirements.txt                 # Python dependencies
├── build_ipa_guide.md               # Hướng dẫn manual
└── README.md                        # File này
```

## Thông tin dự án Unity

- **Scheme**: `Unity-iPhone`
- **Bundle ID**: `com.NROFLY.NRO-FLY`
- **Product Name**: `NROFLY`

## 📚 Tài liệu

- 🚀 **[AUTO_BUILD_GUIDE.md](AUTO_BUILD_GUIDE.md)** - Hướng dẫn tool tự động (Khuyến nghị)
- 📖 **[build_ipa_guide.md](build_ipa_guide.md)** - Hướng dẫn build thủ công qua GitHub Actions

## Lưu ý quan trọng

1. **Code Signing**: IPA được tạo không có code signing. Bạn cần ký lại bằng công cụ của riêng bạn trước khi cài đặt.

2. **GitHub Limits**: 
   - Private repos: 2000 phút/tháng (miễn phí)
   - Public repos: Không giới hạn

3. **Build Time**: Mỗi build thường mất 10-20 phút tùy vào kích thước project.

## Troubleshooting

Nếu gặp vấn đề:
1. Kiểm tra logs trong GitHub Actions
2. Xem [build_ipa_guide.md](build_ipa_guide.md) phần Troubleshooting
3. Đảm bảo Xcode project hợp lệ

## License

Dự án này chỉ là tool/script hỗ trợ build, không liên quan đến license của Unity hoặc ứng dụng của bạn.

