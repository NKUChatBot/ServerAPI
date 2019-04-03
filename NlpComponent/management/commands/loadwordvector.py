import json
from django.core.management.base import BaseCommand

from NlpComponent.models import WordVector


class Command(BaseCommand):
    help = u"从文件中加载 WordVector"

    def handle(self, *args, **options):
        f = open("./vocab/w2v.txt")

        from os import path
        if path.isfile('load_pos.log'):
            line_num = int(open("load_pos.log", "r").read().strip())
        else:
            line_num = 1
        for i in range(line_num):
            next(f)

        for line in f:
            l = line.split(' ')
            if WordVector.objects.filter(word=l[0]).exists(): continue
            WordVector.objects.create(word=l[0], vector=json.dumps(l[1:]).replace(' ', ''))

            with open("load_pos.log", "w") as ff:
                ff.write(str(line_num))
            line_num += 1
            print(str(line_num))

        f.close()
