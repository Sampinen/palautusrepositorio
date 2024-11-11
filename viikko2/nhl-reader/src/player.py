class Player:
    def __init__(self, dict1,nationality):
        self.players = ""
        for player in dict1:
            if player["nationality"] == nationality:
                 self.players += f"\n{player["name"]} team {player["team"]}  goals {player["goals"]}  assists {player["assists"]}"
        self.nationality = nationality

    def __str__(self):
        print(f"Players from {self.nationality}\n\n")

        return self.players
