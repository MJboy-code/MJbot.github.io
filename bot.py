from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# توکن ربات رو اینجا وارد کن
BOT_TOKEN = 'توکن_اینجا_قرار_بگیره'

# اطلاعات ایمیل و رمز عبور (ثابت برای همه کاربران)
EMAIL = "example@email.com"
PASSWORD = "example_password"

# وقتی کاربر /start رو بزنه
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    welcome_text = f"سلام {user.first_name} عزیز! 🌟\nخوش اومدی! لطفاً روی دکمه زیر کلیک کن تا ایمیل و رمز برات ارسال بشه."
    
    keyboard = [[InlineKeyboardButton("📩 دریافت ایمیل و رمز", callback_data="get_email_password")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

# وقتی کاربر روی دکمه کلیک کنه
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    # ارسال ایمیل و رمز عبور
    message = f"""
📧 **ایمیل:** {EMAIL}
🔑 **رمز عبور:** {PASSWORD}

از این اطلاعات استفاده کن! اگه مشکلی داشتی به ادمین پیام بده. 😊
    """
    query.edit_message_text(message)

# راه‌اندازی ربات
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
