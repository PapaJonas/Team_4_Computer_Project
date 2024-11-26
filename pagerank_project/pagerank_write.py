'''A module of wruting function'''
def write_function(filename, information, rank):
    """
    Records the ranking of the teams to a CSV file.
    The function accepts a filename and a list of dictionaries,
    where each dictionary represents a team.
    Each dictionary contains:
        - A single key: the team name (string).
        - A value: a list with two elements (number of points and rank of the team).
    The function sorts the teams by points in descending order and 
    writes the sorted data to a CSV file
    Parameters:
        filename : str, the path of the CSV file where the data will be written.
        information dict, dictionary containing team information.
        rank (list[int]): List of ranks for the teams.

    Return:
        None

    Example Usage:
    --------------
    rank = [15, 10, 5]
    information = {"team1": [99, 200], "team2": [50, 50]}, "team3": [50, 40]}
    write_function("example.csv", information, rank)
    """
    ans = []
    for i, team_data in enumerate(information):
        ans.append([information[team_data][0], rank[i], team_data])
    def func(ans):
        return [ans[0], ans[1]]
    sorted_information = sorted(ans, key = func, reverse = True)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("team,points,rank\n")
        for team_data in sorted_information:
            points, rank_value, team_name = team_data
            file.write(f"{team_name},{points},{rank_value}\n")
