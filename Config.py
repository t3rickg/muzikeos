import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5872315294:AAE1yJIinxu2UcF9ZTCUxb2YFwfh3pkX0SM)
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOL4BuwpfaimTjaEcgN9ReRTGMjgbcuSpXLm8DSRF1FVYdzlcaxWO5Q-ofS16124uQoDivPihKtp2UNJWX_9RWJN8IdYyNUbV26F0IAmndffYrv0oehxoYL1VveSQISW__f4xGItFaWI5cp--vyBh9wMbrxKf8doODEN-saXh7FoDVdIEPvP6AnoKz20zi32jaZzsKpB26PEUSuYqRwfU8Fsvzawwj7Ua31y8eKnIBf-WMZF3WBSzuX05BP0V6MflesdKKmdBxElThcKQRQ8EhjhYjAfYZdiVsX5LqcUQfUIE5yj0xaV4fdNDB-mHy9PzMM6PrCNOabrL3ScGFTEXEDtAjtM=")
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
