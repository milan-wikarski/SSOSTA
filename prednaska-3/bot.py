from json import loads
from requests import get, post
from telegram.ext import Updater, CommandHandler

token = "1038936268:AAGk-ETpJ6o1bM2wA0j6CyI3Wl0xTLVZAaw"

updater = Updater(token=token)
dispatcher = updater.dispatcher

def command_start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Nie som bot, som vtákopysk"
    )

dispatcher.add_handler(
    CommandHandler(
        "start",
        command_start
    )
)

def command_gif(update, context):
    keywords = " ".join(context.args)

    url = "https://api.giphy.com/v1/gifs/random?api_key=iSN2eOFuUuoME2xyrnEJtQSxybCyw1Xt&rating=PG-13&tag=" + keywords

    response = loads(post(url).text)
    image = response["data"]["images"]["originl"]["mp4"]

    context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=image
    )


dispatcher.add_handler(
    CommandHandler(
        "gif",
        command_gif
    )
)

updater.start_polling()
print("Bot is running...")