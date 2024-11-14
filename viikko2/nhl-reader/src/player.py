import requests
from rich.console import Console
from rich.table import Table

console = Console()
class Player:
    player_table = Table(show_header=True, header_style="bold magenta")
    player_table.add_column("Name")
    player_table.add_column("Team")
    def __init__(self, dict1,nationality):
        self.players = []
        for player in dict1:
            if player["nationality"] == nationality:
                sum1 = str(player["goals"] + player["assists"])
                self.players.append(f"{player["name"]}    {player["team"]}  {player["goals"]} + {player["assists"]} = {sum1}") 
        self.nationality = nationality


    def playerlist(self):

        return [f"Players from {self.nationality}\n\n"]+ self.players

class PlayerReader:
    def __init__(self,url):
        self.url = url
    def return_list(self):
        return requests.get(self.url).json()

class PlayerStats:
    def __init__(self,reader):
        self.players = reader
    def top_scorers_by_nationality(self,nationality):
        players = Player(self.players,nationality)
        return players.playerlist()
