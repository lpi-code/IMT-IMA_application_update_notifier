import json
import requests
import bs4 as bs
class IMAClient:
    def __init__(self, base_url : str, username : str, password : str) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-GB,en;q=0.9",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Microsoft Edge\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self._login()

    def _login(self):
        # Get token
        r = self.session.get(self.base_url + '/')
        soup = bs.BeautifulSoup(r.content, 'html.parser')
        token = soup.find('input', {'name': 'app_authentication_login[token]'})['value']
        url = self.base_url + '/authentification/connexion'

        data = {
           "app_authentication_login[username]": self.username,
            "app_authentication_login[password]": self.password,
            "app_authentication_login[token]": token,
            "app_authentication_login[rememberMe]": 1

            }

        # send as form data
        r = self.session.post(url, data=data)
       
        if r.status_code != 200:
            raise Exception('Login failed')
    
    def get(self, url):
        r = self.session.get(self.base_url + url)
        return r