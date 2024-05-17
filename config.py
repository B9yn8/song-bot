import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "21552111"))
    API_HASH = os.environ.get("API_HASH", "0d0c89e2a25afdb2af119339e434662d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7006568131:AAE0WYdZjWIGCKF2p5lTDTm9vEjj9S4Educ")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "shamilhabeeb") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
