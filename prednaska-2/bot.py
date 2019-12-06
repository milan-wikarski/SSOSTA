import telegram.ext
import requests
import json

updater = telegram.ext.Updater(
    token="1038936268:AAGk-ETpJ6o1bM2wA0j6CyI3Wl0xTLVZAaw"
)

dispatcher = updater.dispatcher

def command_start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Nie som bot, som vtákopysk"
    )

dispatcher.add_handler(
    telegram.ext.CommandHandler(
        "start",
        command_start
    )
)

def command_gif(update, context):
    keywords = " ".join(context.args)

    url = "https://api.giphy.com/v1/gifs/random?api_key=iSN2eOFuUuoME2xyrnEJtQSxybCyw1Xt&rating=PG-13&tag=" + keywords

    response = str(requests.get(url).text)
    reponse_json = json.loads(response)

    image = reponse_json["data"]["images"]["original"]["mp4"]

    context.bot.send_document(
        chat_id=update.effective_chat.id
        document=image
    )


dispatcher.add_handler(
    telegram.ext.CommandHandler(
        "gif",
        command_gif
    )
)

updater.start_polling()
print("Bot is running...")