import json

import requests

from slack.slack import const

GET_FILES_URL = "https://slack.com/api/files.list"
DELETE_FILE_URL = "https://slack.com/api/files.delete"


if __name__ == "__main__":
    response = requests.post(GET_FILES_URL, data=dict(token=const.TOKEN))
    print(json.dumps(response.json(), indent=2))

    for image in response.json()["files"]:
        print(f"Deleting file {image['name']} ...")
        requests.post(
            DELETE_FILE_URL, data=dict(token=const.TOKEN, file=image["id"])
        )

    print("DONE!")
