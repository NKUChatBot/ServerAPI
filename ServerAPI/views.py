import json
import requests
from django.views.decorators.http import require_GET

from ServerAPI.method import get_json_ret, json_response_zh
from TeacherMsg.method import response as teacher_response
from FixedConv.method import response as fixed_response


@require_GET
def ask(request):
    """
    实现总的问答环节的 API
    :param request:GET 请求，需要参数 question
    :return:data 中包含 answer 字段
    """
    question = request.GET.get("question")
    if question is None:
        return json_response_zh(get_json_ret(40))
    answer = teacher_response(question, request=request)
    if answer is not None:
        return json_response_zh(get_json_ret(0, data={"answer": answer}))
    answer = fixed_response(question, request=request)
    if answer is not None:
        return json_response_zh(get_json_ret(0, data={"answer": answer}))
    response = requests.post("http://openapi.tuling123.com/openapi/api/v2", data={
        "reqType":0,
        "perception": {
            "inputText": {"text": question},
            "selfInfo": {"location": {"city": "天津",}},
            "userInfo": {
                "apiKey": "004c80aecff04ac6b27a967162b941b2",
                "userId": request.session.session_key,
            }
        }
    })
    response = json.loads(response.text)
    return json_response_zh(get_json_ret(0, data={"answer": response["results"]}))
