# Cách tìm nút "Run workflow" - Hướng dẫn chi tiết với hình ảnh

## Vấn đề

Bạn đang ở trang **chi tiết của một workflow run** (có "Summary", "Jobs", etc.) → Trang này **KHÔNG có nút "Run workflow"**.

## Cách tìm nút "Run workflow"

### Bước 1: Quay lại trang Workflow Overview

**Có 2 cách:**

#### Cách 1: Click vào tên workflow trong sidebar (Dễ nhất)

1. Nhìn vào **sidebar bên trái**
2. Tìm dòng: **`.github/workflows/build-ipa.yml`**
3. **Click vào text đó** (click vào `.github/workflows/build-ipa.yml`)
4. Trang sẽ chuyển sang trang **overview của workflow** (không phải trang run detail)

#### Cách 2: Click mũi tên quay lại

1. Ở đầu trang bạn đang xem, có mũi tên **←** (quay lại)
2. Bên cạnh có text: **`.github/workflows/build-ipa.yml`**
3. **Click vào text đó** hoặc mũi tên
4. Sẽ quay về trang workflow overview

### Bước 2: Tìm nút "Run workflow"

Sau khi vào trang **workflow overview** (không phải trang run detail):

1. **Nhìn góc phải trên cùng** của trang
2. Bạn sẽ thấy nút lớn màu xanh lá/xanh dương: **"Run workflow"** 
3. Nút này nằm **ngay dưới thanh tìm kiếm "Filter workflow runs"**

## Hình ảnh minh họa vị trí

```
┌─────────────────────────────────────────┐
│  Repository name                         │
├─────────────────────────────────────────┤
│  [←] .github/workflows/build-ipa.yml     │ ← Click vào đây
├─────────────────────────────────────────┤
│                    [Filter] [Run workflow] ← NÚT Ở ĐÂY!
│                                           │
│  Workflow runs:                          │
│  - Initial commit (failed)               │
│  - ...                                   │
└─────────────────────────────────────────┘
```

## Kiểm tra bạn đang ở đúng trang chưa

### ❌ Trang SAI (Không có nút "Run workflow"):

- Có tab "Summary", "Jobs", "Run details"
- Có text "Triggered via push X minutes ago"
- Có phần "Workflow graph" hoặc "Annotations"
- **→ Đây là trang CHI TIẾT của một run cụ thể**

### ✅ Trang ĐÚNG (Có nút "Run workflow"):

- **Không có** tab "Summary", "Jobs" ở trên
- **Có** danh sách tất cả workflow runs
- **Có** nút **"Run workflow"** ở góc phải trên
- Tiêu đề trang là tên workflow file, không phải tên run

## Sau khi tìm thấy nút "Run workflow"

1. **Click "Run workflow"**
2. Popup sẽ hiện:
   - **Branch**: Chọn `main`
   - **Build configuration**: Chọn `Release` hoặc `Debug`
3. **Click nút "Run workflow"** màu xanh ở dưới popup
4. Workflow sẽ bắt đầu chạy

## Lưu ý quan trọng

- **Nút "Run workflow" KHÔNG có** ở trang run detail (trang bạn đang xem)
- **Chỉ có** ở trang workflow overview
- Để vào trang overview: Click tên workflow trong sidebar bên trái

## Tóm tắt nhanh

1. Sidebar bên trái → Click **`.github/workflows/build-ipa.yml`**
2. Góc phải trên → Nút **"Run workflow"**
3. Chọn branch + config → Click **"Run workflow"**

