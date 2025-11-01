# Hướng dẫn sửa GitHub Billing để chạy GitHub Actions

## Vấn đề

GitHub Actions bị khóa với thông báo: **"Your account's billing is currently locked"**

## Giải pháp từng bước

### Bước 1: Vào Payment Information

1. Từ trang Billing Overview hiện tại
2. Click vào **"Payment information"** ở thanh bên trái (dưới mục "Billing and licensing")
3. Hoặc vào trực tiếp: https://github.com/settings/billing/payment

### Bước 2: Kiểm tra trạng thái Payment Method

Bạn sẽ thấy một trong các trường hợp:

#### Trường hợp A: Chưa có Payment Method

**Nếu thấy "No payment method" hoặc yêu cầu thêm:**
1. Click **"Add payment method"** hoặc **"Add credit or debit card"**
2. Nhập thông tin thẻ (Credit/Debit card)
   - Số thẻ
   - Ngày hết hạn
   - CVV
   - Tên chủ thẻ
   - Địa chỉ (nếu yêu cầu)
3. Click **"Add payment method"**

**Lưu ý quan trọng:**
- GitHub Free plan **KHÔNG tính phí** nếu bạn chỉ dùng trong giới hạn
- Private repos: 2000 phút Actions/tháng miễn phí
- Public repos: Không giới hạn Actions
- Bạn chỉ bị tính phí nếu vượt quá giới hạn

#### Trường hợp B: Payment Method đã hết hạn/Lỗi

**Nếu thẻ cũ bị từ chối:**
1. Click **"Update"** hoặc **"Edit"** bên cạnh payment method
2. Cập nhật thông tin thẻ mới
3. Hoặc xóa thẻ cũ và thêm thẻ mới

#### Trường hợp C: Có Payment Method nhưng vẫn bị lock

1. Kiểm tra xem có email cảnh báo từ GitHub không
2. Vào **"Payment history"** để xem có khoản phí chưa thanh toán không
3. Liên hệ GitHub Support nếu vấn đề vẫn tiếp diễn

### Bước 3: Xác nhận Free Plan

Sau khi thêm payment method:

1. Quay lại **"Overview"** trong Billing
2. Kiểm tra phần **"Subscriptions"**:
   - Nên thấy **"GitHub Free"** - $0.00/month ✅
   - Không cần upgrade lên Pro/Team trừ khi bạn cần

3. Kiểm tra **"Usage"**:
   - Vào **"Usage"** tab
   - Xem giới hạn Actions: **2000 phút/tháng** cho private repos
   - Public repos: **Unlimited** ✅

### Bước 4: Test GitHub Actions

Sau khi sửa billing:

1. Vào repository: https://github.com/cuong1206/IPA_UNITY_FULL
2. Tab **Actions**
3. Workflow **"Build iOS IPA"** (hoặc `.github/workflows/build-ipa.yml`) sẽ không còn cảnh báo billing
4. Click **"Run workflow"** để test

## Giải thích về GitHub Free Plan

### Bạn có thể làm gì miễn phí:

✅ **Private repositories**: 
- 2000 phút GitHub Actions/tháng
- Đủ cho ~100 builds IPA/tháng (mỗi build ~20 phút)

✅ **Public repositories**:
- **Unlimited** GitHub Actions
- Không giới hạn phút

### Khi nào bị tính phí:

❌ Chỉ khi vượt quá 2000 phút/tháng cho private repos
❌ Sử dụng Codespaces (tính phí riêng)
❌ Sử dụng Packages (tính phí riêng)

**Build IPA của bạn:**
- Mỗi build ~15-20 phút
- 2000 phút = ~100 builds/tháng
- **Hoàn toàn miễn phí** nếu trong giới hạn

## Nếu không muốn thêm Payment Method

### Giải pháp thay thế:

1. **Chuyển sang Public Repository** (khuyến nghị):
   - Public repos có unlimited Actions
   - Không cần payment method
   - Code sẽ public (ai cũng thấy)

2. **Dùng Codemagic hoặc AppCircle**:
   - Không cần payment method
   - Free tier tốt
   - Xem `alternative_solutions.md`

## Troubleshooting

### Vẫn bị lock sau khi thêm payment method:

1. Đợi 5-10 phút (GitHub cần xử lý)
2. Refresh trang Actions
3. Thử chạy workflow lại
4. Nếu vẫn lỗi, kiểm tra email từ GitHub

### Không có thẻ tín dụng:

**Giải pháp:**
- Tạo **Public repository** → Không cần payment method
- Hoặc dùng **prepaid card** (thẻ trả trước)
- Hoặc dùng **PayPal** (nếu GitHub hỗ trợ)

## Tóm tắt nhanh

1. Vào: https://github.com/settings/billing/payment
2. Click **"Add payment method"**
3. Nhập thông tin thẻ (không bị tính phí nếu trong giới hạn)
4. Đợi 5 phút
5. Test workflow lại

**Hoặc:**
- Tạo **Public repository** → Không cần payment method → Unlimited Actions

