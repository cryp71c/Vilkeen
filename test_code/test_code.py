"""
 Every 10 levels your exp needed for the next level will be 1000*level

level = 2
if (level%10)+1 == 0:
    exp_needed = level*1000
    print(exp_needed)
else:
    exp_needed = level*1000
    print(exp_needed)

"""

item = {"drop_chance": 0.00025}
times_killed = 100
base_drop_chance = item['drop_chance']
base_exp_chance = 3
player_level = 25
enemy_level = 3

player = {
    "name": "Emily",
    "class": "Warlock",
    "status": "Middle Class",
    "exp": 400,
    "level": 1,
}


def level_updater(exp, level):
    pass
    """
        if exp <= (level*1000):
            return(exp, level)
    """


def update_player(t_exp, ):
    pass


def exp_calc(bec, el, pl):
    exp_chance = bec + (el - pl) * (bec / pl)
    t_exp = (bec * exp_chance) * 10
    print("Player Level:", player_level, " Enemy Level:", enemy_level, ", Exp Chance:", exp_chance, " Total EXP:",
          t_exp)
    return t_exp


def drop_calc_enemy(bdc, el, pl, tk, t_exp):
    dc = (0.0005 * pl + bdc * el + t_exp * (tk * 0.01)) - 1
    print("Drop Chance: ", dc)
    return dc


drop_chance = drop_calc_enemy(base_drop_chance, enemy_level, player_level, times_killed,
                              exp_calc(base_exp_chance, enemy_level, player_level))
