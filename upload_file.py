import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


TOKEN = ""

LOCALFILE = "analise_comportamental_sentimento_culpa.PDF"
BACKUPPATH = "/pasta/analise_comportamental_sentimento_culpa.pdf"

dbx = dropbox.Dropbox(TOKEN)

with open(LOCALFILE, "rb") as f:
    print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
    try:
        dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode("overwrite"))
    except ApiError as err:
        print(err)
