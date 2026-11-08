from classes.tar1 import Player


#tar1
players = [Player("Dana"), Player("Avi"), Player("Noa")]
players[0].add_points(50)
players[1].add_points(15)
players[2].add_points(40)
highest_points = 0
winning_name = None
for player in players:
    if player.get_points() > highest_points:
        winning_name = player.name
print(winning_name)
