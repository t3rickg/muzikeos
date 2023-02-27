import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "23689112"))
    API_HASH = os.environ.get("API_HASH", "83c73f8446efa4b57cbdd71fd0960b14")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5838739088:AAG-JuIGEg_HT0_YtSfjhO2Vlt-bH-PjUmQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIkBu5wsQhsAcZ3uAZMYeXARcFK_uRmx_ldtgwxy0WqQbGfONaAHzVSLYghddm3CSi0BeU5dFkg90lc_Nv_vvFl3tBLX6N9m9OL3gaUqZVqAGzl4Z9CcA_T7A9NYFab6g3wxeqO8Srma75hT830sTAUVkQc6dEbsWBtocrKnvEAfgnKOVBftSOQFAVCzj-r1NpTLuyQGZTUOcaEHgPfzjuPd1FF6mgXGinPbY2OlyEtLudHVidzz3tuUazENH929TLD6Bqbm8ivw17UpG_S1q53cnzrJLv-v7yNks-ydo53gcVcUAQKpksdFSOJF3gtog6AXhGNJVGrpmOCmUAXUdHoEkR4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Brutal_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
