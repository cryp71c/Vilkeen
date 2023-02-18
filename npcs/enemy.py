from main import enemy_table
class generate_enemy:
    def __init__(self, enemy_id):
        self.table = enemy_table.loc[enemy_id]
        self.id = enemy_id
        self.name = self.table.name
        self.type = self.table.type
        self.dead = self.table.dead
        self.lootable = self.table.lootable
        self.level = self.table.level
        self.weapon = self.table.weapon
        self.spells = self.table.spells
        self.effect = self.table.effect

