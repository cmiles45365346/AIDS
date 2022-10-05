class player_inventory:
    def __init__(self):
        self.inventory = ["gold", 10] # Chose array because yes

    def open_player_inventory(self):
        print(self.inventory)
    
    def get_player_gold(self):
        print(self.inventory["gold"])


if __name__ != '__main__':
    player_inventory = player_inventory()
