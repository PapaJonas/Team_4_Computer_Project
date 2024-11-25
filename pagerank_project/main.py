"""League table"""

import pagerank_read

def main() -> None:
    """
    Main function to execute the tournament score processing.
    """
    players_file = 'teams.csv'
    games_file = 'games.csv'

    players = pagerank_read.read_players(players_file)
    results = pagerank_read.read_games(games_file)

if __name__ == "__main__":
    main()