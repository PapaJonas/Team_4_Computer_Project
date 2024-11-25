"""League table"""

import pagerank_project.pagerank_algo as pagerank_algo
import pagerank_project.pagerank_read as pagerank_read
##################################################################################################

def main() -> None:
    """
    Main function to execute the tournament score processing.
    """
    players_file = 'teams.csv'
    games_file = 'games.csv'

    players = pagerank_read.read_players(players_file)
    results = pagerank_read.read_games(games_file)

    n = pagerank_algo.numb_of_players(players)
    connections = pagerank_algo.connect_list(players, results)
    rank = pagerank_algo.rank_return(n, connections)

    print(rank)
if __name__ == "__main__":
    main()
