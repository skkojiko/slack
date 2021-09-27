import time

import requests

from slack.slack import const


GET_HISTORY_URL = "https://slack.com/api/conversations.history"
DELETE_CHAT_URL = "https://slack.com/api/chat.delete"


if __name__ == "__main__":
    for channel in const.CHANNELS:
        while True:
            headers = dict(Authorization=f"Bearer {const.TOKEN}")
            params = {"channel": channel}
            messages = requests.get(
                GET_HISTORY_URL,
                headers=headers,
                params={"channel": channel},
            ).json()["messages"]
            if not messages:
                break

            for message in messages:
                params["ts"] = message["ts"]
                response = requests.post(
                    DELETE_CHAT_URL, headers=headers, params=params
                ).json()
                print(response)
                time.sleep(0.8)

    print("DONE!")
