import requests

def send_notification_webhook(url, new_state):
    message = "Job project changed status to : {}".format(new_state)
    requests.post(url, json={"content": message})
