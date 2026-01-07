import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import aiohttp
import ssl

# تنظیمات لاگ ساده
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

print("="*60)
print("🤖 ربات دانلود تلگرام - نسخه تصحیح شده")
print("🛜 برای ایران با VPN")
print("="*60)

# توکن شما
TOKEN = "8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY"

async def check_vpn():
    """بررسی VPN"""
    print("\n🔍 بررسی اتصال...")
    
    try:
        # ساخت SSL context
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        connector = aiohttp.TCPConnector(ssl=ssl_context)
        
        async with aiohttp.ClientSession(connector=connector) as session:
            # تست گوگل
            async with session.get("https://google.com", timeout=5) as resp:
                if resp.status == 200:
                    print("✅ اینترنت و VPN فعال است")
                    return True
                else:
                    print("⚠️  VPN ممکن است مشکل داشته باشد")
                    return False
                    
    except Exception as e:
        print(f"❌ خطا در اتصال: {type(e).__name__}")
        return False

async def create_bot_session():
    """ایجاد session برای ربات"""
    print("🔧 در حال ساخت ربات...")
    
    try:
        # ساخت session ویژه
        connector = aiohttp.TCPConnector(ssl=False)
        session = aiohttp.ClientSession(connector=connector)
        
        # ساخت ربات
        bot = Bot(token=TOKEN, session=session)
        
        # تست اتصال (بدون پارامتر timeout)
        me = await bot.get_me()  # خطا اصلاح شد
        print(f"🎉 اتصال موفق! ربات: @{me.username}")
        
        return bot
        
    except Exception as e:
        print(f"❌ خطا در ساخت ربات: {e}")
        return None

async def setup_bot():
    """تنظیمات ربات"""
    bot = await create_bot_session()
    
    if not bot:
        print("\n" + "="*60)
        print("⚠️  نتوانستم به تلگرام وصل شوم!")
        print("\n🔧 **اقدامات فوری:**")
        print("1. VPN را خاموش/روشن کن")
        print("2. سرور VPN را عوض کن (ترکیه پیشنهاد می‌شود)")
        print("3. 30 ثانیه صبر کن")
        print("4. دوباره امتحان کن")
        print("="*60)
        
        retry = input("\n🔄 دوباره امتحان کنم؟ (y/n): ")
        if retry.lower() == 'y':
            print("\n🔄 تلاش مجدد...")
            await setup_bot()
        return None
    
    return bot

