import random
import string
import time
from telegram import Bot, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.updater import Updater

updater = Updater("#your token", use_context=True)
dispatcher = updater.dispatcher


foo = [
   "514adm2s0c@wwjmp.com",
   "9q6fv8wkwr4@wwjmp.com",
   "xi9pw5ry@1secmail.com",
   "xpni3u25w@1secmail.net",
   "pkbds55jep@1secmail.com",
   "jeil65xzv8@1secmail.org",
   "cg89o9i0thml@1secmail.net",
   "0tw2rcoc3id@1secmail.org",
   "szsjhdc@gmail.com",
   "sfsdsdfdxf@wwjmp.com",
   "5dsfdfc@wwjmp.com",
   "sdfdxdd@wwjmp.com",
   "xdfzfvdfd@1secmail.com",
   "xpndfvdx@1secmail.net",
   "pkbddxcxd@1secmail.com",
   "zfcvcvxc8@1secmail.org",
   "dcxdvcx@1secmail.net",
   "cvxzv@1secmail.org",
   "zcvzxv@1secmail.org",
   "dsfszc@wwjmp.com",
   "zcczc@wwjmp.com",
   "zvcz4@wwjmp.com",
   "zxxxzz@1secmail.com",
   "zxzxcxcv@1secmail.net",
   "vbvxvxv@1secmail.com",
   "rrtrere@1secmail.org",
   "moujhj@1secmail.net",
   "dfxdfvg@1secmail.org",
   "dfdvdv@1secmail.org",
   "ddfvvcvcv@wwjmp.com"
]


def start(update, context):
    kbd_lst = [["🗑 Random Email"], ["📁Developer", "💡More"]]
    kbd = ReplyKeyboardMarkup(kbd_lst, row_width=3,resize_keyboard=True)

    update.message.reply_text(text="🚧 Yo Brudda This Bot Was Made By => @levi_dev", reply_markup=kbd)

def ranemail(update, context):
    update.message.reply_text(text= "🧩 Random Email =>\n" + random.choice(foo))    

def more(update, context):
    update.message.reply_text(text="💡For Updates => @levilibrary")

def developer(update, context):
    update.message.reply_text(text="🧩Developer => @levi_dev")    

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text("🗑 Random Email"), ranemail))
dispatcher.add_handler(MessageHandler(Filters.text("📁Developer"), developer))
dispatcher.add_handler(MessageHandler(Filters.text("💡More"), more))

updater.start_polling()
print("Running")
