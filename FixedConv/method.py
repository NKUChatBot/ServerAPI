import re

from .models import Aiml


def response(question, request=None, prev=None):
    if request is not None:
        prev = request.session.get("prev_pk")
    aiml_objs = Aiml.objects.all()
    for aiml_obj in aiml_objs:
        if aiml_obj.that is None or aiml_obj.that == "":
            print(aiml_obj.pattern, question)
            p = re.compile(aiml_obj.pattern)
            if re.match(p, question):
                request.session["prev_pk"] = aiml_obj.pk
                return aiml_obj.template
        elif prev is not None:
            prev_obj = Aiml.objects.get(pk=prev)
            if aiml_obj.that == prev_obj.template:
                return aiml_obj.template
    return None