# ساخت دیسپچر
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    """دستور start"""
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="📥 دانلود فایل", callback_data="download")],
        [types.InlineKeyboardButton(text="📁 دسته‌بندی‌ها", callback_data="categories")],
        [types.InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="settings")],
        [types.InlineKeyboardButton(text="📊 راهنما", callback_data="help")]
    ])
    
    await message.answer(
        f"✨ **سلام {message.from_user.first_name}!**\n\n"
        "🚀 **به ربات دانلود پیشرفته خوش آمدید!**\n\n"
        "🔸 **قابلیت‌های اصلی:**\n"
        "• دانلود از ۱۰۰+ سایت\n"
        "• تبدیل فرمت خودکار\n"
        "• دسته‌بندی هوشمند\n"
        "• سرعت دانلود بالا\n\n"
        "🔸 **نحوه استفاده:**\n"
        "لینک مورد نظر را بفرستید\n\n"
        "**از منوی زیر انتخاب کنید:**",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    """دستور help"""
    await message.answer(
        "📚 **راهنمای استفاده:**\n\n"
        "🔹 **برای دانلود:**\n"
        "1. لینک را کپی کنید\n"
        "2. برای ربات بفرستید\n"
        "3. کیفیت را انتخاب کنید\n"
        "4. دانلود شروع می‌شود\n\n"
        "🔹 **سایت‌های پشتیبانی شده:**\n"
        "• YouTube\n• Instagram\n• Twitter\n• TikTok\n"
        "• و بسیاری سایت‌های دیگر\n\n"
        "🔹 **دستورات:**\n"
        "/start - شروع ربات\n"
        "/download - دانلود فایل\n"
        "/settings - تنظیمات\n"
        "/help - این راهنما\n\n"
        "❓ **سوال دارید؟**\n"
        "از قسمت پشتیبانی کمک بگیرید",
        parse_mode="Markdown"
    )

@dp.message(Command("download"))
async def download_command(message: types.Message):
    """دستور download"""
    await message.answer(
        "📥 **سیستم دانلود**\n\n"
        "🔗 **لطفا لینک را ارسال کنید:**\n\n"
        "🎬 **ویدیو:**\n"
        "https://youtube.com/...\n"
        "https://instagram.com/...\n\n"
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
    """مدیریت دکمه‌ها"""
    if callback.data == "download":
        await callback.message.answer(
            "🔗 **لطفا لینک را بفرست:**\n\n"
            "مثال:\n"
            "• https://youtu.be/xxxxx\n"
            "• https://www.instagram.com/p/xxxxx\n"
            "• https://twitter.com/xxxxx\n\n"
            "⚡ سیستم به صورت خودکار نوع فایل را تشخیص می‌دهد!",
            parse_mode="Markdown"
        )
    
    elif callback.data == "categories":
        await callback.message.answer(
            "📁 **دسته‌بندی‌ها:**\n\n"
            "1. **ویدیو**\n"
            "   - آموزشی\n"
            "   - سرگرمی\n"
            "   - موزیک ویدیو\n\n"
            "2. **صوت**\n"
            "   - پادکست\n"
            "   - آهنگ\n"
            "   - کتاب صوتی\n\n"
            "3. **عکس**\n"
            "   - والپیپر\n"
            "   - اینفوگرافیک\n"
            "   - ممز\n\n"
            "4. **اسناد**\n"
            "   - PDF\n"
            "   - Word\n"
            "   - PowerPoint\n\n"
            "✨ **ویژگی:**\n"
            "می‌توانی دسته‌های شخصی بسازی!",
            parse_mode="Markdown"
        )
    
    elif callback.data == "settings":
        await callback.message.answer(
            "⚙️ **تنظیمات شخصی سازی:**\n\n"
            "🔸 **کیفیت پیش‌فرض:**\n"
            "• بالا (1080p)\n"
            "• متوسط (720p)\n"
            "• پایین (480p)\n\n"
            "🔸 **محل ذخیره‌سازی:**\n"
            "• تلگرام\n"
            "• گالری\n"
            "• فایل‌های دانلودی\n\n"
            "🔸 **زبان:**\n"
            "• فارسی\n"
            "• انگلیسی\n\n"
            "🔸 **سایر تنظیمات:**\n"
            "• اعلان‌ها\n"
            "• تم ربات\n"
            "• سرعت دانلود\n\n"
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
            "🔹 **چطور کیفیت را عوض کنم؟**\n"
            "بعد از ارسال لینک، گزینه‌ها نمایش داده می‌شود\n\n"
            "📞 **پشتیبانی:**\n"
            "اگر مشکل دارید، پیام بفرستید",
            parse_mode="Markdown"
        )
    
    await callback.answer()

async def main():
    """تابع اصلی"""
    print("\n⚠️  لطفا:")
    print("1. VPN را روشن کن")
    print("2. اگر VPN کار نکرد، سرور را عوض کن")
    print("3. معمولاً سرورهای ترکیه بهتر کار می‌کنند")
    
    input("\n🔘 وقتی آماده بودی Enter بزن...")
    
    # بررسی VPN
    vpn_ok = await check_vpn()
    if not vpn_ok:
        print("\n❌ VPN مشکل دارد!")
        print("لطفا VPN را تنظیم کن دوباره امتحان کن")
        return
    
    # ساخت ربات
    bot = await setup_bot()
    if not bot:
        return
    
    print("\n" + "="*60)
    print("✅ **ربات آماده است!**")
    print("📱 **مراحل تست:**")
    print("1. تلگرام را باز کن")
    print("2. این آدرس را سرچ کن: @8595890168_bot")
    print("3. روی Start کلیک کن")
    print("4. از منو استفاده کن")
    print("="*60 + "\n")
    
    # شروع ربات
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("\n👋 ربات خاموش شد!")
    except Exception as e:
        print(f"\n❌ خطا: {e}")
    finally:
        if bot:
            await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())