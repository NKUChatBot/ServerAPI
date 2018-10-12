from django.shortcuts import render
from django.http import JsonResponse
from pickle import load as load_pickle
import ao_wordvector


def JsonResponseZh(json_data):
    """
    因为返回含中文的 Json 数据总是需要设置 {'ensure_ascii': False}，所以直接在此集成
    :param json_data: 需要返回的数据
    """
    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False})


# Create your views here.
def get_word_vector(request):
    WV = load_pickle(open("WV.pkl", "rb"))
    word = request.GET.get("word")
    if word is None:
        return JsonResponseZh({
            "code": 1,
            "msg": "请求错误",
            "error": "请指定 word 参数",
        })
    vector = WV.get_word_vector(word)
    if vector is None:
        return JsonResponseZh({
            "code": 1,
            "msg": "请求错误",
            "error": "未找到请求词",
        })
    else:
        return JsonResponseZh({
            "code": 0,
            "msg": "查询成功",
            "data": vector.tolist(),
        })