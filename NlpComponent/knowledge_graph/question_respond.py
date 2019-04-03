import sys
import os
from . import sentences
import random
import py2neo
from py2neo import Graph, Node, Relationship, PropertyDict

endSentence = ['哦', '~', '吖', '呐', '呢', '喔', '嘿']

abs_path = os.path.split(os.path.realpath(__file__))[0] + '/'
# print(abs_path)


graph = Graph('bolt://140.143.78.7:7687', username='neo4j', password='NKU@)!*QA')


# print(graph)

def randEnd():
    return random.choice(endSentence)


def comb(a, b, c):
    return a + b + '是' + c + randEnd()


def findRelation(start, sentence):
    query = "match (u)-[r:%s]->(v) where u.name='%s' return v"
    for word in sentence:
        res = graph.run(query % (word, start)).data()
        # print(query % (word, start), res)
        if res:
            return comb(start, word, res[0]['v'].get('name'))
    return None


def findAttribute(node, sentence):
    for word in sentence:
        # print(word, node)
        if node.get(word):
            return comb(node.get('name'), word, node.get(word))


def respond(question):
    sentence = sentences.Sentences(update=True).sentences_cut(question)
    # print(sentence)
    words = []
    query = 'match (e) where e.name="%s" return e'
    for word in sentence:
        try:
            res = graph.run(query % word).data()
            if res:
                ans = findAttribute(res[0]['e'], sentence)
                if not ans:
                    ans = findRelation(word, sentence)
                if ans:
                    return ans
        except Exception as e:
            # print(e)
            pass
    return None


if __name__ == '__main__':
    question = "南开校训？"
    print(respond(question))
