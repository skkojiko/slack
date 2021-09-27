import requests

from slack.slack import const

GET_CHANNELS_URL = "https://slack.com/api/conversations.list"


if __name__ == "__main__":
    channel_list = requests.get(
        GET_CHANNELS_URL, headers=dict(Authorization=f"Bearer {const.TOKEN}")
    ).json()["channels"]

    for channel in channel_list:
        print(channel["name"], channel["id"])
