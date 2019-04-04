import json
import threading
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from NlpComponent.models import WordVector


def insert_word(l):
    try:
        WordVector.objects.create(word=l[0], vector=json.dumps(l[1:]).replace(' ', ''))
        return True
    except IntegrityError:
        return False


class Command(BaseCommand):
    help = u"从文件中加载 WordVector"

    def handle(self, *args, **options):
        f = open("./vocab/w2v.txt")

        from os import path
        line_num = int(open("load_pos.log", "r").read().strip()) if path.isfile('load_pos.log') else 1

        for i in range(line_num):
            next(f)

        for line in f:
            l = line.split(' ')
            t = threading.Thread(target=insert_word, args=(l,))
            t.start()
            line_num += 1
            print(str(line_num))

        f.close()
