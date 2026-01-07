from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("download"))
async def cmd_download(message: types.Message):
    await message.answer(
        "🔗 **لطفا لینک مورد نظر را ارسال کن:**\n\n"
        "مثال:\n"
        "• https://example.com/file.zip\n"
        "• https://youtube.com/watch?v=...\n\n"
        "📦 فرمت‌های پشتیبانی شده:\n"
        "ویدیو، صدا، عکس، فایل‌های فشرده"
    )