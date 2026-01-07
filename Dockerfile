# خط ۱: استفاده از Python نسخه ۱۱
FROM python:3.11-slim

# خط ۲: ساخت پوشه /app در سرور
WORKDIR /app

# خط ۳: کپی کردن فایل requirements.txt
COPY requirements.txt .

# خط ۴: نصب کتابخانه‌ها
RUN pip install --no-cache-dir -r requirements.txt

# خط ۵: کپی کردن همه فایل‌های پروژه
COPY . .

# خط ۶: دستور اجرای ربات
CMD ["python", "railway_bot.py"]