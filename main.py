from IMAClient import IMAClient
from bs4 import BeautifulSoup as Soup
from time import sleep
import yaml

from discord_hook import send_notification_webhook
def main():
    # Load secrets from secrets.yaml
    with open('secrets.yaml') as f:
        secrets = yaml.load(f, Loader=yaml.FullLoader)
    username = secrets['username']
    password = secrets['password']
    webhook_url = secrets['webhook_url']
    job_path = secrets['job_path']
    client = IMAClient('https://appima.fr', username, password)
    trimmed_text = ""
    while True:
        soup =  Soup(client.get(job_path).content, 'html.parser')
        div = soup.find('div', {'class': 'col-xl-5'}).find('div').find('div')
        text = div.text.strip()
        if trimmed_text != text:
            trimmed_text = text
            send_notification_webhook(webhook_url, trimmed_text)
        sleep(60)
if __name__ == "__main__":
    main()