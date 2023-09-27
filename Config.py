import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "24808890"))
    API_HASH = os.environ.get("API_HASH", "c64f4aa5deb88d7a3d8ef3017c475282")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6325562367:AAEePqSZYwMx8sHkG_qfeHgsj9B52A2Di_g)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOL4BuwOrMBPQ1sh6wCNga62PIfvkemDXUo1-k9QemiHT24nH0ojULNW3jNMsZPXKujWDqT4zHysRpIYB1nc9aXkqdvkFSLMkiRWrIW0rKuWD5UvkICxyR83zOZZp5w5508mmf8YSri578JQ4AC_UguDR9XKrGFBhpU0Yt4TAI_u9MYD354_zCGhc2NTEV27KqcFKM2Z-AW536oXVs6bgxzmq4O8PnFRCp5E5GcIXZlQ3H9m-WDrj0WI_HlNAxTtzn5laQvFsZBXRiMVbCqaKmRT_8dJtv2jJMYzyIMdbEzOgptfswHVQsqghsbM6kKELAmHwwwwJ89zJWWzzT84lFk-7TYA=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ayii_AM_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
