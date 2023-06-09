from requests import post, get  # for creating requests to google servers
from json import loads          # for loading secret token data from json
import codes                    # for code verifier and challenge

fileUrl = "https://www.googleapis.com/upload/drive/v3/files"   # google drive url to post
oAuthUrl = "https://accounts.google.com/o/oauth2/v2/auth"
tokenUrl = "https://oauth2.googleapis.com/token"
# SCOPES = "https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/drive.metadata https://www.googleapis.com/auth/drive.metadata.readonly https://www.googleapis.com/auth/drive.photos.readonly https://www.googleapis.com/auth/drive.readonly https://www.googleapis.com/auth/drive.scripts"
SCOPES = "https://www.googleapis.com/auth/drive.file"

fileContent = "kocham pcimcie!"

with open("secret_token.json", "r") as file:
    jsonStr = file.read()
    secretTokenData = loads(jsonStr)
    client_id = secretTokenData["installed"]["client_id"]
    client_secret = secretTokenData["installed"]["client_secret"]
    redirect_uri = secretTokenData["installed"]["redirect_uris"][0] + ":8000"

codeVerifier = codeChallenge = codes.getCodeVerifier()
oAuthCodeRequestParams = {
    "scope": SCOPES,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "client_id": client_id 
}
oAuthTokenRequestParams = {
    "code": "",  # to be filled later
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code"
}
fileRequestParams = {
    "uploadType": "media",
    "access_token": "" # to be filled later
}

# headers to specify a file type
headers = {
    "Content-Type":     "application/octet-stream",     # default type
    "Content-Length":   "16"                             # 8 bytes long
}

# post the request and follow the printed link in your browser
req = post(oAuthUrl, params=oAuthCodeRequestParams)
print("link:", req.url)

# set the code in params
code = input("Enter the code recieved from Google API: ")
oAuthTokenRequestParams["code"] = code

# post the access token request
req = post(tokenUrl, params=oAuthTokenRequestParams)
accessTokenData = loads(req.text)
accessToken = accessTokenData["access_token"]
fileRequestParams["access_token"] = accessToken

post(fileUrl, params=fileRequestParams, headers=headers, data=fileContent)
