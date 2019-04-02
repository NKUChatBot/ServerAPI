from django.shortcuts import render
from django.views.decorators.http import require_GET

from ServerAPI.method import get_json_ret, json_response_zh

from .method import response

# Create your views here.
@require_GET
def ask(request):
    """
    实现固定问答的路由函数
    :param request: GET 请求，需要一个 question 参数
    :return:请求成功，返回数据包 data 字段中将包含 answer
    """
    question = request.GET.get("question")
    if question is None:
        return json_response_zh(get_json_ret(40))
    answer = response(question, request=request)
    return json_response_zh(get_json_ret(0, data={"answer": answer}))
