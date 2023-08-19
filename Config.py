import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25004662"))
    API_HASH = os.environ.get("API_HASH", "1c9f3e4b93eb1957caffab790fb5f4fd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", " 6517810094:AAEYxjE40P5sHmz046icFV4TA4jQa1KLzAo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu4C4sDhHK-1uRrLbds6YuKFJnkWm6bdScnawe4GyHGQ41hKQ-wtPAUAWUYrL1EFHlPseF2l6-nB5yHa9HvB5H-OfLswlY7tiSohHcMzmqmNgv7jXPVxdI2AUXGUTPhJwgeeEVAzSiwQfudwb3Pd4VQtuTap9esDspQi-6yZymRT-LIlD96r0HMxMoCjc48IrBUax1sdiU6tMt7kBOvSQn8GP4LqTF2IN8vhdb2zgdu26bNzFgJzcFefxHtWOP4fhKGKZqp4U-8H9wTHP0Nby44oMw-GvLuPRE6RFLfvyBl9xxhlAjVFtlHHOqxnhxQI-qLbcxC9snAJopIlGuvgHTEM=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "BaldevXmusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5468509508")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
