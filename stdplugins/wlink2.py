""" Top Secret Scraper """

import os

import shutil

from bs4 import BeautifulSoup

import re

from time import sleep

from html import unescape

from re import findall

from datetime import datetime

from selenium import webdriver

from urllib.parse import quote_plus

from urllib.error import HTTPError

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options

from wikipedia import summary

from wikipedia.exceptions import DisambiguationError, PageError

from urbandict import define

from requests import get

from google_images_download import google_images_download

from googleapiclient.discovery import build

from googleapiclient.errors import HttpError

from googletrans import LANGUAGES, Translator

from gtts import gTTS

from emoji import get_emoji_regexp

from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN

from userbot.utils import register

from userbot.utils import admin_cmd

import pybase64

@borg.on(admin_cmd("ghar (.*)"))
async def _(event):
    name="apple"
    input_str = event.pattern_match.group(1)
    if input_str:
        name = input_str
    else:
        await event.edit("Enter a username you noob!")
        return
    await event.edit(f"`Preparing to fuck your ass.... Get ready to be surprised...\n25% done...\nPuk You`")
    URL=f"http://vogue-conventions.000webhostapp.com/dh3r4zphp3.php?user={name}"
    page_src = get(URL)
    soup = BeautifulSoup(page_src.text,"html.parser")
    data = soup.find_all('img')[7].get("src")
    data=data[21:]
    await event.edit(f"`50% done...`")
    imgdata = pybase64.b64decode(data)
    file = 'scifidemon.gif'
    with open ("./scifidemon.gif", 'wb') as f:
        f.write(imgdata)
    await event.edit(f"`75% done...`")
    await event.client.send_file(

         event.chat_id,

         file,

         caption="`You Surprised Gey?`",

         force_document=True,

         reply_to=event.message.reply_to_msg_id,

         )

    os.remove('./scifidemon.gif')
    await event.delete()
