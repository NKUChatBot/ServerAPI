import json
import threading
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from NlpComponent.models import WordVector

max_thread_amount = threading.Semaphore(10000)


class InsertThread(threading.Thread):
    def __init__(self, l, line_num):
        threading.Thread.__init__(self)
        self.l = l
        self.line_num = line_num

    def run(self):
        with max_thread_amount:
            try:
                WordVector.objects.create(word=self.l[0], vector=json.dumps(self.l[1:]).replace(' ', ''))
                print(f"success: {str(self.line_num)}")
                return True
            except Exception as e:
                print(f"fail: {str(self.line_num)} [{e}]")
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
            t = InsertThread(l, line_num)
            t.start()
            line_num += 1

        f.close()
