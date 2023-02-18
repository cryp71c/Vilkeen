import pandas as pd
import random
from npcs import enemy

debug = True

weapons_table = pd.read_excel("data_table.xlsx", sheet_name="weapons", index_col="id")
armor_table = pd.read_excel("data_table.xlsx", sheet_name="armor", index_col="id")
enchants_table = pd.read_excel("data_table.xlsx", sheet_name="enchants", index_col="id")
spells_table = pd.read_excel("data_table.xlsx", sheet_name="spells", index_col="id")
effects_table = pd.read_excel("data_table.xlsx", sheet_name="effects", index_col="id")
enemy_table = pd.read_excel("data_table.xlsx", sheet_name="enemies", index_col="id")


def enemy_generator():
    random_enemy = enemy.generate_enemy(enemy_id=1)
    print(random_enemy.type)


def get_weapon_by_id(item_id):
    return weapons_table.loc[[item_id]]


def get_armor_by_id(item_id):
    return armor_table.loc[[item_id]]


def populate_enemy_loot(enemy_level, drop_chance, player_level, times_killed_enemy):
    pass


def populate_chest_loot(location_id, enemy_id, enemy_level):
    pass


def print_table():
    tables = [weapons_table, armor_table, enchants_table, spells_table, effects_table]
    for i in tables:
        print(i)


def main():
    enemy_generator()


if __name__ == '__main__':
    main()