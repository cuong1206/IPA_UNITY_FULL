# Sửa lỗi "Invalid payment method - authorization hold failed"

## Lỗi bạn gặp phải

**"Invalid payment method - authorization hold failed"**

Điều này có nghĩa GitHub không thể xác minh thẻ của bạn (không phải là không đủ tiền, mà là không thể kiểm tra thẻ).

## Các cách sửa lỗi

### Cách 1: Điền đầy đủ Billing Information (Thử ngay)

Trên trang Payment Information bạn đang xem:

1. **Cuộn xuống phần "Billing information"**
2. **Điền đầy đủ tất cả các trường**:
   - First name *
   - Last name *
   - Address (Street, P.O. box) *
   - City *
   - Country/Region * (chọn từ dropdown)
   - State/Province (nếu yêu cầu)
   - Postal/Zip code *
3. **Click "Save billing information"** (nút màu xanh lá cây)

Sau đó thử thêm payment method lại.

### Cách 2: Kiểm tra lại thông tin thẻ

**Nguyên nhân thường gặp:**

❌ Số thẻ sai  
❌ Ngày hết hạn sai  
❌ CVV sai  
❌ Tên trên thẻ không khớp  
❌ Thẻ bị khóa/tạm khóa  
❌ Ngân hàng chặn giao dịch quốc tế

**Cách xử lý:**

1. **Kiểm tra lại thông tin thẻ**:
   - So sánh số thẻ, ngày hết hạn, CVV với thẻ vật lý
   - Đảm bảo tên chủ thẻ khớp với thẻ

2. **Liên hệ ngân hàng**:
   - Gọi hotline ngân hàng
   - Hỏi: "Thẻ của tôi có bị chặn giao dịch quốc tế không?"
   - Yêu cầu mở khóa giao dịch quốc tế (nếu bị chặn)
   - Nói là cần để xác minh thẻ với GitHub (không phải thanh toán thực)

3. **Thử thẻ khác** (nếu có):
   - Thẻ Visa/Mastercard khác
   - Hoặc thẻ từ ngân hàng khác

### Cách 3: Xóa và thêm lại Payment Method

1. Tìm phần hiển thị payment method hiện tại
2. Click **"Remove"** hoặc **"Delete"** để xóa thẻ cũ
3. Click **"Add payment method"** lại
4. Nhập thông tin thẻ mới (kiểm tra kỹ lại)
5. **Đảm bảo đã điền đầy đủ Billing information** trước khi thêm thẻ

### Cách 4: Thử phương thức thanh toán khác

Nếu GitHub hỗ trợ:
- **PayPal** (nếu có tài khoản)
- **Prepaid card** (thẻ trả trước)
- **Thẻ từ ngân hàng quốc tế** (nếu có)

## Giải pháp KHÔNG CẦN Payment Method

### ✅ Giải pháp 1: Tạo Public Repository (Khuyến nghị nhất)

**Public repositories có unlimited GitHub Actions, KHÔNG CẦN payment method!**

**Cách làm:**

1. Vào repository: https://github.com/cuong1206/IPA_UNITY_FULL
2. Click **Settings** (tab trên cùng)
3. Cuộn xuống cuối → phần **"Danger Zone"**
4. Click **"Change visibility"**
5. Chọn **"Make public"**
6. Nhập tên repo để xác nhận: `cuong1206/IPA_UNITY_FULL`
7. Click **"I understand, change repository visibility"**

**Sau đó:**
- GitHub Actions sẽ hoạt động ngay
- Không cần payment method
- Unlimited build time

**Lưu ý:** Code sẽ public (ai cũng xem được). Nếu code không nhạy cảm, đây là cách tốt nhất.

### ✅ Giải pháp 2: Dùng Codemagic (Không cần payment method)

**Codemagic không yêu cầu payment method:**

1. Đăng ký: https://codemagic.io
2. Connect GitHub account
3. Chọn repository: `cuong1206/IPA_UNITY_FULL`
4. Setup build workflow (xem `codemagic_setup.md`)
5. Build miễn phí 500 phút/tháng

### ✅ Giải pháp 3: Dùng AppCircle

1. Đăng ký: https://appcircle.io
2. Upload Xcode project
3. Build trên cloud
4. Không cần payment method

## Khuyến nghị theo thứ tự ưu tiên

### 1. Tạo Public Repository (Nhanh nhất - 2 phút)
✅ Không cần payment method  
✅ Unlimited Actions  
✅ Hoạt động ngay  
⚠️ Code sẽ public

### 2. Điền Billing Information + Thử lại thẻ (5 phút)
✅ Giữ code private  
✅ 2000 phút/tháng miễn phí  
⚠️ Có thể vẫn gặp lỗi nếu thẻ/thẻ có vấn đề

### 3. Dùng Codemagic (10 phút setup)
✅ Không cần payment method  
✅ Giữ code private  
⚠️ Chỉ 500 phút/tháng (vẫn đủ dùng)

## Hướng dẫn từng bước: Tạo Public Repo (Cách nhanh nhất)

Nếu code không nhạy cảm, làm theo các bước sau:

1. **Vào repository**: https://github.com/cuong1206/IPA_UNITY_FULL
2. **Click tab "Settings"** (ở thanh menu trên cùng)
3. **Cuộn xuống cuối trang** → tìm phần **"Danger Zone"**
4. **Click "Change visibility"**
5. **Chọn "Make this repository public"**
6. **Nhập tên repo để xác nhận**: `cuong1206/IPA_UNITY_FULL`
7. **Click nút đỏ "I understand, change repository visibility"**

Sau 10 giây:
- Vào tab **Actions**
- Workflow sẽ không còn cảnh báo billing
- Có thể chạy build ngay

## Nếu vẫn muốn giữ Private Repo

Thử các bước sau theo thứ tự:

1. ✅ **Điền đầy đủ Billing Information** (First name, Last name, Address, City, Country, Zip code)
2. ✅ **Lưu Billing Information** (click nút "Save billing information")
3. ✅ **Xóa payment method cũ** (nếu có)
4. ✅ **Liên hệ ngân hàng** để mở khóa giao dịch quốc tế
5. ✅ **Thêm lại payment method** với thông tin đã kiểm tra kỹ
6. ✅ **Đợi 5-10 phút** để GitHub xử lý

Nếu sau 30 phút vẫn lỗi → Chuyển sang Public Repo hoặc dùng Codemagic.

## Tóm tắt

**Cách nhanh nhất (khuyến nghị):**
→ Chuyển repository sang **Public** → Không cần payment method → Unlimited Actions

**Cách giữ private:**
→ Điền đầy đủ Billing Information → Liên hệ ngân hàng → Thử lại thẻ

**Cách thay thế:**
→ Dùng **Codemagic** → Không cần payment method → 500 phút/tháng miễn phí

Bạn muốn thử cách nào?

