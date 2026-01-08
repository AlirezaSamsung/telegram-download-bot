import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

print("=" * 60)
print("🚀 ربات تلگرام - Railway Deployment")
print("=" * 60)

# خواندن توکن از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "8057684663")

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN not found in environment variables!")
    print("💡 Solution: Add BOT_TOKEN in Railway Variables")
    exit(1)

print(f"✅ BOT_TOKEN loaded: {BOT_TOKEN[:10]}...")
print(f"✅ ADMIN_ID: {ADMIN_ID}")

# ایجاد ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    """دستور شروع"""
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود فایل", callback_data="download")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی‌ها", callback_data="categories")],
        [types.InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="settings")],
        [types.InlineKeyboardButton(text="📊 راهنما", callback_data="help")]
    ])
    
    await message.answer(
        f"✨ **سلام {message.from_user.first_name}!**\n\n"
        "🎉 **ربات با موفقیت روی Railway راه‌اندازی شد!**\n\n"
        "✅ **ویژگی‌ها:**\n"
        "• ۲۴/۷ آنلاین\n"
        "• سرعت بالا\n"
        "• بدون نیاز به VPN\n"
        "• دانلود از ۱۰۰+ سایت\n\n"
        "📌 **نحوه استفاده:**\n"
        "لینک را بفرستید → کیفیت را انتخاب کنید → دانلود!\n\n"
        "**از منوی زیر انتخاب کنید:**",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    """دستور راهنما"""
    await message.answer(
        "📚 **راهنمای ربات:**\n\n"
        "🔸 **دستورات اصلی:**\n"
        "/start - شروع ربات\n"
        "/download - دانلود فایل\n"
        "/help - این راهنما\n\n"
        "🔸 **سایت‌های پشتیبانی شده:**\n"
        "• YouTube\n• Instagram\n• Twitter\n• TikTok\n• SoundCloud\n\n"
        "🔸 **لینک تست:**\n"
        "https://youtu.be/dQw4w9WgXcQ\n\n"
        "⚡ **سرور:** Railway.app 🇺🇸",
        parse_mode="Markdown"
    )

@dp.message(Command("download"))
async def download_command(message: types.Message):
    """دستور دانلود"""
    await message.answer(
        "📥 **سیستم دانلود**\n\n"
        "🔗 **لطفاً لینک را ارسال کنید:**\n\n"
        "🎬 **ویدیو:**\n"
        "https://youtube.com/watch?v=...\n"
        "https://instagram.com/p/...\n\n"
        "🎵 **صوت:**\n"
        "https://soundcloud.com/...\n"
        "https://spotify.com/...\n\n"
        "📷 **عکس:**\n"
        "https://pinterest.com/...\n"
        "https://imgur.com/...\n\n"
        "⚡ **ویژگی‌ها:**\n"
        "• کیفیت قابل انتخاب\n"
        "• سرعت بالا\n"
        "• پشتیبانی از حجم‌های مختلف",
        parse_mode="Markdown"
    )

@dp.callback_query()
async def handle_buttons(callback: types.CallbackQuery):
    """مدیریت دکمه‌های اینلاین"""
    if callback.data == "download":
        await callback.message.answer(
            "🔗 **لطفاً لینک را بفرستید:**\n\n"
            "مثال‌ها:\n"
            "• ویدیو: https://youtube.com/watch?v=...\n"
            "• عکس: https://instagram.com/p/...\n"
            "• صوت: https://soundcloud.com/...\n\n"
            "⚡ سیستم به زودی کامل می‌شود!",
            parse_mode="Markdown"
        )
    
    elif callback.data == "categories":
        await callback.message.answer(
            "📁 **دسته‌بندی‌ها:**\n\n"
            "1. **ویدیو**\n"
            "2. **صوت**\n"
            "3. **عکس**\n"
            "4. **اسناد**\n\n"
            "✨ به زودی قابل شخصی‌سازی!",
            parse_mode="Markdown"
        )
    
    elif callback.data == "settings":
        await callback.message.answer(
            "⚙️ **تنظیمات:**\n\n"
            "🔸 **کیفیت پیش‌فرض:**\n"
            "🔸 **محل ذخیره‌سازی:**\n"
            "🔸 **زبان:**\n"
            "🔸 **سایر تنظیمات:**\n\n"
            "🛠️ **به زودی قابل تنظیم...**",
            parse_mode="Markdown"
        )
    
    elif callback.data == "help":
        await callback.message.answer(
            "❓ **پرسش‌های متداول:**\n\n"
            "🔹 **آیا ربات رایگان است؟**\n"
            "بله! کاملاً رایگان\n\n"
            "🔹 **حداکثر حجم دانلود؟**\n"
            "تا 2GB پشتیبانی می‌شود\n\n"
            "🔹 **چرا بعضی لینک‌ها کار نمی‌کنند؟**\n"
            "برخی سایت‌ها محدودیت دارند\n\n"
            "📞 **پشتیبانی:**\n"
            "اگر مشکل دارید، پیام بفرستید",
            parse_mode="Markdown"
        )
    
    await callback.answer()

@dp.message()
async def handle_messages(message: types.Message):
    """مدیریت پیام‌های معمولی"""
    text = message.text or ""
    
    if text.startswith("http"):
        await message.answer(
            f"🔗 **لینک دریافت شد!**\n\n"
            f"`{text[:50]}...`\n\n"
            "⏳ **در حال پردازش...**\n"
            "سیستم دانلود به زودی اضافه می‌شود!\n\n"
            "✅ **سرور:** Railway.app 🇺🇸",
            parse_mode="Markdown"
        )
    
    elif text and not text.startswith("/"):
        await message.answer(
            "🤖 **ربات دانلود تلگرام**\n\n"
            "برای شروع /start را بزنید\n"
            "برای راهنما /help را بفرستید\n\n"
            "🔥 **ویژگی‌ها:**\n"
            "• دانلود از لینک\n"
            "• دسته‌بندی\n"
            "• شخصی‌سازی\n"
            "• سرعت بالا",
            parse_mode="Markdown"
        )

async def main():
    """تابع اصلی"""
    print("🔍 در حال اتصال به تلگرام...")
    
    try:
        # تست اتصال
        me = await bot.get_me()
        print(f"✅ اتصال موفق! ربات: @{me.username}")
        print(f"✅ نام ربات: {me.first_name}")
        print(f"✅ ID ربات: {me.id}")
        
        print("\n" + "=" * 60)
        print("🤖 **ربات آماده است!**")
        print("📱 **مراحل تست:**")
        print(f"1. تلگرام را باز کن")
        print(f"2. این آدرس را سرچ کن: @{me.username}")
        print(f"3. روی Start کلیک کن")
        print(f"4. از منو استفاده کن")
        print("=" * 60 + "\n")
        
        # شروع ربات
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"❌ خطا در اتصال: {e}")
        print("\n🔧 **راه‌حل‌های احتمالی:**")
        print("1. توکن BOT_TOKEN را در Railway Variables چک کن")
        print("2. مطمئن شو توکن از @BotFather گرفته شده")
        print("3. دوباره Redeploy کن")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 ربات خاموش شد!")
    except Exception as e:
        print(f"\n❌ خطای غیرمنتظره: {e}")