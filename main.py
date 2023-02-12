import pandas as pd

debug = True


# TODO:
# finish loot tables
#
#
#
#

def print_table(*tables):
    for i in tables:
        print(i)


def main():
    if debug:
        print("[*] In Main")

    weapons_table = pd.read_excel("data_table.xlsx", sheet_name="weapons", index_col="id")
    armor_table = pd.read_excel("data_table.xlsx", sheet_name="armor", index_col="id")
    enchants_table = pd.read_excel("data_table.xlsx", sheet_name="enchants", index_col="id")
    spells_table = pd.read_excel("data_table.xlsx", sheet_name="spells", index_col="id")
    effects_table = pd.read_excel("data_table.xlsx", sheet_name="effects", index_col="id")


if __name__ == '__main__':
    main()
