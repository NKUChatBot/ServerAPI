import json
from django.core.management.base import BaseCommand

from NlpComponent.models import WordVector


class Command(BaseCommand):
    help = u"从文件中加载 WordVector"

    def handle(self, *args, **options):
        with open("./vocab/w2v.txt") as f:
            first_line = f.readline()
            for line in f:
                l = line.split(' ')
                if WordVector.objects.filter(word=l[0]).exists(): continue
                WordVector.objects.create(word=l[0], vector=json.dumps(l[1:]).replace(' ', ''))
