# Hướng dẫn setup Codemagic (Thay thế GitHub Actions)

## Tại sao Codemagic?

- ✅ Miễn phí: 500 phút/tháng
- ✅ Không cần credit card
- ✅ Hỗ trợ Unity iOS builds
- ✅ Dễ setup

## Cách setup

### Bước 1: Đăng ký Codemagic

1. Vào: https://codemagic.io
2. Click "Get started"
3. Đăng nhập bằng GitHub account
4. Cho phép Codemagic truy cập repositories

### Bước 2: Add Application

1. Từ dashboard, click "Add application"
2. Chọn repository: `cuong1206/IPA_UNITY_FULL`
3. Chọn platform: **iOS**
4. Click "Next"

### Bước 3: Configure Workflow

1. Codemagic sẽ tự detect Xcode project
2. Chọn **Xcode project** type
3. Project path: `XCODE/Unity-iPhone.xcodeproj`
4. Scheme: `Unity-iPhone`

### Bước 4: Build Configuration

Trong file `codemagic.yaml` (sẽ được tạo), sửa như sau:

```yaml
workflows:
  unity-ios-workflow:
    name: Unity iOS Build
    max_build_duration: 120
    instance_type: mac_mini_m1
    environment:
      groups:
        - app_store_credentials
      vars:
        XCODE_WORKSPACE: "XCODE/Unity-iPhone.xcodeproj"
        XCODE_SCHEME: "Unity-iPhone"
        BUNDLE_ID: "com.NROFLY.NRO-FLY"
      xcode: latest
    scripts:
      - name: Build IPA
        script: |
          cd XCODE
          xcodebuild clean archive \
            -project Unity-iPhone.xcodeproj \
            -scheme Unity-iPhone \
            -configuration Release \
            -archivePath build/Unity-iPhone.xcarchive \
            CODE_SIGN_IDENTITY="" \
            CODE_SIGNING_REQUIRED=NO \
            CODE_SIGNING_ALLOWED=NO \
            -destination "generic/platform=iOS"
          
          # Create IPA manually
          mkdir -p build/export/Payload
          cp -R build/Unity-iPhone.xcarchive/Products/Applications/*.app build/export/Payload/
          cd build/export
          zip -r NROFLY.ipa Payload/
    artifacts:
      - XCODE/build/export/*.ipa
    publishing:
      email:
        recipients:
          - your-email@example.com
```

### Bước 5: Chạy Build

1. Click "Start new build"
2. Chọn workflow
3. Đợi build hoàn thành (10-20 phút)
4. Download IPA từ Artifacts

## Lưu ý

- Build sẽ tạo unsigned IPA (giống GitHub Actions)
- Có thể setup tự động build khi push code
- Free tier: 500 phút/tháng

