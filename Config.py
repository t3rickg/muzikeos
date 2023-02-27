import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6087485386:AAHqhgeDORPL2wfWwKnWiYneH0R5xyk0s6w)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOH8Bu7tYx_MMm1_y3e4lf5FcGslPQqHJBufMq68eXUgPjseaSZmYyRbefZtBSBkBhioc_IV2HjYmdc0tY6NfUCB3LRWx2QHtwgts9cREc-V5_15Z7hRoIcRZk5Xdp6REEoD-PyanAC5kZOyKD2w3Homlo8pRUfWOtUsNKoPO43RZw6gPVqNtjtt3-CyQDIC3o6adGm8lkyVGjOagGZf3EC8cy5R3v2IZ9Q07nnUbT16tXvBEcyuzLWeqP4GhxDuDVsd7yRhsHe3ZWqZnrDp7wR1nkTC8fjmbWyx3y3qiAlls7q0CWczH4vRf6eBCAAjHiOevcsmB20pHS8JUjPjfe4c4VEo=)
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
