"""Pagerank algorhytm reader. That reads 2 types of file: players and their games"""

import csv

def read_players(teams_file: str) -> list[str]:
    """
    Reads a list of teams from a CSV file and initializes their scores to 0.

    Args:
        teams_file (str): Path to the CSV file containing team names.

    Returns:
        List[str]: A list of team names as strings.
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
def update_players(results: list[tuple[str, str, str , str]], players_list: list[str], pts_per_win: int, pts_per_draw: int) -> dict[str, list[int]]:
    """
    Updates player or team scores based on game results.

    Args:
        results (list[tuple[str, str, str, str]]): 
            A list of tuples representing game results. 
            Each tuple contains:
            - `team_1` (str): Name of the first team/player.
            - `team_2` (str): Name of the second team/player.
            - `winner` (str): Name of the winner or 'tie' if the game was a draw.
            - `score` (str): The score of the game (e.g., 'X-Y').

        players_list (list[str]): A list of all team/player names.

        pts_per_win (int): Points awarded for a win.

        pts_per_draw (int): Points awarded to each team/player in the event of a draw.

    Returns:
        dict[str, list[int]]: 
            A dictionary where:
            - Keys are team/player names.
            - Values are lists containing:
              1. Total points (int).
              2. Reserved for future use (int, default 0).
              3. Number of games played (int).

    Notes:
        - If the `winner` is `'tie'`, both teams are awarded points for a draw.
        - Whitespace around `winner` names is stripped before processing.
        - The `players_dict` is initialized with all players having `[0, 0, 0]` 
          for points, reserved space, and games played, respectively.
    """
    players_dict = {player : [0, 0, 0] for player in players_list}
    for team_1, team_2, winner, _ in results:
        players_dict[team_1][2] += 1
        players_dict[team_2][2] += 1
        if winner == 'tie':
            players_dict[team_1][0] += pts_per_draw
            players_dict[team_2][0] += pts_per_draw
            continue
        winner = winner.strip()
        players_dict[winner][0] += pts_per_win
    return players_dict
