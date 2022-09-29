import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16180057"))
API_HASH = getenv("API_HASH", "96fc6b582b78a28881c6e78d06f04c4a")

BOT_TOKEN = getenv("BOT_TOKEN", "5512778238:AAEB00SmA5K_ZL3NXLALEFr2EhsyVgjHKSA")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aero:BotzV1@cluster0.zhwf83q.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "720")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1440")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001627514871"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Aero ✘ Music Player~🇮🇳​")

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1484735126").split())
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AerodynamicV1Botz/AeroXMusic2.0",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/AerodynamicV1_Update")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/AerodynamicV1_Promotion")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f84d28d91512a445ecce1.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "7")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBFKqrBkhRHYlcaoh75kGtEhsq5lpw6mN26neu5indgwrhJXP7ds_Q-WnfRBavABhReS3G8FpDg7XrSVvvUF8u5l2zGisCWIoYeC6uvYCuC23QAlz39MI510mzHTd_VL_uX4cxmTAmbtQvzR3iCvj23mSx44Ebxrq4M9zL1CpZ7Rwupt5KDfXEw2MIVI1jWkM7j2mTSTUReJhRRRP3OH03APdnYgh-gMfqSYnBrny_G5aracBvdn2MQgOKYYZj0qnMZX-YxmEL1v8E8eQhGsbKT-WXUADieW3Y6U6eFo1aO1YUvd0qdnjwtVAZh3Iljn77n4hsAp94299m0k5D3RDadAAAAAVloDrAA")
STRING2 = getenv("STRING_SESSION2", "BQBZ0Urqc3Hn0-a05fOKk1JBygVAWIp6QPtTIemy0yyC0HOd9LKDalJ6wiTmUbN5cVYq2QO5PZAtvREGLeu6tFRT6Y6NNUVV60NlQAVSHrg3ZBqoLTXrGJqfXp2oLcVKh2gw1EQMELr4XEoVbYxnhz7Wr4yoMR7bZcFxNfZXvIm3WvBw4CLrnselyG3_emyqBJ5zAc0wdnfBF0SUYIzsmb4k6T2B0ZZLMbe3a0WLTQMO4k79dy9VBYLepuSoF6Y9xPSdCbNGZdoTPiUmoWZhjRRHQukwRoTiPDBh_lyziYgrDct5HSb0GFXv5Dsh6AwFW96kjFMVBwYhFcz6hXe8lvJfAAAAAVW7DsAA")
STRING3 = getenv("STRING_SESSION3", "BQCux_FV4XewqHCIw40uYbH1OqbjRuTxQzSPTeR0PfuM4E6grmP0aasUmZz92myF55GJWiToVZ3RtPQxgTP5uMseZgGS9R8MT-9lxwPQjitMjmONct_5YA0FUTEkGlrkQzV6fLASL4NWFK_Dwm6tmsHMPpPxZs0kBIHHsNgzEl8o9B23rNqxjZwyD0uKdjnpncwq8SYXfI1TJnxcX4ddPJMUYSfsqtKPEkadIpRn0j9Yjrt3A5cchO5mnpUtRKcVxzXT6gYTL_XA_2td_a-t2QK1Y1QEonkZDQxAEGwtecXojuTH6qah99ccahy6Ma2uEi5TMfoZDDy8SqL3p-T2vNLxAAAAAVloDrAA")
STRING4 = getenv("STRING_SESSION4", "BQAfE-ErHdAQ0_IFGczFm0hMcyslyulN42EKBFYoY6YBnFSqJa5-Yd13g2YG9OwMNd4ySpW-wfAekYFXNN0iZ-qzbVioZ6rBZOlzVRPn_XsoZeOmg2qG1w9vf0AkBJDZ61t_KeXUNZm_5Kmwg55nQQbQoSeQZNg-227R_D0MolXGGGQZZCOigHQuTof0W4YzuxkBSI22c63sZ8wHux-aZZFgDR8BPnb1965U8eiHKjXSBpMxAY52z1EgmK5OMCRbAPdmeEE1dGudgfgPI2fBKkmPgoB24se-PQlS7NBa8LYxwTSTA2MLjw7SgNU-iSf-CjG_nPLOZdsSVY6Dw1YC7N30AAAAAUP-g74A")
STRING5 = getenv("STRING_SESSION5", "BQAVPcCE1_YZEm9UK1Ag3sKJ-OVKIzjpj5ki4P2vAZjz7_etATfwTw_vVsyxdBb0P0ld-E_CMjEG5ZKwc5e0jGTIv04Qfmx3xPXP3AYkBAQkmSo7T62HGd49YvX44yjVenT5CyXA9oXeoNgtECmZl8_r2R_uRX4qCHEHzVkuvTCkKFDHLW9DqCuY24flTYjOOFujGiurjKuNB1BdRr0_IGI3Hk_tWGn1PpnyksKEvtzF8S9Abia7ctlBafb3CuSuSFv_cxsX3luktD3PqtmPiScptL0AMPPrEvSgimSoY06B1x83u4Tbmc2J_DEp8QDotRV9rQu6Ha6xsVzsmY4X2Z0ZAAAAATWdCQkA")

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "anonxlogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph//file/c6d7af5a8dc30ea72764f.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph//file/c6d7af5a8dc30ea72764f.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
