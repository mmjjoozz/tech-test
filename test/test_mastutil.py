import unittest
from mast.mast_util import MastUtil
from datetime import datetime as dt

class TestMastUtil(unittest.TestCase):
    def setUp(self):
        self.doc_len = 43
        self.mast_util = MastUtil('../data/Python Developer Test Dataset.csv')
    
    def test_all_csv_lines_parsed(self):
        self.assertEqual(len(self.mast_util.masts), self.doc_len-1)
    
    def test_gets_first_5_ascending(self):
        first_5 = self.mast_util.print_sorted(num=5)

        # test gets 5 if num arg provided
        self.assertEqual(len(first_5), 5)

        # test ascending order
        self.assertGreater(first_5[1].current_rent, first_5[0].current_rent)
    
    def test_gets_lease_years_total_rent(self):
        lease_25, total_rent = self.mast_util.print_total_rent_subset_by_lease_years()

        for lease in lease_25:
            self.assertEqual(lease.lease_years, 25)
        self.assertEqual(total_rent, 46500)
    
    def test_count_masts_per_tenant(self):
        counts = {'Arqiva Ltd.': 2,
                  'Vodafone Ltd.': 2,
                  'O2 (UK) Ltd.': 1,
                  'Everything Everywhere & Hutchinson 3G UK Ltd.': 17,
                  'Everything Everywhere Ltd.': 4,
                  'Cornerstone Telecommunications Infrastructure': 16}
                  
        self.assertEquals(
            self.mast_util.print_masts_by_tenant(), counts
        )

    def test_rentals_between_june_1999_aug_2007(self):
        rentals = self.mast_util.print_rentals_by_lease_start()

        self.assertGreaterEqual(
            dt.strptime(rentals[0].lease_start, '%d/%m/%Y'),
            dt(1999,6,1)
        )
        self.assertLessEqual(
            dt.strptime(rentals[-1].lease_start, '%d/%m/%Y'),
            dt(2007,8,31)
        )
    



    
    


    