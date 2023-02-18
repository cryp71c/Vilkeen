base_exp_chance = 3
player_level = 1
enemy_level = 20

"""
 Every 10 levels your exp needed for the next level will be 1000*level


"""
level = 2
if (level%10)+1 == 0:
    exp_needed = level*1000
    print(exp_needed)
else:
    exp_needed = level*1000
    print(exp_needed)
# TODO:
#   Level Cap Lower Level Mobs
#
#

# while player_level < 100:
#     exp_chance = base_exp_chance + (enemy_level - player_level) * (base_exp_chance/player_level)
#     total_exp = (base_exp_chance*exp_chance)*10
#     print("Player Level: ", player_level,", Exp Chance:", exp_chance, " Total EXP:", total_exp)
#     player_level+=1


