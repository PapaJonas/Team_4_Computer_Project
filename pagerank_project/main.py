"""League table"""

import pagerank_read
import pagerank_algo
import pagerank_write
import pagerank_cli

##################################################################################################

def main() -> None:
    """
    Main function to execute the tournament score processing.
    """
    # players_file = 'teams.csv'
    # games_file = 'games.csv'
    # filename = 'example.csv'
    players_file, games_file, filename = pagerank_cli.cli()
    players = pagerank_read.read_players(players_file)
    results = pagerank_read.read_games(games_file)
    information = pagerank_read.update_players(results, players)

    n = pagerank_algo.numb_of_players(players)
    connections = pagerank_algo.connect_list(players, results)
    rank = pagerank_algo.rank_return(n, connections)

    pagerank_write.write_function(filename, information, rank)
if __name__ == "__main__":
    main()
