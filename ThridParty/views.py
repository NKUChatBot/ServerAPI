from django.shortcuts import render

from ServerAPI.method import get_json_ret, json_response_zh

from .method import ask_tuling123


# Create your views here.
def ask(request):
    """
    实现调用第三方库的路由函数，此处调用图灵机器人的库
    :param request: GET 请求，需要一个 question 作为参数
    :return: 如果请求成功，data 中包含 answer
    """
    question = request.GET.get("question")
    if question is None:
        return json_response_zh(get_json_ret(42))
    answer = ask_tuling123(question, request=request)
    return json_response_zh(get_json_ret(0, data={"answer": answer}))
