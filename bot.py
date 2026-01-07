import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

print("=" * 60)
print("🤖 در حال راه‌اندازی ربات تلگرام...")
print("🔧 حالت: پروکسی خودکار برای ایران")
print("=" * 60)

async def create_bot_with_proxy():
    """ایجاد ربات با پشتیبانی از پروکسی"""
    
    # لیست پروکسی‌های آزمایشی (می‌تونی تغییر بدی)
    PROXIES = [
        "http://138.201.223.250:3128",  # پروکسی نمونه ۱
        "http://85.185.238.66:3128",    # پروکسی نمونه ۲
        None  # حالت بدون پروکسی
    ]
    
    for proxy in PROXIES:
        try:
            print(f"🔗 تست اتصال با پروکسی: {proxy or 'بدون پروکسی'}")
            
            # تنظیمات session با پروکسی
            session = None
            if proxy:
                session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
            
            # ایجاد ربات
            bot = Bot(
                token=BOT_TOKEN,
                session=session,
                default=DefaultBotProperties(
                    parse_mode=ParseMode.HTML,
                    link_preview_is_disabled=True
                )
            )
            
            # تست اتصال
            me = await bot.get_me()
            print("🎉 موفقیت! ربات متصل شد")
            print(f"   نام ربات: {me.first_name}")
            print(f"   یوزرنیم: @{me.username}")
            
            return bot
            
        except Exception as e:
            print(f"   ❌ خطا: {type(e).__name__}")
            continue
    
    print("❌ هیچ کدام از پروکسی‌ها کار نکرد!")
    return None

async def main():
    print("\n🔄 در حال اتصال به تلگرام...")
    
    # ایجاد ربات با پروکسی
    bot = await create_bot_with_proxy()
    
    if not bot:
        print("=" * 60)
        print("⚠️  راه حل‌های جایگزین:")
        print("1. از VPN یا فیلترشکن استفاده کن")
        print("2. پروکسی مناسب پیدا کن")
        print("3. روی هاست خارج از ایران اجرا کن")
        print("=" * 60)
        return
    
    # ایجاد دیسپچر
    dp = Dispatcher()
    
    # ایمپورت هندلرها
    try:
        from handlers.start import router as start_router
        from handlers.download import router as download_router
        
        dp.include_router(start_router)
        dp.include_router(download_router)
        
    except ImportError as e:
        print(f"⚠️  هشدار: {e}")
        print("📁 در حال ساخت هندلرهای پیش‌فرض...")
        
        # هندلرهای اضطراری
        from aiogram import Router, types
        from aiogram.filters import Command
        
        emergency_router = Router()
        
        @emergency_router.message(Command("start"))
        async def emergency_start(message: types.Message):
            await message.answer("✅ ربات فعال است! اما برخی ماژول‌ها بارگذاری نشدند.")
        
        dp.include_router(emergency_router)
    
    print("\n" + "=" * 60)
    print("✅ ربات آماده است!")
    print("📱 به تلگرام برو و ربات را تست کن")
    print("🔗 آدرس ربات: https://t.me/8595890168_bot")
    print("=" * 60)
    
    # شروع ربات
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 ربات خاموش شد!")
    except Exception as e:
        print(f"\n❌ خطای غیرمنتظره: {e}")