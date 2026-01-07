import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

print("=" * 60)
print("🚀 ربات تلگرام روی Railway")
print("📅 شروع: ", __import__('datetime').datetime.now())
print("=" * 60)

# خواندن توکن از محیط
BOT_TOKEN = os.getenv("BOT_TOKEN", "8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY")
ADMIN_ID = os.getenv("ADMIN_ID", "8057684663")

if "توکن" in BOT_TOKEN or len(BOT_TOKEN) < 10:
    print("❌ توکن تنظیم نشده! در Railway Variables تنظیم کن")
    exit()

# ساخت ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    """دستور شروع"""
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود", callback_data="dl")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی", callback_data="cat")],
        [types.InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="set")]
    ])
    
    await message.answer(
        f"🌟 **سلام {message.from_user.first_name}!**\n\n"
        "✅ **ربات روی Railway فعال شد!**\n\n"
        "⚡ **مزایا:**\n"
        "• ۲۴ ساعته آنلاین\n"
        "• سرعت بالا\n"
        "• بدون قطعی\n\n"
        "📌 **آماده دانلود!**\n"
        "لینک را بفرست...",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    """دستور راهنما"""
    await message.answer(
        "📖 **راهنما:**\n\n"
        "🔸 لینک را بفرست\n"
        "🔸 کیفیت را انتخاب کن\n"
        "🔸 دانلود شروع می‌شود!\n\n"
        "🛠 **پشتیبانی:** @",
        parse_mode="Markdown"
    )

@dp.message()
async def echo(message: types.Message):
    """پاسخ به پیام‌های معمولی"""
    if message.text and message.text.startswith("http"):
        await message.answer(
            f"🔗 **لینک دریافت شد!**\n\n"
            f"`{message.text[:50]}...`\n\n"
            "⏳ سیستم دانلود به زودی...\n"
            "✅ **سرور:** Railway.app 🇺🇸",
            parse_mode="Markdown"
        )

async def main():
    """تابع اصلی"""
    print("🔍 در حال اتصال به تلگرام...")
    
    try:
        # تست اتصال
        me = await bot.get_me()
        print(f"✅ متصل شد! ربات: @{me.username}")
        
        print("\n" + "=" * 60)
        print("🤖 ربات آماده است!")
        print("📱 به تلگرام برو و:")
        print(f"1. @{me.username} را سرچ کن")
        print("2. Start بزن")
        print("3. /help را تست کن")
        print("=" * 60)
        
        # شروع ربات
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"❌ خطا: {e}")
        print("\n🔧 راه‌حل: توکن را در Railway Variables چک کن")

if __name__ == "__main__":
    asyncio.run(main())