import random

class Human:
    def __init__(self,name):
        self.name=name

class Footballer(Human):
    def __init__(self,name,team=None):
        self.team=team
        super().__init__(name)

    def assign_team(self, team_name):
        """Assigns a player to a team"""
        self.team = team_name

# List of 22 player names
players_names = [
    "حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی", 
    "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"
]

# Create 22 Footballer objects
# way 1
# players=[]
# for name in players_names:
#     players.append(Footballer(name))

# way 2
players = [Footballer(name) for name in players_names]

# Shuffle the players randomly
random.shuffle(players)

# Assign players to teams (first 11 → Team A, rest → Team B)
team_A = players[:11]
team_B = players[11:]  


# Print the teams
print("🏆 Team A:")
for player in team_A:
    player.assign_team("A") # first assign player to team then print player name
    # print(f"{player.name} - Team {player.team}")
    print(f"{player.name}")

print("\n🏆 Team B:")
for player in team_B:
    player.assign_team("B")
    # print(f"{player.name} - Team {player.team}")
    print(f"{player.name}")