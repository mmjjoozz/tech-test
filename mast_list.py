import csv
from mast import Mast
from operator import attrgetter

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
                    int(l[9]),
                    float(l[10])) for l in reader]

    def get_sorted(self, by='current_rent', reverse=True, num=None):
        s = sorted(self.masts, key=attrgetter(by), reverse=reverse)
        if num:
            return s[:num]
        else:
            return s

    def get_by_lease_years(self, lease_years=25):
        return [mast for mast in self.masts if mast.lease_years == lease_years]



