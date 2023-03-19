import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20214273"))
    API_HASH = os.environ.get("API_HASH", "20b5c4629faae0a9e43c362f4513abdd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",5996556154:AAHw8gPJi1gPX101ZUbhXAJJw5qusSJTWdM)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOHIBu0hObVqhNZTI4MEhl7f3KssHHL_tK5gvKNufCjYb_oM4ycxnULnTy7lySlaxA-1Un5F00NteQBoEeFl7JQVDOg0VCJLWX2iKx50NDLDek-jTmDBUIHm59-OYmrYGrdpOWLIYsj7f0RtwsSqoDJjSdfIxPFTAL9jC7aC-tfwZNhs2tSD_nnraoT-WiX-fMOj0ahkbDGOWWemMhC4ny2ZomXyQkkmUX38D55pq5ICOhCxjdcZarjBlorQDNY7TmGrv5Khot5S0s573SWs3qt3K400RvajA2UZrJDyx1qANaLb4qMYyKAA7PNMkaFUr7wnLe0ndYT-pg9R2ARE1TXKCNyE=)
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
