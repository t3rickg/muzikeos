import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29255460"))
    API_HASH = os.environ.get("API_HASH", "466315333c42a20e8ef3bbe9dffc9724")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6155652608:AAGxki1S8CIh4V_q5QCLNB8gml92IAIC8XY)
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOK4Bu5wa_MsI0vtLzSUftXDwDMTIhnroMd0EJw_fhzz-OEZuS7z-Sb3CfTE9JqzXZ4CcMZ6P4EXrYApNwFyOZG-jlVEc62P4q1sD_k8WrxY2j7ozA2fcpz170Ew0C2MX392TZIxv4U5hdJQC-11xobpne1DzNNTA99pSssJSXBoltORjvtsVUNeTumu8XqmcH13ZtMrhGF1J4Zd6Wq3QYtzjKO9In-_Fqxfs4B3Q3TfcfwcZjvTDqtyBsr6zbDp--xjBffk2F-ny9M8L4mVLe-Xtr4mv2MQ82oNzWcAXsYrlw77rnHID4oGFDA9WgqOqGbz1fbQ9IAkQScznwssoHPuZYIM=)
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
