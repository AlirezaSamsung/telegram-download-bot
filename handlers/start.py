from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # ساخت کیبورد اینلاین
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📥 دانلود فایل", callback_data="download")],
        [InlineKeyboardButton(text="📁 دسته‌بندی‌ها", callback_data="categories")],
        [InlineKeyboardButton(text="⚙️ تنظیمات", callback_data="settings")]
    ])
    
    await message.answer(
        f"👋 سلام {message.from_user.first_name}!\n\n"
        "به **ربات دانلود پیشرفته** خوش آمدی! 🚀\n\n"
        "🔹 می‌توانی فایل دانلود کنی\n"
        "🔹 دسته‌بندی شخصی سازی کنی\n"
        "🔹 و سرعت بالایی تجربه کنی\n\n"
        "لطفا از منوی زیر انتخاب کن:",
        reply_markup=keyboard
    )