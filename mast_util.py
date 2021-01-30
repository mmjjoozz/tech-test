import csv
from mast import Mast
from operator import attrgetter
from datetime import datetime as dt
import pprint

pp = pprint.PrettyPrinter(indent=1, sort_dicts=False)

class MastUtil():
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
                    self._normalize(row[6]),                              # tenant name
                    dt.strptime(row[7], '%d %b %Y').strftime("%d/%m/%Y"), # lease start
                    dt.strptime(row[8], '%d %b %Y').strftime("%d/%m/%Y"), # lease end
                    int(row[9]),                                          # lease years
                    float(row[10]))                                       # current rent
                for row in reader]


    def _normalize(self, name):
        if 'Ever' in name and '3G' not in name:
            return 'Everything Everywhere Ltd.'
        elif 'Ever' in name and '3G' in name:
            return 'Everything Everywhere & Hutchinson 3G UK Ltd.'
        elif 'Corn' in name:
            return 'Cornerstone Telecommunications Infrastructure'
        elif 'Arq' in name:
            return 'Arqiva Ltd.'
        elif 'Voda' in name:
            return 'Vodafone Ltd.'
        elif 'O2' in name:
            return 'O2 (UK) Ltd.'
        else:
            return name
        

    def print_sorted(self, by='current_rent', reverse=False, num=5):
        data_sorted = sorted(self.masts, key=attrgetter(by), reverse=reverse)
        if num:
            data_sorted = data_sorted[:num]

        for data_point in data_sorted: pp.pprint(data_point.__dict__)


    def print_total_rent_subset_by_lease_years(self, lease_years=25):
        total_rent = 0
        subset = [
            mast for mast in self.masts if mast.lease_years == lease_years
        ]
        if subset: total_rent = sum(mast.current_rent for mast in subset)

        for data_point in subset: pp.pprint(data_point.__dict__)
        print("Total Rent: ", total_rent)


    def print_masts_by_tenant(self):
        counts = {}
        for mast in self.masts:
            if mast.tenant_name in counts:
                counts[mast.tenant_name] += 1
            else:
                counts[mast.tenant_name] = 1

        pp.pprint(counts)


    def print_rentals_by_lease_start(self, 
                                  date_min=dt(1999,6,1), 
                                  date_max=dt(2007,8,31)):
        rentals = [
             mast for mast in self.masts if
             dt.strptime(mast.lease_start, '%d/%m/%Y') >= date_min and 
             dt.strptime(mast.lease_start, '%d/%m/%Y') <= date_max
            ]

        for data_point in rentals: pp.pprint(data_point.__dict__)