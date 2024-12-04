'''A module of writing function'''
def write_function(filename, information, rank):
    """
    Records the ranking of the teams to a CSV file.

    Parameters:
        filename (str): The path of the CSV file where the data will be written.
        information (dict): Dictionary containing team data:
            - keys: Team names (strings).
            - values: A list with three elements:
                1. Number of points (int),
                2. Placeholder rank (int, initially set to 0),
                3. Number of games played (int).
        rank (list[float]): Numerical values representing the teams' ranks.

    Returns:
        None

    Example Usage:
    --------------
    rank = [29.47, 16.78, 14.93]
    information = {
        "team1": [5, 0, 3],
        "team2": [4, 0, 3],
        "team3": [4, 0, 3],
    }
    write_function("example.csv", information, rank)
    """
    ans = []
    for i, team_data in enumerate(information):
        ans.append([information[team_data][0], rank[i], information[team_data][2], team_data])

    def func(ans):
        return ans[0], ans[1]
    print(ans)
    sorted_information = sorted(ans, key = func, reverse = True)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("team,games,points,rank\n")

        for team_data in sorted_information:
            points, rank_value, games, team_name = team_data
            file.write(f"{team_name},{games},{points},{rank_value}\n")
