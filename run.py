from mast_list import MastList

def main():
    l = MastList("data/Python Developer Test Dataset.csv")
    for mast in l.masts:
        print(mast.__dict__)


if __name__ == "__main__":
    main()