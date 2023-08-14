import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20092138"))
    API_HASH = os.environ.get("API_HASH", "74f8d9a67cdafc4711d393e4df1cce35")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6536119132:AAE5DcITmroKnlwm9YXXx1IyX0v6YCjT-Pw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu6Z2szlLT2BugX64aoJJsZvNSw3vB-DZdNiMAbml2sOR8aamW-3deeQyhDL_Hpw1gezal5IdHsbhrxbJcDlaAF0C42v49cD0-x1LS5yrYVqaWPxl3TV0ePdBZyT-PfxIVKQXVDeW_RWb2jAeWWPRxGoUkNUKx_TgpvILOzHeMcS-5-MJMarpG-tEfkiR5HPaz7OrQ8ZRuRiCBofvQ2ewLbvNfOvgyonJln1v8rRYprUwzbrtatXjzaBCI0qtUT4ujEx68Cu1MH5d-MxBfkiM1q3BkJoLp3nZEpT0wqh8cx1ctctSgGf41cf8moZk5tKc1pqNV2Hi1SYmcPBQ_7AnVV4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Zoroz4")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
