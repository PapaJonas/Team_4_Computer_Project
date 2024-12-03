"""The main algorithm of PageRank, implemented for ranking players based on game results."""

import copy

##################################################################################################
def connect_list(players: list[str], results: list[str, str, str, str]) -> list:
    """ Generate a list of connections representing game outcomes.

    Args:
        players (list[str]): A list of player names.
        results (list[list[str, str, str, str]]): 
        A list of game results, where each result contains:
            [team_1, team_2, winner, _] 
            - team_1 (str): Name of the first team.
            - team_2 (str): Name of the second team.
            - winner (str): Name of the winning team or 'tie'.
            - _ (str): Placeholder for additional data.

    Returns:
        list[list[int]]: A list of connections where each connection is a pair [loser, winner].
            For ties, both directions are included."""

    connections = []
    for game in results:
        team_1, team_2, winner, _ = game
        flag = 0
        if winner == team_1:
            flag = 1
        team_1 = players.index(team_1)
        team_2 = players.index(team_2)
        if winner == 'tie':
            connections.append([team_1, team_2, 'd'])
            connections.append([team_2, team_1, 'd'])
        elif flag:
            connections.append([team_2, team_1, 'w'])
        else:
            connections.append([team_1, team_2, 'w'])
    return connections
##################################################################################################
def rank_return(n: int, connections: list[list], damping: float) -> list[float]:

    """Calculate the PageRank of players based on game connections.

    Args:
        n (int): The number of players.
        connections (list[list[int]]): 
        A list of connections where each connection is a pair [loser, winner].
        demping: The number of probability of visiting random edge from 0 to 1

    Returns:
        list[float]: 
        A list of PageRank values, rounded to two decimal places, 
        representing the rank of each player.
    """
    matr = [[0]*n for _ in range(n)]
    rank = [100/n] * n
    damp_const = damping * 100 / n
    counter_from = [0]*n
    for el in connections:
        i, j, result = el
        if result == 'w':
            counter_from[i] += 1
            matr[j][i] = 1
        elif result == 'd':
            counter_from[i] += 0.5
            matr[j][i] = 0.5
    for i, mas in enumerate(matr):
        masa = []
        for j, el in enumerate(mas):
            if el:
                masa.append(el/counter_from[j])
            else:
                masa.append(0)
        matr[i] = masa
    for _ in range(50):
        rank_cop = copy.copy(rank)
        for i in range(n):
            rank[i] = sum(rank_cop[j]*el for j, el in enumerate(matr[i]))
        summ_r = sum(rank)
        rank = [(100 - damp_const * n)*el/summ_r + damp_const for el in rank]
    rank = [round(el, 2) for el in rank]
    return rank
