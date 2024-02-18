class player:
    def __init__(self, data):
        self.player_name = data['player_name']
        self.player_weapons = data['inventory']['weapons']
        self.player_armor = data['inventory']['armor']
        self.player_consumables = data['inventory']['consumables']
        self.player_misc = data['inventory']['miscellaneous']
        self.player_spells = data['spells']
        self.player_skills = data['skills']

    def equip_item(self):
        pass