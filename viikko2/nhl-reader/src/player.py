class Player:
    def __init__(self, dict1,nationality):
        self.players = ""
        for player in dict1:
            if player["nationality"] == nationality:
                sum1 = str(player["goals"] + player["assists"])
                self.players += f"\n{player["name"]}    {player["team"]}  {player["goals"]} + {player["assists"]} = {sum1}"
        self.nationality = nationality

    def __str__(self):
        print(f"Players from {self.nationality}\n\n")

        return self.players
