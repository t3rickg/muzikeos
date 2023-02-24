import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21242860"))
    API_HASH = os.environ.get("API_HASH", "b1deaa84daa9d9f2b65725c21735e6c1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5983924624:AAGhcQjFKxUGtNEp8KNW_uXVJMeL8DaJIe8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJYBuw7jYufog2oXPK8B0A91xKxR-dqULn6uzeP_oofwsT9b-zaUO_sFOOzcdu721YBLpLOgVErJDcg9W6uTFIK5ZoBs7JDsZTtDBW1k9E-MYgGL6JWrq6KLKFK5_NvwsTGXLQHJnrWUk77-ftyyrqu6d8oRLLZPIGkBmJOEH_k1Z2BcdoG7_S3oUjVlH8ocsdp9z6JApAdpvwnIsjhxsgNX6JDwwdYERjLo0re_V82DR85mZRZ5oRxM-DZIS3wut91s4pArIHZnrRzKGfHuJfHWEjd4L0848cPyFyymuA71oDG-ZwGrw-ftP5Kyfx9cRyF634IKekQc6PLElVMWRsdDaU0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@masum_bacha01_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5443873584")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
