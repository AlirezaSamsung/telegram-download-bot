import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# تنظیمات
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=" * 60)
print("🤖 Telegram Download Bot - Render Deployment")
print("=" * 60)

# خواندن توکن
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "8057684663")

if not BOT_TOKEN:
    logger.error("❌ ERROR: BOT_TOKEN not found!")
    logger.info("💡 Add BOT_TOKEN in Render Environment Variables")
    exit(1)

print(f"✅ Bot Token: {BOT_TOKEN[:10]}...")
print(f"✅ Admin ID: {ADMIN_ID}")

# پورت برای Render
PORT = int(os.environ.get("PORT", 8080))

# ایجاد ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ================== دستورات ربات ==================

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود", callback_data="download")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی", callback_data="categories")],
        [types.InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="settings")]
    ])
    
    await message.answer(
        f"✨ **سلام {message.from_user.first_name}!**\n\n"
        "🎉 **ربات روی Render فعال شد!**\n\n"
        "✅ **ویژگی‌ها:**\n"
        "• ۲۴/۷ آنلاین\n"
        "• سرعت بالا\n"
        "• بدون نیاز به VPN\n"
        "• دانلود از ۱۰۰+ سایت\n\n"
        "📌 **لینک را بفرستید...**",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📚 **راهنمای ربات:**\n\n"
        "🔸 **دستورات:**\n"
        "/start - شروع\n"
        "/download - دانلود\n"
        "/help - راهنما\n\n"
        "🔸 **سایت‌های پشتیبانی:**\n"
        "YouTube, Instagram, Twitter, TikTok\n\n"
        "⚡ **سرور:** Render.com",
        parse_mode="Markdown"
    )

@dp.message(Command("download"))
async def download_command(message: types.Message):
    await message.answer(
        "📥 **لینک را بفرستید:**\n\n"
        "🎥 ویدیو: https://youtube.com/...\n"
        "📷 عکس: https://instagram.com/...\n"
        "🎵 صوت: https://soundcloud.com/...\n\n"
        "⚡ سیستم به زودی کامل می‌شود!",
        parse_mode="Markdown"
    )

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == "download":
        await callback.message.answer("🔗 لینک را بفرستید...")
    elif callback.data == "categories":
        await callback.message.answer("📁 دسته‌بندی‌ها به زودی...")
    elif callback.data == "settings":
        await callback.message.answer("⚙️ تنظیمات به زودی...")
    
    await callback.answer()

@dp.message()
async def handle_messages(message: types.Message):
    if message.text and message.text.startswith("http"):
        await message.answer(
            f"🔗 **لینک دریافت شد!**\n\n"
            f"`{message.text[:50]}...`\n\n"
            "⏳ در حال پردازش...\n"
            "✅ **سرور:** Render.com",
            parse_mode="Markdown"
        )

# ================== وب سرور برای Render ==================

async def health_check(request):
    """صفحه سلامت برای Render"""
    return web.Response(text="🤖 Telegram Bot is running on Render!")

async def start_web_server():
    """شروع وب سرور برای Render"""
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)
    app.router.add_get("/status", health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    
    logger.info(f"🌐 Web server started on port {PORT}")
    return runner

async def start_bot():
    """شروع ربات تلگرام"""
    try:
        me = await bot.get_me()
        logger.info(f"✅ Bot connected: @{me.username}")
        
        # شروع ربات
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")

async def main():
    """تابع اصلی"""
    logger.info("🚀 Starting services...")
    
    # شروع وب سرور
    runner = await start_web_server()
    
    # شروع ربات در background
    bot_task = asyncio.create_task(start_bot())
    
    print("\n" + "=" * 60)
    print("✅ **Services started successfully!**")
    print(f"🌐 Web server: http://0.0.0.0:{PORT}")
    print("🤖 Telegram bot is running...")
    print("📱 Go to Telegram and test: @8595890168_bot")
    print("=" * 60 + "\n")
    
    try:
        # نگه داشتن هر دو سرویس
        await asyncio.gather(bot_task)
    except KeyboardInterrupt:
        logger.info("👋 Shutting down...")
    finally:
        await runner.cleanup()
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())