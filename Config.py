import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6048456911:AAGB5JeC6XtgC6nyWSW7sdeotM9cYuq5vhE)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1ApWapzMBuxgVzKekvfQL8UTLn_PeL5Ekz07UUnyik5WtN65XH5wEXG3bH4Ydo_c3pNOKdJ-wMLytwIMG_6mhqrjb3z4Ir-NE1DsYBnENjCwozGNH5LJvQbL53ltj9nWukNGdHqaYNKMiLzL6OpPYQhNtMTinu6DaL8ubC1kWN53VTWUB6fPYj1u44iitjbGcXMkGde69KFG8m1vvEsvPEofm_MFXiFKl_7TvblsoYB8z2_rzspr_Y15Fb2TRY5qN3yR1Vu52fM9j9EihCuCxzTMRSH7Q2eUSA46nAYpKNdpGh9arMohDskZ2F4sC6IGZsqpwdRYXNQEylUPQecDQuKithWqi034=)
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
