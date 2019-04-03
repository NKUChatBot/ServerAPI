from django.shortcuts import render
from django.views.decorators.http import require_GET

from ServerAPI.method import get_json_ret, json_response_zh

from .method import response
from .models import WordVectorCache, WordVector


# Create your views here.
@require_GET
def get_vector(request):
    """
    通过传入一个词语，查询其 200 维向量的路由函数
    :param request: GET 请求，需要一个 word 参数
    :return:如果请求成功，data 中返回一个 vector
    """
    word = request.GET.get("word")
    if word is None:
        return json_response_zh(get_json_ret(40))
    try:
        wv = WordVectorCache.objects.get(word=word)
        wv.increase_call_times()
        return json_response_zh(get_json_ret(0, data={"vector": wv.get_vector()}))
    except WordVectorCache.DoesNotExist:
        wv = WordVector.objects.get(word=word)
        WordVectorCache.objects.create(word=wv.word, vector=wv.vector)
        return json_response_zh(get_json_ret(0, data={"vector": wv.get_vector()}))
    except Exception as e:
        pass
    return json_response_zh(get_json_ret(44))


@require_GET
def ask(request):
    question = request.get("question")
    if question is None:
        return json_response_zh(get_json_ret(42))
    answer = response(question, request=request)
    return json_response_zh(get_json_ret(0, data={"answer": answer}))