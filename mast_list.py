import csv
from mast import Mast


class MastList():
    def __init__(self, path):
        self.masts = self._parse(path)

    def _parse(self, path):
        with open(path, 'r') as data:
            reader = csv.reader(data)
            next(reader, None)
            return [Mast(
                    l[0], 
                    '{} {} {} {}'.format(
                        l[1], l[2], l[3], l[4]
                    ),
                    l[5], 
                    l[6], 
                    l[7],
                    l[8],
                    l[9],
                    l[10]) for l in reader]



