from django.shortcuts import render
from django.views.decorators.http import require_GET

from ServerAPI.method import get_json_ret, json_response_zh

from .method import response

# Create your views here.
@require_GET
def ask(request):
    """
    教师问答系统的主要路由函数
    :param request:GET 请求需要一个 question 参数
    :return:如果请求成功 respones["data"] 中会包含一个 answer
    """
    question = request.GET.get("question")
    if question is None:
        return json_response_zh(get_json_ret(41))
    answer = response(question)
    return json_response_zh(get_json_ret(0, data={"answer": answer}))
