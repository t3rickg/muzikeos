import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6286300952:AAEYwKc8pDWOqVfD_eYEVxgOCDiMgNR2mck")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu0swnR3HUKUE8yChrIxMnwFOJZkEmHH5pDTWXGrm1end8sS_lrLnnii8PUufDcSZma2_FYYXPvjTHNx89bGqHhLmLaYV7k2HA553Fu4Mg-FKX6Vn2NOfjav-Pogg3ASINa1HTGEf7QcXJsLlRFLg0cf89bdtPfPy3ays4Ob6gKzy2wLjTTDIvxUMKLimovDe1ROfNC_1kocd8w8l9XddNgJlAuXLhYjmkWt9A9smIRUtn28oYU3EDYf1fbShvDkoUMMlVm7lIoWGFc4xUgJl46ncwUCuglGgo17z06-TD2tkrpXJCFuKMpDQOg4Vzs4Ey1J5v8Nmnt7DOYezqRwkx2E=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musicxzreaswe_bot")
    SUPPORT = os.environ.get("SUPPORT", "papokm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "cvxzasoe") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6294217355")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
