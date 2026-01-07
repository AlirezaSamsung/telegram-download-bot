import os
from dotenv import load_dotenv

# بارگذاری تنظیمات
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# تنظیمات پروکسی (برای ایران)
PROXY_URL = "http://proxy.server:3128"  # اگر پروکسی داری اینجا بزار
# یا از پروکسی‌های رایگان:
PROXY_AIOHTTP = "http://138.201.223.250:3128"  # پروکسی نمونه

print("=" * 50)
print("✅ تنظیمات بارگذاری شد!")
print("⚠️  در حال استفاده از حالت پروکسی...")
print("=" * 50)