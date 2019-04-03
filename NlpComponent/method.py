from . import knowledge_graph as kg

def repsonse(question, request=None):
    return kg.respond(question)
