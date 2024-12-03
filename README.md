# Team_5_Computer_Project

## Project's topic

    - Optimized standings 

## Project's main tasks

    - Create an optimized standing by utilizing PageRank algorithm, and represent it in directed network-graph form.

## Project's realisation parts

    - pagerank_write
    - pagerank_read
    - pagerank_algo
    - visualize
    - main

## Visualize part

    - This part consists of graph_create function.
    - graph_create function builds a network-graph representation utilizing NetworkX tools.

To create a graph with graph_create function several steps should be done in advance:
1. Install matplotlib and networkx libraries:
    ``` python
    pip install matplotlib
    pip install networkx
    ```
2. Create a file with teams' names (csv format)

*Example*:

        УКУ1
        УКУ2
        УКУ3
        УКУ4
        УКУ5
        УКУ6
        УКУ7
        УКУ8
    
3. Create a file with games list (csv format: **winner,loser,score**)

*Example*:

        УКУ1,УКУ2,3-1
        УКУ3,УКУ4,2-2
        УКУ5,УКУ6,1-0
        УКУ7,УКУ8,0-3
        УКУ1,УКУ5,2-2
        УКУ2,УКУ6,1-0
        УКУ4,УКУ7,2-1
        УКУ8,УКУ3,1-4
        УКУ1,УКУ4,0-1
        УКУ5,УКУ7,3-1
        УКУ6,УКУ8,2-3
        УКУ2,УКУ3,1-1

4. Write a simple code:

```python

import pagerank_read
import pagerank_algo
import pagerank_write
import visualize

players_file = 'teams.csv'
games_file = 'games.csv'
filename = 'example.csv'
players = pagerank_read.read_players(players_file)
results = pagerank_read.read_games(games_file)
information = pagerank_read.update_players(results, players)

n = pagerank_algo.numb_of_players(players)
connections = pagerank_algo.connect_list(players, results)
rank = pagerank_algo.rank_return(n, connections)
pagerank_write.write_function(filename, information, rank)
```
5. graph_create function takes two arguments: filename_ranks (str), and filename_games (str).

    - filename_ranks - address of the file with teams' ranks. For the previous code it is **filename**
    variable.
    - filename_games - address of the file with teams' games. For the previous code it is **games_file** variable.

6. To see the visualization of optimized standings you need to run a command:

    ``` python
    visualize.graph_create(filename, games_file)
    ```

## graph_create function working principles

    - graph_create function shows an optimized stangings in the form of network-graph.
    - graph_create function utilizes NetworkX tools.
    - graph_create function creates a network-graph, where:
        1. nodes are marked as a team's name and it's rank
        2. node's size depends on team's rank
        3. nodes are connected with directed edges.
        4. edge's direction is derived by (**winner** -> **loser**) or (<->) if the game result is *tie*.


## Pagerank Algorithm Reader
    This Python program reads and processes two types of CSV files to analyze game results and calculate player or team rankings. It is         part of a larger project implementing the Pagerank algorithm for sports or competitive standings.
1. Player Data Reading
The read_players function reads a list of players or teams from a file and initializes their scores to 0.

        Input: A CSV file with team/player names (one name per line).
        Output: A list of team/player names.
Code:
```
def read_players(teams_file: str) -> dict[str, int]:
    with open(teams_file, 'r', encoding='utf-8') as f:
        ans = []
        for line in f:
            ans.append(line.strip())
        return ans
```
2. Game Data Reading
The read_games function parses game results from a CSV file, calculates the winner for each game, and formats the data.

        Input: A CSV file with columns: Player1, Player2, and Score (e.g., 3-1).
        Output: A list of tuples containing:
            Player1: Name of the first team.
            Player2: Name of the second team.
        Winner: Name of the winner (or 'tie' for draws).
        Score: Game score in X-Y format.

   Code:
   ```
   def read_games(games_file: str) -> list[tuple[str, str, str, str]]:
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
   ```
3. Player Score Updates
The update_players function calculates rankings based on game results.

    Input:
    Game results (output of read_games).
    Player list (output of read_players).
    Points awarded for a win and a draw.
    Output: A dictionary with player/team names as keys and a list as values:
    [score, reserved, games_played].

   
Code:
```
def update_players(results: list[tuple[str, str, str , str]], players_dict: dict[str, int], win_points: int) -> None:
    for _, _, winner, _ in results:
        if winner == 'tie':
            continue
        winner = winner.strip()
        if winner not in players_dict:
            players_dict[winner] = 0
        players_dict[winner] += win_points
    for player1, player2, winner, _ in results:
        if winner == 'tie':
            if player1 not in players_dict:
                players_dict[player1] = 0
            if player2 not in players_dict:
                players_dict[player2] = 0
            players_dict[player1] += win_points
            players_dict[player2] += win_points
```
4. Code Example
```
teams_file = "teams.csv"
games_file = "games.csv"

# Step 1: Read players
players = read_players(teams_file)

# Step 2: Read game results
results = read_games(games_file)

# Step 3: Update player scores
updated_scores = update_players(results, players, pts_per_win=3, pts_per_draw=1)

print(updated_scores)
```

## Pagerank writing part
    - The pagerank_write module is responsible for saving the optimized results generated by the PageRank algorithm into a CSV file.
    - The pagerank_write function  writes team data, including points, games played, and ranks, into a CSV file. It ensures the data is sorted by team points in descending order for better readability and further processing.

The function’s parameters:
    - filename (str): The path to the CSV file where results will be written.
    - information (dict): A dictionary containing team data:
        - keys: Team names (strings).
        - values: A list with three elements (number of points (int), rank (initially set to 0 or any value, later updated from the rank list), number of games played (int))
    - rank (list[float]): A list of ranks corresponding to the order of the teams in the information dictionary. These are numerical scores (e.g., PageRank values).
Returns: None

Output:
    - The function generates a CSV file where the teams are sorted by points in descending order. 

Example of CSV File Format:

```
team,games,points,rank
team1,3,5,29.47
team2,3,4,16.78
team3,3,4,14.93
```

Example Usage:

```python
import pagerank_write

rank = [29.47, 16.78, 14.93]
information = {"team1": [5, 0, 3], "team2": [4, 0, 3], "team3": [4, 0, 3]}

pagerank_write.write_function("example.csv", information, rank)
```

### pagerank_write function working principles:

1. Input Data:
    - Accepts a dictionary where keys are team names, and values are lists containing points, rank, and games played.
    - Takes a separate list of ranks (rank) with numerical values.
2. Data Processing:
    - Iterates over the dictionary and updates the placeholder rank (`0`) for each team with the corresponding value from the `rank` list.
    - Forms a list for each team in the format `[points, rank, games, team]` and compiles these into a master list.
3. Sorting:
    - Sorts the master list by points in descending order, ensuring teams with higher scores appear first.
4. CSV File Creation:
    - Writes the sorted team data into a CSV file with the following headers: team, games, points, rank.