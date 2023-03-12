import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "26072070"))
    API_HASH = os.environ.get("API_HASH", "0cb84c3b80049fe7e46c647fcd14db11")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6024133735:AAHk3xm4sUzsPeJNXyEdXBAq_FXkjJrtRxg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQGN1AYAsGVJzHJtYdWmKm6BZzcgfXpZGR9ESWmWrNJzvYnYj13sDQ_XVQjFWD_fhuEtZrLnGup3PdPigL_mzV10Zaj-Tv-CSE2WW7nmTPmx-MHarJLRH1xevnGiMk-U6spouzWYGn585KfpvGf2R7LH3_laU5ShINFXK_fqUEwBs1y1Z9W4B96i5xaLIBDPUY8FFjklr1ALqajnDhbxbdPpVl5FaolrJiF-Gf4lR1navWw4nck8S-Xu5DaR-GM0uP6m-TT_vSKGXNAVM4F3HC4VUpy2SiZDPNRfzjTRLdFWcyV2XC2EMI7FIAh7PMzToFYqW9iDguwjdu4tTUqwM96x4Ts2zgAAAAByVwteAA")
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
