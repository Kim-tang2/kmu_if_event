import requests
import datetime
from login_info import username, password

time = int(datetime.datetime.now().timestamp())

instaLoginInfo = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'queryParams': "{}"
}

instaSession = requests.session()
with instaSession as e:
    req = instaSession.get("https://www.instagram.com/accounts/login")

    cookieStr = str(req.cookies)
    loginCSRFtoken = cookieStr[37:69]
    requestsHeader = {
        'origin': "www.instagram.com",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'x-csrftoken': loginCSRFtoken,
        'x-instagram-ajax': "de81cb3fd9c4-hot",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "*/*",
        'referer': "https://www.instagram.com/accounts/login"
    }

    login = instaSession.post("https://www.instagram.com/accounts/login/ajax/", data=instaLoginInfo,
                              headers=requestsHeader)

    print(login.status_code)
