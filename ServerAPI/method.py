from django.http import JsonResponse


def json_response_zh(json_data):
    """
    因为返回含中文的 Json 数据总是需要设置 {'ensure_ascii': False}，所以直接在此集成
    :param json_data: 需要返回的数据
    """
    return JsonResponse(json_data, json_dumps_params={'ensure_ascii': False})


def get_json_ret(code, msg=None, err=None, data=None):
    """
    :param code: 一个整数型的标识码
    :return: 一个字典对象，包含 code 键值和 msg 信息或 err 信息。
    """
    res = {
        0: {"code": 0, "msg": "请求正常"},
        # TODO: 以 4 开头标识用户请求错误
        40: {"code": 40, "msg": "请求错误", "err": "请求参数缺失"},
        41: {"code": 41, "msg": "请求错误", "err": "请求参数错误"},
        42: {"code": 42, "msg": "请求错误", "err": "用户权限错误"},
        43: {"code": 43, "msg": "请求错误", "err": "请求过于频繁"},
        44: {"code": 44, "msg": "请求错误", "err": "请求逻辑错误"},
        # TODO: 以 5 开头标识服务器检查错误
        50: {"code": 50, "msg": "检查错误", "err": "验证码无时效、错误或不存在"},
        51: {"code": 51, "msg": "检查错误", "err": "数据项已经存在"},
        52: {"code": 52, "msg": "检查错误", "err": "数据项不存在"},
        53: {"code": 53, "msg": "检查错误", "err": "拒绝上传文件"},
        # TODO: 以 6 开头表示第三方错误
        60: {"code": 60, "msg": "第三方错误", "err": "短信验证码发送失败"}
    }[code]
    if err is not None: res["err"] = err
    if msg is not None: res["msg"] = msg
    if data is not None: res["data"] = data
    return res


def is_allowed_file(filename):
    """
    通过文件名检查上传的文件类型是否合法
    :param filename: 文件名
    :return:如果合法则返回 True，非法则返回 False
    """
    # TODO: 文件名中不能包含 `/` 与 `\`
    slash = ('/' not in filename) and ('\\' not in filename)

    # TODO: 只支持 jpg 与 png 文件格式
    allowed_content_type = [".jpg", ".png"]
    content_type = False
    for ct in allowed_content_type:
        if filename.endswith(ct):
            content_type = True

    return content_type and slash