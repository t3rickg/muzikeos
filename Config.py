import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6207643647:AAHE_R-9xkJcoRaZKx932D72KkyxdvbtNTk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLMBu4esacYyrMkQSqwyGr_8f0n7SPK-uJhz0wnGWbZUzHknqP_nYha348XHXNCnnPiYbJ95qwGGqnK4PPP9blMOOiaMsjb7SgyRSd1QH3AZ62Ami-01_ujdQpCDEMbZ82sgcCzzn2n6UUSkwqrTbJI7CHvPLrJnN46XDY9M-Xr4EsGilJI7uxnfp6r5z7uf-WjIFnvJ66pd8vmcZ6sy4FY05XaFrOk34_WH994ccNTok9-nOv0jPCfbGEpvImJ8lE1dp44iVbruxlfAIOHUtRvOkPBzWGCYsm3mF35WKfcJaBlHz2uTpm7b3-Ay_o2cnoMKcdDQwMQrv8r48nZNoqAnVec=")
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
