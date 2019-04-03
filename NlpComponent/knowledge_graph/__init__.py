from . import question_respond


def respond(question):
    try:
        ans = question_respond.respond(question)
        return ans
    except:
        return None