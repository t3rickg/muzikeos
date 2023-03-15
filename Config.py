import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("5735838722:AAEjzDUYURrQ2hhESY6CYAgMN9Bnz8Mr-DY", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOH8BuzigIvgBXWvcGWTv4F5l3lSNhmnsqtv3m1LqfG0CxxfiXziFaxbwKHHMKknKGEO5-kI8sjRRL6l87NyPQarCi9s9mP_rKog07LWG_jGHUwyoYdJcSSsm_4B0Q7ZBz9Z7GRgczMyv6eeVAv3HZIsbudkBF_e_Qdmiwo5Cf9nNkaizQnvnG97632z82aRNX6A27qzcsEElVPUkfwZe1cGRzTo_b9Ph2iuJIgAo5AAysiogpJ8zYzqoXILkg_Y-lGT1uBIBqc7OkRaGIDfoduMe_KYq4dfd_S2Y1YWR0NHskpvLYVWdc0j7-PZalroylAcssSu84KOsoSGG33iYk95p7Us=)
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
