import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6068306451:AAHsr2aYQbwnfps8Q0DcUbwa_hNGyV_2syI)
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBgJfOC2ScrvhhdlosmONGs1x68A3bwa50WDyN5kWf2FPjZsk2cN_yut6G1kaTJjbzQ_4zl_FJWGxIAADRtpImcNMDOdkL_0np_g_we1ElVPYUMNAe0kdwFjxLX8IcZ3LJo3aAfLF-eT0KLP4kxAJ9CERKZwsQsPKDsUESkmBpnKaNcSUHw3p8dkwnWHLcn-6gaBP8Edcy3uiH6Gj_Cn2PmxWVs1pAwSUe0DEyW_dQBKs0TaHxMi0iD0WPzrH95YX9PGigFhaPXI5xId9WLW6l_7IDqrwO9whBkEVW7ywqKluV9tkTltU3s3hVi-X3MMCtCAXdECostyPgwLU2dSqibAAAAATSnUZMA)
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
