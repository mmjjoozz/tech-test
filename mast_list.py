import csv
from mast import Mast
from operator import attrgetter
from datetime import datetime as dt


class MastList():


    def __init__(self, path):
        self.masts = self._parse(path)


    def _parse(self, path):
        with open(path, 'r') as data:
            reader = csv.reader(data)
            next(reader, None)
            return [Mast(
                    row[0],                                               # property name
                    '{} {} {} {}'.format(
                        row[1], row[2], row[3], row[4]                    # property address
                    ),
                    row[5],                                               # unit name
                    row[6],                                               # tenant name
                    dt.strptime(row[7], '%d %b %Y').strftime("%d/%m/%Y"), # lease start
                    dt.strptime(row[8], '%d %b %Y').strftime("%d/%m/%Y"), # lease end
                    int(row[9]),                                          # lease years
                    float(row[10]))                                       # current rent
                for row in reader]


    def get_sorted(self, by='current_rent', reverse=True, num=None):
        data_sorted = sorted(self.masts, key=attrgetter(by), reverse=reverse)
        if num: return data_sorted[:num]
        else: return data_sorted


    def get_total_rent_subset_by_lease_years(self, lease_years=25):
        subset = [
            mast for mast in self.masts if mast.lease_years == lease_years
        ]
        total_rent = sum(mast.current_rent for mast in subset)
        return subset, total_rent


    def get_rentals_by_lease_start(self, 
                                  date_min=dt(1999,6,1), 
                                  date_max=dt(2007,8,31)):
        return [
             mast for mast in self.masts if
             dt.strptime(mast.lease_start, '%d/%m/%Y') >= date_min and 
             dt.strptime(mast.lease_start, '%d/%m/%Y') <= date_max
            ]