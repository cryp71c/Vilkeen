import json

import pandas as pd

pd.set_option('display.max_columns', None)

#pd.options.mode.chained_assignment = None  # default='warn'
import os
import random

code_path = -1

debug = True

player_table = pd.read_excel(f"data_table.xlsx", sheet_name="player", index_col="id")
weapons_table = pd.read_excel(f"data_table.xlsx", sheet_name="weapons", index_col="id")
enchants_table = pd.read_excel(f"data_table.xlsx", sheet_name="enchants", index_col="id")
armor_table = pd.read_excel(f"data_table.xlsx", sheet_name="armor", index_col="id")
spells_table = pd.read_excel(f"data_table.xlsx", sheet_name="spells", index_col="id")
effects_table = pd.read_excel(f"data_table.xlsx", sheet_name="effects", index_col="id")
chest_table = pd.read_excel(f"data_table.xlsx", sheet_name="chest", index_col="id")
enemy_table = pd.read_excel(f"data_table.xlsx", sheet_name="enemies", index_col="id")
boss_table = pd.read_excel(f"data_table.xlsx", sheet_name="bosses", index_col="id")
locations_table = pd.read_excel(f"data_table.xlsx", sheet_name="locations", index_col="id")


def enemy_generator():
    from npcs import enemy
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
    # enemy_generator()

    save = 1

    inventory = json.loads(player_table['inventory'][save])
    print(inventory)
    print("----------")

    inventory['weapons'] = [1]

    print(inventory)
    print("----------")

    player_table.at[save, 'inventory'] = inventory

    print(player_table)
    print("----------")


if __name__ == '__main__':
    main()
