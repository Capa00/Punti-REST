from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Example ./manage.py dev -c debug -f ./dev.txt"

    # def add_arguments(self, parser):
    #     parser.add_argument('-f', '--filename', type=str, help='File name of backup')
    #     parser.add_argument('-c', '--command', type=str, help='command to launch')

    def handle(self, *args, **kwargs):
        # filename = kwargs.get('filename')
        # command = kwargs.get('command')
        # if command and command=='debug':
        #    return
        pass
