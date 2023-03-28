import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20482153"))
    API_HASH = os.environ.get("API_HASH", "e55cfcf3751a6543603b292b9cbd041e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6069064073:AAH6l2qMaiyJ1JKpVufHpv6TW9krSiGN2LE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHQBu1Gw5DYwcZKBc6s76j6Ch9HBXr_RFR-5pW3t_QZD7xidABal97LrZUpkEPprZFrEbd5tr-kaMqsKT10zZl_DxqA1O40egTtB-jO9KLpt7JDS0iyyJX-DebPfQSkHOMq9FYdVyCGa_YcUwgbkt7znbQWEqVgyjwk2A5hdwsMdDfoNHuuxu-140n1VEw3G0wJAORgCJ-cD5Ovy0faO0gsAuvmrYOD_zJCQZJG_dAs25LUpKevf9SnlTN-AFqEItk6NYQG05iMVnZg8eWPv-adqOLvjiIxDCV9I5xTQjLxFvSkgCtHwNjAKrFpTvrl9-bTLtd5vPnZ_y4gQSStqBsqwLGk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ayushkrh_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
