import re
from os import environ
from ast import literal_eval as eval
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 3020564
API_HASH = "91c026fadfdc442f504a0bd3e5c8cd18"
BOT_TOKEN = "1651274124:AAGSuYUJTzvmuNA42U8qNfutJUtBjquWd4U"

# Bot settings
CACHE_TIME = "300"
USE_CAPTION_FILTER = False        
PICS = [
  "https://telegra.ph/file/3002281196303098ed719.jpg",
  "https://telegra.ph/file/ba325e42787cc6cfb8f9c.jpg",
  "https://telegra.ph/file/d7483ff134a647606bdbd.jpg",
  "https://telegra.ph/file/fd34364fd60b16dba86e5.jpg",
  "https://telegra.ph/file/1eddd2e17d3c433329644.jpg",
  "https://telegra.ph/file/4d710f5ede210a8d33a9b.jpg",
  "https://telegra.ph/file/126c3d59725f22317b231.jpg",
  "https://telegra.ph/file/223f3f92abb1fa6e95c7d.jpg",
  "https://telegra.ph/file/18ada04c1a18f234fb946.jpg",
  "https://telegra.ph/file/c39c9017ce59d1d201b17.jpg",
  "https://telegra.ph/file/7dbb3f0cbd1491061b0a7.jpg",
  "https://telegra.ph/file/11d9370e562d72cbffc99.jpg",

# Admins, Channels & Users
ADMINS = [1103647866]
CHANNELS = [-1001500220248]
AUTH_USERS = [1560645285]
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb+srv://evamaria2:evamaria2@cluster0.tx3ho.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = "Telegram_files"

# Others
LOG_CHANNEL = -1001716242007
SUPPORT_CHAT = "MGMOVIEGRAM"
P_TTTI_SHOW_OFF = "True"
IMDB = "True"
SINGLE_BUTTON = bool((environ.get('SINGLE_BUTTON', False)))
CUSTOM_FILE_CAPTION = "`{file_name}`"
