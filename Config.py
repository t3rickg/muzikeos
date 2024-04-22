import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "27677843"))
    API_HASH = os.environ.get("API_HASH", "2ed5725ee29efa61502372883a3c903b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6572679323:AAFRnbfYR0xd20niYinzOprGWEfgO90-Ips)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sabrina_brand_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")https://t.me/smartboy13457
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")https://t.me/smartboy13457
    START_IMG = os.environ.get("START_IMG", "https://graph.org/file/ab011f73d5dbfd9a6003d.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://graph.org/file/ab011f73d5dbfd9a6003d.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6744346714")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', 6744346714) # Change it to "True"
