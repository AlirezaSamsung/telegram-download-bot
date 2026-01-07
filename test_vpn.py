import asyncio
import aiohttp
import ssl

async def test_connection():
    """تست اتصال با تنظیمات SSL مختلف"""
    
    print("🔧 تست اتصال با VPN...")
    
    # ایجاد SSL context بدون احراز هویت
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    connector = aiohttp.TCPConnector(
        ssl=ssl_context,
        force_close=True,
        enable_cleanup_closed=True
    )
    
    async with aiohttp.ClientSession(connector=connector) as session:
        # تست اتصال به سایت‌های مختلف
        test_urls = [
            ("تلگرام", "https://api.telegram.org"),
            ("گوگل", "https://google.com"),
            ("تلگرام ربات", f"https://api.telegram.org/bot8595890168:AAHEnSo-5JgUwRsvYGmn-6dKWhD_M-0BygY/getMe")
        ]
        
        for name, url in test_urls:
            try:
                print(f"\n📡 تست {name}: {url}")
                async with session.get(url, timeout=10) as resp:
                    print(f"   ✅ وصل شد! کد: {resp.status}")
                    if "telegram" in url and resp.status == 200:
                        text = await resp.text()
                        if "ok" in text.lower():
                            print("   🎉 تلگرام در دسترس است!")
            except Exception as e:
                print(f"   ❌ خطا: {type(e).__name__}")

if __name__ == "__main__":
    print("="*60)
    print("🛜 تست کننده VPN و اتصال")
    print("⚠️  مطمئن شو VPN روشن است!")
    print("="*60)
    
    input("\n🔘 Enter را بزن وقتی VPN روشن شد...")
    
    asyncio.run(test_connection())
    
    print("\n" + "="*60)
    print("نتیجه تست را بگو:")
    print("1. همه چیز ✅")
    print("2. فقط گوگل ✅")
    print("3. هیچکدام ❌")
    print("="*60)