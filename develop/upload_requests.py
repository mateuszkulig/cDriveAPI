from requests import post, get  # for creating requests to google servers
from json import loads          # for loading secret token data from json
import codes                    # for code verifier and challenge
import url_manip                # for parsing params into url

postUrl = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"   # google drive url to post
oAuthUrl = "https://accounts.google.com/o/oauth2/v2/auth"

# SCOPES = "https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata https://www.googleapis.com/auth/drive.metadata.readonly https://www.googleapis.com/auth/drive.photos.readonly https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/drive.scripts"
SCOPES = "https://www.googleapis.com/auth/drive.file"

with open("secret_token.json", "r") as file:
    jsonStr = file.read()

secretTokenData = loads(jsonStr)

codeVerifier = codeChallenge = codes.getCodeVerifier()

oAuthRequestParams = {
    "scope": SCOPES,
    "response_type": "code",
    "redirect_uri": secretTokenData["installed"]["redirect_uris"][0] + ":8000",
    "client_id": secretTokenData["installed"]["client_id"]
}

req = post(oAuthUrl, params=oAuthRequestParams)
print(req.url)

# headers to specify a file type
# headers = {
#     "Content-Type":     "application/octet-stream",     # default type
#     "Content-Length":   "8"                             # 8 bytes long
# }

# data = "Hello W"

# post(postUrl, headers=headers, data=data)
