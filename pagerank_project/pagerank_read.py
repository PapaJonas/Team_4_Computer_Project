"""Pagerank algorhytm reader. That reads 2 types of file: players and their games"""

import csv

def read_players(teams_file: str) -> dict[str, int]:
    """
    Reads a list of teams from a CSV file and initializes their scores to 0.

    Args:
        teams_file (str): Path to the CSV file containing team names.

    Returns:
        Dict[str, int]: A dictionary where keys are team names and\
        values are their scores (initialized to 0).
    """
    with open(teams_file, 'r', encoding='utf-8') as f:
        ans = []
        for line in f:
            ans.append(line.strip())
        return ans
##################################################################################################
def read_games(games_file: str) -> list[tuple[str, str, str, str]]:
    """
    Reads game results from a CSV file and determines the winner of each game.

    Args:
        games_file (str): Path to the CSV file containing game results.

    Returns:
        List[Tuple[str, str, str, str]]: A list of tuples, where each tuple contains:
            - player1 (str): Name of the first player/team.
            - player2 (str): Name of the second player/team.
            - winner (str): Name of the winner or 'tie' if the game was a draw.
            - score (str): The score of the game in the format 'X-Y'.
    """
    results = []
    with open(games_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            player1, player2, score = row
            score1, score2 = map(int, score.split('-'))

            if score1 > score2:
                winner = player1
            elif score2 > score1:
                winner = player2
            else:
                winner = 'tie'
            if (player1, player2, winner, score) not in results:
                results.append((player1, player2, winner, score))

    return results
##################################################################################################
def update_players(results: list[tuple[str, str, str , str]], players_dict: dict[str, int]) -> None:
    """
    Updates the scores of players/teams based on the game results.

    Args:
        results (List[Tuple[str, str, str, str]]): A list of tuples containing game results.
        players_dict (Dict[str, int]): A dictionary containing the current scores of players/teams.

    Modifies:
        players_dict: Updates the scores of the winners in the dictionary.
    """
    for _, _, winner, _ in results:
        if winner == 'tie':
            continue
        winner = winner.strip()
        if winner not in players_dict:
            players_dict[winner] = 0
        players_dict[winner] += 1
