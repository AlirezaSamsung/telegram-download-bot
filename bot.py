import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

print("=" * 60)
print("🚀 Telegram Download Bot - Final Version")
print("=" * 60)

# خواندن توکن
BOT_TOKEN = os.getenv("BOT_TOKEN", "8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY")
ADMIN_ID = os.getenv("ADMIN_ID", "8057684663")

if not BOT_TOKEN or "توکن" in BOT_TOKEN:
    print("❌ ERROR: Invalid BOT_TOKEN!")
    print("💡 Set BOT_TOKEN in Render Environment Variables")
    exit(1)

print(f"✅ Bot: {BOT_TOKEN[:10]}...")
print(f"✅ Admin: {ADMIN_ID}")

# ساخت ربات
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"🎉 **سلام {message.from_user.first_name}!**\n\n"
        "✅ **ربات فعال شد!**\n\n"
        "📌 لینک را بفرستید تا دانلود کنم...\n\n"
        "🔗 مثال: https://youtube.com/...",
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "📚 **راهنما:**\n"
        "/start - شروع\n"
        "/help - این صفحه\n\n"
        "🔗 لینک را مستقیماً بفرستید",
        parse_mode="Markdown"
    )

@dp.message()
async def handle_links(message: types.Message):
    if message.text and message.text.startswith("http"):
        await message.answer(
            f"🔗 **دریافت شد:**\n`{message.text[:50]}...`\n\n"
            "⏳ به زودی دانلود می‌شود...",
            parse_mode="Markdown"
        )

async def main():
    try:
        me = await bot.get_me()
        print(f"✅ Connected: @{me.username}")
        
        print("\n" + "=" * 60)
        print("🤖 **Bot is running!**")
        print(f"📱 Test: @{me.username}")
        print("=" * 60)
        
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())