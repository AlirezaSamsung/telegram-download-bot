import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# توکن ربات شما
TOKEN = "8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY"

# ایجاد ربات و دیسپچر
bot = Bot(token=TOKEN)
dp = Dispatcher()

# دستور /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود", callback_data="download")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی", callback_data="categories")],
        [types.InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="settings")]
    ])
    
    await message.answer(
        f"🎉 **سلام {message.from_user.first_name}!**\n\n"
        "✅ **ربات با موفقیت فعال شد!**\n\n"
        "✨ **قابلیت‌ها:**\n"
        "• دانلود فایل‌های مختلف\n"
        "• دسته‌بندی هوشمند\n"
        "• شخصی‌سازی کامل\n"
        "• سرعت بالا\n\n"
        "از منوی زیر انتخاب کن:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# دستور /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "📚 **راهنمای ربات:**\n\n"
        "🔹 `/start` - شروع ربات\n"
        "🔹 `/download` - دانلود فایل\n"
        "🔹 `/help` - این راهنما\n\n"
        "🎯 **نکته:** لینک فایل را مستقیم بفرست تا دانلود کنم!",
        parse_mode="Markdown"
    )

# پاسخ به callback دکمه‌ها
@dp.callback_query()
async def handle_callbacks(callback: types.CallbackQuery):
    data = callback.data
    
    if data == "download":
        await callback.message.edit_text(
            "🔗 **لطفا لینک را ارسال کن:**\n\n"
            "🎥 ویدیو (YouTube, Instagram)\n"
            "🎵 صوت (MP3, Voice)\n"
            "📷 عکس\n"
            "📄 فایل\n\n"
            "یا از دستور `/download` استفاده کن",
            parse_mode="Markdown"
        )
    
    elif data == "categories":
        await callback.message.edit_text(
            "📁 **دسته‌بندی‌ها:**\n\n"
            "1. ویدیو\n"
            "2. صوت\n"
            "3. عکس\n"
            "4. اسناد\n"
            "5. سایر\n\n"
            "به زودی قابل شخصی‌سازی خواهد بود!",
            parse_mode="Markdown"
        )
    
    elif data == "settings":
        await callback.message.edit_text(
            "⚙️ **تنظیمات:**\n\n"
            "🔹 کیفیت دانلود\n"
            "🔹 محل ذخیره‌سازی\n"
            "🔹 قالب فایل\n"
            "🔹 زبان\n\n"
            "به زودی...",
            parse_mode="Markdown"
        )
    
    await callback.answer()

# هندلر عمومی برای لینک‌ها
@dp.message()
async def handle_links(message: types.Message):
    text = message.text or ""
    
    if any(domain in text.lower() for domain in ['http://', 'https://', 'youtube', 'instagram', 't.me']):
        await message.answer(
            f"🔍 **لینک شناسایی شد!**\n\n"
            f"📎 `{text[:50]}...`\n\n"
            "⏳ در حال پردازش...\n"
            "به زودی سیستم دانلود اضافه می‌شود!",
            parse_mode="Markdown"
        )

# تابع اصلی
async def main():
    print("=" * 60)
    print("🤖 **ربات دانلود تلگرام**")
    print("🛜 VPN فعال: بله")
    print("🔗 آدرس ربات: https://t.me/8595890168_bot")
    print("=" * 60)
    
    try:
        # تست اتصال
        print("\n🔍 در حال تست اتصال به تلگرام...")
        me = await bot.get_me()
        print(f"✅ متصل شد! ربات: @{me.username}")
        
        print("\n" + "=" * 60)
        print("🎉 **ربات آماده است!**")
        print("📱 به تلگرام برو و ربات را تست کن:")
        print("1. ربات را پیدا کن: @8595890168_bot")
        print("2. روی Start کلیک کن")
        print("3. از منو استفاده کن")
        print("=" * 60 + "\n")
        
        # شروع ربات
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"\n❌ **خطا در اتصال:** {e}")
        print("\n🔧 **راه‌حل:**")
        print("1. مطمئن شو VPN روشن است")
        print("2. VPN را عوض کن")
        print("3. چند ثانیه صبر کن دوباره امتحان کن")
        print("4. از VPN با سرور کشور دیگری استفاده کن")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 ربات خاموش شد!")