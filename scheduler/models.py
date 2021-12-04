from django.db import models
from django.db.models import CASCADE

from punti.settings import DNA_MAX_LENGTH


class Brain(models.Model):
    _dna = models.TextField(max_length=DNA_MAX_LENGTH)
    next = models.ForeignKey('self', on_delete=CASCADE, related_name='previous', blank=True, null=True)

    @property
    def ids(self):
        return [b.id for b in self]

    @property
    def dna(self):
        return "".join([b._dna for b in self])

    def __iter__(self):
        return Brain.Iterator(self)

    class Iterator:
        def __init__(self, curr):
            self.curr = curr

            while True:
                if not self.curr: break

                last = self.curr
                self.curr = self.curr.previous.first()

            self.curr = last

        def __iter__(self):
            return self

        def __next__(self):
            if self.curr:
                ret = self.curr
                self.curr = self.curr.next
                return ret

            else:
                raise StopIteration
