import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28194700"))
    API_HASH = os.environ.get("API_HASH", "f8287d3ee565b54e5d096f3f8913ae03")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6191191278:AAFOdclKx0Cw-04HzBOBJVBJkPkLpGwCJ3s")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI0Bu665NXZ5AdMSY36daRwTgr1pen5ifPw5rrauLQJ8mLZP2W_oYn88ae0CXkGC8Bt-9-9L4ruhtlw50RIqjnGhz5NJsKxb7OGfM4EZ-4gJ1cO1C7kKvdHd-HPQQk9B5tCsaMiTsYx2qfircDkTD-pgeGSK2iEoHV6iL41M9gOYTlPBhXoni5ZJ_WUa22W6oURtLMgHPlk1LPCEMuXLmWxAnOuHnHDCUeVl0JYy3PQjxRlDL56VSrjJ_cB3055jbXJDKgCCua3a7qfzuPpGrpvq5O7olZh21zb96BV6yq32sZJK2ls5y6J4Jo5m_jJh4N6uBzuw-vk0BgeKfaONu8hVNk4=")
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
