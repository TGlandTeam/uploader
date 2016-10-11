# Uploader Bot By @EleGanceTM

# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import redis as r
import json
import logging
import urllib
import urllib2
import time
import logging
import subprocess
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)
token = "TOKEN"
-- YOUR TOKEB HERE :[
bot = telebot.TeleBot(token)
opizo_email = 'mrx2121mrx@gmail.com'
start_msg = '*Hello :D*'

# Uploader Bot By @MosyDev

@bot.message_handler(commands=['start'])
def m(m):
         name = m.from_user.first_name
         id = m.from_user.id
         redis.sadd('memebers',id)
         print 'User: {} Start the bot!'.format(m.from_user.id)
         bot.send_message(m.chat.id,start_msg,parse_mode='Markdown')

# Uploader Bot By @EleGanceTM

@bot.message_handler(commands=['stats'])
def m(m):
        if m.from_user.id == 0 or m.from_user.id == 100096055:
          file = redis.scard('files')
          msm = redis.scard('memebers')
          em = redis.scard('msgs')
          bot.send_message(m.chat.id,'*Files Uploaded:* _{}_\n*Users:* _{}_\n*All Messages:* _{}_'.format(file,msm,em),parse_mode='Markdown')

# Uploader Bot By @EleGanceTM

@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice'])
def all(m):
  try:
            if m.photo :
                fileid = m.photo[1].file_id
            elif m.video :
                fileid = m.video.file_id
            elif m.sticker :
                fileid = m.sticker.file_id
            elif m.document :
                fileid = m.document.file_id
            elif m.audio :
                fileid = m.audio.file_id
            elif m.voice :
                fileid = m.voice.file_id
            e = m.from_user.username
            text = m
            redis.sadd('files',fileid)
            link = urllib2.Request("https://api.pwrtelegram.xyz/bot{}/getFile?file_id={}".format(token,fileid))
            open = urllib2.build_opener()
            f = open.open(link)
            link1 = f.read()
            jdat = json.loads(link1)
            patch = jdat['result']['file_path']
            send = 'https://storage.pwrtelegram.xyz/{}'.format(patch)
            link = urllib2.Request("http://api.gpmod.ir/shorten/?url={}&username={}".format(opizo_email,send))
            opeen = urllib2.build_opener()
            j = opeen.open(link)
            lin1 = j.read()
            bot.send_message(m.chat.id,'در حال آپلود فایل....')
            bot.send_message(m.chat.id,'<b>تبریک فایل آپلود شد!</b>\n\n<b>لینک فایل شما:</b>\n{}\n\n<b>ساخته شده توسط:</b> \nMax Team | @MaxTeamCh'.format(lin1),parse_mode='HTML')
  except:
   bot.send_message(m.chat.id,link1)

# Uploader Bot By @EleGanceTM

@bot.message_handler(commands=['rate'])
def rate(m):
      markup = types.InlineKeyboardMarkup()
      rate = types.InlineKeyboardButton('Rate',url='https://telegram.me/EleGanceTM')
      markup.add(rate)
      bot.send_message(m.chat.id,'If you like me, please join to channel: @EleGanceTM\nYou can also recommend me to your friends.\nHave a nice day!',reply_markup=markup)

# Uploader Bot By @EleGanceTM
# Uploader Bot By @EleGanceTM
# Uploader Bot By @EleGanceTM

bot.polling(True)
