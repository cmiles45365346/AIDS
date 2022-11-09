class player_inventory:
#review time: 1668128107.0732753
    def __init__(self):
        self.inventory = ["gold", 10] # Chose array because yes

#review time: 1668128107.0732753
    def open_player_inventory(self):
        print(self.inventory)
    
#review time: 1668128107.0732753
    def get_player_gold(self):
        print(self.inventory["gold"])


if __name__ != '__main__':
    player_inventory = player_inventory()
