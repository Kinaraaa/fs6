# (©)Codexbotz
# Recode by @Daijobu69
# t.me/GojoProjct & t.me/GojoSupport

import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5655866333:AAGnIVgVGJo1ua2u5jocJlwUbh9V8kUD9S0")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22464238"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "4071eeea5526605614307610653622d1")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001214093784"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5356286861"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "AbbyCute")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://ngmftwpb:ozc2sRfCq6UWCFRBzjF_3nol1APMUWQy@mouse.db.elephantsql.com/ngmftwpb")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "AsupanSHID")
GROUP = os.environ.get("GROUP", "Squadhomexxx")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001527016233"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001615837947"))
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001658671781"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001619188473"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1001676165015"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "-1001786381934"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Jangan Lupa Join Terlebih Dahulu.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5356286861 1834738583 1474472980").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hallo {first}\n\nSelamat datang dan jangan lupa join\n\nSilakan Join Terlebih Dahulu.. Kalau Sudah Silahkan Menikmati</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1972848319)


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
