import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6163690266:AAEdE1_HAMblf_-YVtiudSjv3esGtqQFPKI)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQClJQxZPFNkAB6byhvKH74vpUeBNnPIg5Yb6LG0wA79dplBt5sHRy03bg_c9aXGSc50fb-8gG2p9JiKjBXehJVIEp294KCQqv2UbJ6gdZJw0vBJbl9GAP_fbzSTRgSkj8iPmseW6N5-kdRTBLT8Vp6ILP92qWxvezrj722MdhAarGeQJ2oEOxFsOGf2PRnuUwyH3y9TzZGzdLq64ubzBy2JToonmGfe2R2RH273PZERFdi37klhPPttAh5R9lZYPjpd9PUFlYulNV2kxcgrHjitU2kKPkQnl-MT_olmMBps1lKBRt6Rh3ZxEg0eT5sTHW2ggaZqrkGPE_DJumgdErHRAAAAAWQZt3EA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
