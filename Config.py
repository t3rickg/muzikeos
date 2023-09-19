import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6673102864:AAEsazdr8KNFm9caJrnxm-FjQ1Gu8lRtGu8)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOMUBu0dHXUOuaSg53ZDNbjWGkkaO_uu3zeEwEeku2izYrHDrs0RZEL5m9jUj78dMNu3jSL8lxLNIfCxsUlfPEYrUhxaZVLwOCCAs931RxiN5WbcDYbQDNvmnR8L0ZyKV3DpI8qHeZLWKh55w2h3YbO4d4h1sQPOnvJBK5nwirlpBQyqZXy4S6auqKKwDOh_agFsMncDlLZHm4GyUryziMzGC63t7CsOlyPo3SyqB-EeFRBzMyKo0BGesnstgYYKs2ZRPbzaO1t-kxGcGTL-N25zCUt20PJJDn_8nz-4MWb5COvV6JWLZg7tq6bQ3cfvIDDq3m3KdnxrG0KNPoAjy31ZDEY4=)
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
