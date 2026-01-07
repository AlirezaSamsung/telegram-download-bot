from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    """منوی اصلی ربات"""
    buttons = [
        [InlineKeyboardButton(text="📥 دانلود فایل", callback_data="menu_download")],
        [InlineKeyboardButton(text="📁 دسته‌بندی من", callback_data="menu_categories")],
        [InlineKeyboardButton(text="⚡ دانلود‌های اخیر", callback_data="menu_recent")],
        [
            InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="menu_settings"),
            InlineKeyboardButton(text="📊 راهنما", callback_data="menu_help")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def download_options():
    """گزینه‌های دانلود"""
    buttons = [
        [InlineKeyboardButton(text="🎥 ویدیو", callback_data="dl_video")],
        [InlineKeyboardButton(text="🎵 صوت", callback_data="dl_audio")],
        [InlineKeyboardButton(text="🖼️ عکس", callback_data="dl_image")],
        [InlineKeyboardButton(text="📄 فایل", callback_data="dl_file")],
        [InlineKeyboardButton(text="🔙 بازگشت", callback_data="menu_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)