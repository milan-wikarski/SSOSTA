import telegram.ext
import requests
import json

updater = telegram.ext.Updater(
    token="1007784086:AAE4MYenUlA6VVS06ew_y0WiU7RI3wmdgUA",
    use_context=True
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

def command_gifs(update, context):
    keywords = " ".join(context.args)

    url = "https://api.giphy.com/v1/gifs/random?api_key=iSN2eOFuUuoME2xyrnEJtQSxybCyw1Xt&rating=PG-13&tag=" + keywords

    response = str(requests.get(url).text)
    response_json = json.loads(response)

    image = response_json["data"]["images"]["original"]["mp4s"]

    context.box.send_document(
        chat_id=update.effective_chat.id,
        document=image
    )
    

dispatcher.add_handler(
    telegram.ext.CommandHandler(
        "gif",
        command_gifs
    )
)

updater.start_polling()
print("Bot is running")