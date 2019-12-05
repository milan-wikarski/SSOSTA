from json import loads
from requests import get, post
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = "917535748:AAHFvMiIumHnLLoxUkKEYPcPVod_-XbbzV4"


# Logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# Setup
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


# Command /start
def command_start(update, context):
  print("TEST")
  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Nie som bot, som vtákopysk!")

dispatcher.add_handler(CommandHandler("start", command_start))


# Command /help
def command_help(update, context):
  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Dokážem nájsť text piesne pomocou príkazu /lyrics")

dispatcher.add_handler(CommandHandler("help", command_help))


# Command /caps
def command_caps(update, context):
  text = " ".join(context.args).upper()

  context.bot.send_message(
      chat_id=update.effective_chat.id, text=text)

dispatcher.add_handler(CommandHandler("caps", command_caps))


# Command /lyrics
def command_lyrics(update, context):
  url = "https://some-random-api.ml/lyrics?title="
  title = " ".join(context.args)

  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Fetching lyrics for " + title)

  response_txt = str(get(url + title).text)
  response_json = loads(response_txt)

  if ("lyrics" in response_json):
    lyrics = response_json["lyrics"]

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=lyrics)
  else:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I was not able to find lyrics for " + title)

dispatcher.add_handler(CommandHandler("lyrics", command_lyrics))


def command_gif(update, context):
  tag = "cat"

  if (len(context.args) >= 1):
    tag = context.args[0]

  url = "https://api.giphy.com/v1/gifs/random?api_key=iSN2eOFuUuoME2xyrnEJtQSxybCyw1Xt&rating=PG-13&tag="

  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Loading random GIF of " + tag)

  response_txt = str(get(url + tag).text)
  response_json = loads(response_txt)

  image = response_json["data"]["images"]["original"]["mp4"]

  print(image)

  context.bot.send_document(
      chat_id=update.effective_chat.id, document=image)

dispatcher.add_handler(CommandHandler("gif", command_gif))


# Start the bot
updater.start_polling()
print("Bot is running...")
