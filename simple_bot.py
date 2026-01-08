import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# تنظیمات ساده
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=" * 60)
print("🤖 Simple Telegram Bot - Render")
print("=" * 60)

# خواندن توکن
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN not found!")
    logger.info("💡 Add BOT_TOKEN in Render Environment Variables")
    exit(1)

print(f"✅ Bot Token loaded")

# ساخت ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    """دستور شروع"""
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود", callback_data="download")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی", callback_data="categories")]
    ])
    
    await message.answer(
        f"👋 سلام {message.from_user.first_name}!\n\n"
        "✅ ربات روی Render فعال شد!\n\n"
        "📌 لینک را بفرست تا دانلود کنم...",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "📚 راهنما:\n\n"
        "/start - شروع\n"
        "/download - دانلود\n"
        "/help - راهنما\n\n"
        "🔗 لینک را مستقیماً بفرست",
        parse_mode="Markdown"
    )

@dp.message()
async def handle_links(message: types.Message):
    if message.text and message.text.startswith("http"):
        await message.answer(
            f"🔗 لینک دریافت شد:\n`{message.text[:50]}...`\n\n"
            "⏳ سیستم دانلود به زودی...",
            parse_mode="Markdown"
        )

async def main():
    print("🔗 Connecting to Telegram...")
    
    try:
        me = await bot.get_me()
        print(f"✅ Connected! Bot: @{me.username}")
        
        print("\n" + "=" * 60)
        print("🚀 Bot is ready!")
        print(f"📱 Test: @{me.username}")
        print("=" * 60)
        
        await dp.start_polling(bot)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # برای Render: یک سرور ساده HTTP هم راه می‌اندازیم
    from aiohttp import web
    
    async def health(request):
        return web.Response(text="Bot is running")
    
    # فقط اگر PORT تعریف شده باشد
    PORT = os.environ.get("PORT")
    if PORT:
        async def run_server():
            app = web.Application()
            app.router.add_get('/', health)
            app.router.add_get('/health', health)
            
            runner = web.AppRunner(app)
            await runner.setup()
            await web.TCPSite(runner, '0.0.0.0', int(PORT)).start()
            print(f"🌐 Health check on port {PORT}")
        
        # اجرای همزمان
        async def run_all():
            await asyncio.gather(
                run_server(),
                main()
            )
        
        asyncio.run(run_all())
    else:
        asyncio.run(main())