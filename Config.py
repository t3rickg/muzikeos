import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "22659994"))
    API_HASH = os.environ.get("API_HASH", "2c89964a0088a7a39ec819c60ae67de7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5909970619:AAGbiFzsH_Owy350MUmHhdPDQsPddEr-0Xw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BAFZw5oAmsyl8oc-dscXvX4upz6GKviqPKI1JoNg_z_KMbpVNUtqgnphsj3uVkNTUcSrvByli1LkZzN9fwVVjhtm0VjFQ5qFGatQ5T4_3MqdC36XEAFR_G9Gzl-Ib7sI8QX2vLRdxE6_rNxRpYg_jgKLJSHv6-hV48LHERYuRDLcSsXvgQOI-9P_zTPVKWSYfrrhah3su12BdU4vnIOYTkVR3BuAJ1ziWKwTxh33kbHn-Kbzhw7rU_zroJeSWbBd9emNs3oADFxV1ocL3LToOW6IzXE_tXB_PiOmWn_K4OxhbVsi6v9M1Nd_suO1cAMYTeCfOVXFzFt-g_iHavB6gygVwhtjkwAAAAG-dXUpAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "pstoptoptos") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "pstoptoptos") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7490336041")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
