from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
)

async def start(update: Update, context: CallbackContext):
    keyboard = [["💰 رصيد"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("مرحبًا! البوت يعمل الآن 🎉", reply_markup=reply_markup)

async def show_balance(update: Update, context: CallbackContext):
    await update.message.reply_text("رصيدك الحالي: 100.00$")

TOKEN = "AAGSvR8NVeahQX3yTFpLA3lVYRqQO5lvO2M"
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex("^💰 رصيد$"), show_balance))

app.run_polling()
