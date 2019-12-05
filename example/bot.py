from json import loads
from requests import get
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = "917535748:AAHFvMiIumHnLLoxUkKEYPcPVod_-XbbzV4"


# Logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# Setup
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


# Commands
def command_start(update, context):
  print("TEST")
  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Nie som bot, som vtákopysk!")

dispatcher.add_handler(CommandHandler("start", command_start))


def command_help(update, context):
  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Dokážem nájsť text piesne pomocou príkazu /lyrics")

dispatcher.add_handler(CommandHandler("help", command_help))


def command_upper(update, context):
  text = " ".join(context.args).upper()

  context.bot.send_message(
      chat_id=update.effective_chat.id, text=text)

dispatcher.add_handler(CommandHandler("caps", command_upper))


def command_lyrics(update, context):
  url = "https://some-random-api.ml/lyrics?title="
  title = " ".join(context.args)

  context.bot.send_message(
      chat_id=update.effective_chat.id, text="Fetching lyrics for " + title)

  response_txt = str(get(url + title).text)
  response_json = loads(response_txt)

  lyrics = response_json["lyrics"]

  if ("lyrics" in lyrics):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=lyrics)
  else:
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I was not able to find lyrics for " + title)

dispatcher.add_handler(CommandHandler("lyrics", command_lyrics))


# Start
updater.start_polling()
print("Bot is running...")
