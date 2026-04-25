import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8601754547:AAEZF3PuXvz3-7io_mSLwfBq-cm6tbmc7MA"
def загрузить_текст(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()

jokes = загрузить_текст("jokes.txt")
anekdots = загрузить_текст("anekdots.txt")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["Шутка🤪", "Анекдот💫"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет, я бот, который постарается зарядить тебя хорошим настроением!Выбери категорию ниже⬇️ )",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Шутка🤪":
        joke = random.choice(jokes)
        await update.message.reply_text(joke)

    elif text == "Анекдот💫":
        anekdot = random.choice(anekdots)
        await update.message.reply_text(anekdot)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
