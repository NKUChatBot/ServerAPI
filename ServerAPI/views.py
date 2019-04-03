import json
import requests
from django.views.decorators.http import require_GET

from .secret import tuning_key

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
        "reqType": 0,
        "perception": {
            "inputText": {"text": question},
            "selfInfo": {"location": {"city": "天津", }},
            "userInfo": {"apiKey": tuning_key, "userId": request.session.session_key,}
        }
    })
    response = json.loads(response.text)
    return json_response_zh(get_json_ret(0, data={"answer": response["results"]}))


@require_GET
def greet(request):
    greeing_dict = {
        'init': [
            "你好呀，我是上知天文下知地理的南小开！！！",
            "嘿，你好，我是南小开。你想问什么？",
            "Hello there, What can I do for you?",
            "那边的朋友你们好吗！！！？？？",
            "我好菜啊"
        ],
        'friendly': [
            "What a great thing you just said. I'm so glad you said it.",
            "Ahh, yes, I agree. It is so great to say things, isn't it?",
            "Please, tell me more. It brings me such joy to respond to the things you say.",
            "Ahh, yes valid point. Or was it? Either way, you're fantastic!",
            "Anyways, did I mention that I hope you're having a great day? If not, I hope it gets better!"
        ],
        'confuse': [
            "我不知道，妈妈还没有告诉我",
            "小开肚子里还没吃这个知识，不如你告诉我吧",
            "我不明白你在说什么",
            "I just don't know if I can trust that thing you just said...",
            "Oh, interesting. I totally believe you. (Not really)",
            "Uh-huh, yeah, listen...I'm not going to fully invest in this conversation until I'm certain I know your motive.",
            "Wait, what the heck is that?? Oh, phewf, it's just another rogue letter 'R' that escaped the letter pool.",
            "You can't fool me, I know that's not true!"
        ],
        'boastful': [
            "我可厉害了",
            "哈哈哈，我是最棒的",
            "That's interesting. I'll have you know that I have an extremely advanced learning algorithm that analyzes everything you say...well, not really, but I wish.",
            "Hey, while I have you, I should probably tell you that I can respond in 4 seconds flat. Which is pretty fast if you ask me.",
            f"Listen, that's neat and all, but look how fast I can calculate this math problem: 12345 * 67890 = {str(12345 * 67890)}.Didn't even break a sweat.",
            "Oh, I forgot to mention that I've existed for over 100,000 seconds and that's something I'm quite proud of.",
            "Wow, thats pretty cool, but I can hold my breath for all of eternity. And it took me 0 seconds to gain that ability."
        ]
    }
    mood = request.GET.get("mood")
    from random import choice
    greet = choice(greeing_dict[mood]) if mood is not None else choice(greeing_dict["init"])
    return json_response_zh(get_json_ret(0, data={"greet": greet}))
