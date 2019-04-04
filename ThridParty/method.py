import json
import requests

from ServerAPI.secret import tuning_key
from ServerAPI.method import get_json_ret, json_response_zh


def ask_tuling123(question, request=None):
    post_data = {
        "reqType": 0,
        "perception": {
            "inputText": {"text": question},
        },
        "userInfo": {
            "apiKey": tuning_key,
            "userId": request.session.session_key,
        }
    }
    response = requests.post("http://openapi.tuling123.com/openapi/api/v2", data=post_data)
    response = json.loads(response.text)
    answer = ''.join([r.get("values") for r in response.get("results")])
    return answer
