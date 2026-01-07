import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import aiohttp
import ssl

# غیرفعال کردن لاگ‌های اضافی
logging.getLogger('aiohttp').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)

print("="*60)
print("🚨 ربات اضطراری - حالت ایران")
print("🔧 با تنظیمات خاص برای VPN")
print("="*60)

# توکن شما
TOKEN = "8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY"

async def create_bot():
    """ایجاد ربات با تنظیمات ویژه"""
    
    # ۱. ابتدا VPN را تست می‌کنیم
    print("\n🔍 در حال تست VPN...")
    
    try:
        # تست ساده اینترنت
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        connector = aiohttp.TCPConnector(ssl=ssl_context)
        
        async with aiohttp.ClientSession(connector=connector) as session:
            # تست به گوگل
            async with session.get("https://google.com", timeout=5) as resp:
                if resp.status == 200:
                    print("✅ VPN فعال است")
                else:
                    print("⚠️  VPN ممکن است مشکل داشته باشد")
                    
    except Exception as e:
        print(f"❌ مشکل VPN: {type(e).__name__}")
        print("\n💡 لطفا:")
        print("1. VPN را خاموش/روشن کن")
        print("2. سرور VPN را عوض کن")
        print("3. از VPN دیگری استفاده کن")
        return None
    
    # ۲. حالا ربات را می‌سازیم
    print("🤖 در حال ساخت ربات...")
    
    try:
        # ساخت session ویژه
        session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                ssl=False,  # غیرفعال کردن SSL موقتاً
                force_close=True
            )
        )
        
        # ساخت ربات
        bot = Bot(token=TOKEN, session=session)
        
        # تست اتصال
        me = await bot.get_me(timeout=30)
        print(f"🎉 موفقیت! ربات: @{me.username}")
        
        return bot
        
    except Exception as e:
        print(f"❌ خطا در ساخت ربات: {e}")
        return None

async def main():
    """تابع اصلی"""
    
    # ساخت ربات
    bot = await create_bot()
    
    if not bot:
        print("\n" + "="*60)
        print("🚫 نتوانستم ربات را بسازم!")
        print("\n🎯 راه‌حل‌های پیشنهادی:")
        print("1. **VPN را قطع و وصل کن**")
        print("2. **سرور VPN را به کشور دیگری تغییر بده** (ترکیه، آلمان، آمریکا)")
        print("3. **از VPN معتبرتر استفاده کن**")
        print("4. **مقداری صبر کن** (گاهی سرور VPN شلوغ است)")
        print("="*60)
        
        # درخواست تلاش مجدد
        retry = input("\n🔄 آیا می‌خواهی دوباره امتحان کنی؟ (y/n): ")
        if retry.lower() == 'y':
            print("\n" + "="*60)
            print("🔄 تلاش مجدد...")
            print("⏳ لطفا 10 ثانیه صبر کن سپس Enter بزن")
            input()
            await main()
        return
    
    # ساخت دیسپچر
    dp = Dispatcher()
    
    # دستور /start
    @dp.message(Command("start"))
    async def start_cmd(message: types.Message):
        await message.answer(
            "🎊 **تبریک! ربات فعال شد!**\n\n"
            "✅ اتصال VPN موفقیت‌آمیز بود\n"
            "🤖 حالا می‌توانی از ربات استفاده کنی\n\n"
            "برای ادامه `/help` را بفرست",
            parse_mode="Markdown"
        )
    
    # دستور /help
    @dp.message(Command("help"))
    async def help_cmd(message: types.Message):
        await message.answer(
            "📚 **دستورات:**\n\n"
            "/start - شروع ربات\n"
            "/download - دانلود فایل\n"
            "/settings - تنظیمات\n"
            "/help - این راهنما\n\n"
            "🔗 می‌توانی لینک هم مستقیم بفرستی!",
            parse_mode="Markdown"
        )
    
    # هندلر دانلود
    @dp.message(Command("download"))
    async def download_cmd(message: types.Message):
        await message.answer(
            "📥 **سیستم دانلود**\n\n"
            "لطفا لینک را بفرست:\n"
            "- 🎥 ویدیو (یوتیوب، اینستاگرام)\n"
            "- 🎵 صوت\n"
            "- 📷 عکس\n"
            "- 📄 فایل\n\n"
            "⚡ به زودی کامل می‌شود!",
            parse_mode="Markdown"
        )
    
    # هندلر پیام‌های متنی
    @dp.message()
    async def handle_text(message: types.Message):
        text = message.text or ""
        
        if text.startswith("http"):
            await message.answer(
                f"🔗 **لینک دریافت شد!**\n\n"
                f"`{text[:50]}...`\n\n"
                "⏳ سیستم دانلود به زودی اضافه می‌شود...",
                parse_mode="Markdown"
            )
        elif not text.startswith("/"):
            await message.answer(
                "🤖 **ربات دانلود تلگرام**\n\n"
                "برای شروع /start را بزن\n"
                "برای راهنما /help را بفرست\n\n"
                "🔥 **ویژگی‌ها:**\n"
                "• دانلود از لینک\n"
                "• دسته‌بندی\n"
                "• شخصی‌سازی\n"
                "• سرعت بالا",
                parse_mode="Markdown"
            )
    
    print("\n" + "="*60)
    print("✅ **ربات آماده است!**")
    print("📱 به تلگرام برو و:")
    print("1. @8595890168_bot را سرچ کن")
    print("2. Start بزن")
    print("3. /help را تست کن")
    print("="*60 + "\n")
    
    # شروع ربات
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ خطا در حین اجرا: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    print("⚠️  لطفا قبل از ادامه:")
    print("1. VPN خود را روشن کن")
    print("2. مطمئن شو اینترنت وصل است")
    print("3. اگر VPN وصل نیست، سرور آن را عوض کن")
    
    input("\n🔘 وقتی آماده بودی Enter بزن...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 ربات خاموش شد!")