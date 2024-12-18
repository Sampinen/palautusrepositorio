from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print(f"/n testi")
    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)
    print(f"/n testi2")
    matcher = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


    print(f"/n testi3")
    matcher = Or(
    HasAtLeast(45, "goals"),
    HasAtLeast(70, "assists")
    )


    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
