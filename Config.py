import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6413040986:AAENMMywWgeBJyAHZwuYkn0Zk_L1WJprGlw)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIEBu7RJuNlAk3ZYZL9ikV0PfpWCWJvSBpfO4-jwQ4iZU6oKfachqvNSKCtVjdXW0oYkxjCSpyamcN1_27ldY2vPnlYaIBEIyPTMYNqIZQSEyzukukBtwvIUzEiIJ5SAUT79S7VgR0oWuX_7ym45ahDHinBdX2EyHzG8xR7HHWPt-zMmUX6WWSHb02J5Otx-5tcMXyQpk5xb2yddcGMdx-LgqTIQkmbm-zH981CQjib0E_L5mpqI83Kd1ScI4GMyoW8SD4abvm5kYKvfUt9BC9l73hEU7xPoZquCfqOOvxlJbbFtXg6Z9N7lMVoehkD0AX9QN-fwLKCw4V1S7kDqmcn7FIs=)
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
