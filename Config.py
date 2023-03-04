import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "7223178"))
    API_HASH = os.environ.get("API_HASH", "65333a147bdad023ef0f584431390108")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5911509294:AAFIGr70b4HdGAQtsE4vkxAtO8W4J1UAie0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLMBu7TMVR4M_I95XY_CUMwwba8Gjqldi6S2LHn7b7nPqsb4-A3gc8rr1AcrKQ4BeS1oDGFPfFe7Jnjxf5bKmGSxCypQ8clefR2BwvLUGE0zBjD7HVLQ-LM_JhatKQBHnzmeAHnlpOSk23MgXD14SisnEPs8Qa2IZ4SvS_7_KNeObYTekxoOtAhqthx1jduqlWs_OfZhECsFGt6Jj4D8U4dlplfje10oI_J3yRECIVHP8qhMnMxf4wAe9ZA-HWLbe6PgNif093bQcAz6vhliy-mj3srOB4S9LquV7NAbE2trnniQtwIa2XQ4zFczeRy_u_Tbr0P3tvsAo6CtHf_21vfNL28=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "mmsvidrobot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("1929056577", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
