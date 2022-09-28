class PlayerInventory:
    def __init__(self):
        self.inventory = [0]

    def open_inventory(self):
        print(PlayerInventory.inventory)


if __name__ == '__main__':
    exit(0)
else:
    PlayerInventory = PlayerInventory()
