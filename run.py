import argparse
from mast.mast_util import MastUtil


argparser = argparse.ArgumentParser()


PATH = "data/Python Developer Test Dataset.csv"
mast_util = MastUtil(PATH)


argparser.add_argument('--task1',
                       help='Print first 5 current rents in ascending order.',
                       action='store_true')
argparser.add_argument('--task2',
                       help='Print a list of of mast data with "Lease=25".',
                       action='store_true')
argparser.add_argument('--task3',
                       help='Print a dictionary with number of mast data points per tenant.',
                       action='store_true')
argparser.add_argument('--task4',
                       help='Print all rentals with start dates between June 1 1999 and Aug 31 2007',
                       action='store_true')


args = argparser.parse_args()


cmd = [k for k, v in vars(args).items() if v is True]
cmd_dict = {
    'task1': mast_util.print_sorted,
    'task2': mast_util.print_total_rent_subset_by_lease_years,
    'task3': mast_util.print_masts_by_tenant,
    'task4': mast_util.print_rentals_by_lease_start
}

# if no args provided, run all tasks defined in cmd_dict
if not cmd: cmd = cmd_dict.keys()
for arg in cmd:
    print("\n===== {} =====".format(arg))
    cmd_dict[arg]()