# Team_4_Computer_Project

## Project's topic

    - Optimized standings 

## Project's main tasks

    - Create an optimized standing by utilizing PageRank algorithm, and represent it in directed network-graph form.

## Project's realisation parts

    - pagerank_read
    - pagerank_algo
    - pagerank_write
    - pagerank_cli
    - visualize
    - main
## Command line inteface

    - This part consists of pagerank_cli function
    - pagerank_cli creates a Command-Line Interface (CLI) using the argparse library. CLI is an application that interacts with users through a terminal. Users input commands and parameters, and the program processes these inputs and returns outputs.
step-by-step breakdown

1.Importing argparse
      The argparse library is imported to handle command-line arguments.
      
2.Defining function

3.Creating Argument Parser
      An ArgumentParser object is created to process command-line arguments.

4.Adding Arguments

--players (-p): Specifies the file containing player data.
--games (-g): Specifies the file containing game data.
--results (-r): Specifies the output file for results.
--win (-w): Specifies the points awarded for a win (integer).
--draw (-dr): Specifies the points awarded for a draw (integer).
--damping (-dmp): Specifies the damping factor for the algorithm (float).

5.Parse Arguments:
     parser.parse_args() reads and processes the command-line inputs.

6.Return Values:
     The function returns a list of parsed argument values:
     [args.players, args.games, args.results, args.win, args.draw, args.damping]

Example Usage:

   - python main.py -p ../teams.txt -g ../games.txt -r ../example.txt -w 3 -dr 1 -dmp 0.85
     (make sure you are in the right directiory)
it will:
     Collect and parse the provided arguments:
     Return them as a list
     ``` python
     ["players.txt", "games.txt", "results.txt", 3, 1, 0.85]



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
![photo_2024-12-03_23-10-38](https://github.com/user-attachments/assets/ea456974-6b73-4a3f-888e-0c594f8740ac)

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
# PageRank Algorithm Implementation

This document outlines the implementation of the PageRank algorithm (`pagerank_algo`) for ranking players or teams based on game results. The algorithm transforms game outcomes into directed connections and computes rankings through iterative calculations.

---

## 1. Connection List Generation

The `connect_list` function generates a list of directed connections based on game results.

### **Inputs**
- **`players`**: A list of player/team names.
- **`results`**: A list of game results, where each result includes:
  - `team_1`: Name of the first team.
  - `team_2`: Name of the second team.
  - `winner`: Name of the winning team or `"tie"` for draws.
  - `_`: Placeholder for additional metadata.

### **Outputs**
- **`connections`**: A list of directed connections:
  - `[loser, winner, 'w']` for wins.
  - `[loser, winner, 'd']` and `[winner, loser, 'd']` for ties.

### **Code**
```python
def connect_list(players: list[str], results: list[list[str, str, str, str]]) -> list[list[int]]:
    """Generate a list of connections representing game outcomes.

    Args:
        players (list[str]): List of player names.
        results (list[list[str, str, str, str]]): Game results [team_1, team_2, winner, _].
        
    Returns:
        list[list[int]]: Directed connections [loser, winner, result].
    """
    connections = []
    for game in results:
        team_1, team_2, winner, _ = game
        team_1_idx = players.index(team_1)
        team_2_idx = players.index(team_2)
        if winner == 'tie':
            connections.append([team_1_idx, team_2_idx, 'd'])
            connections.append([team_2_idx, team_1_idx, 'd'])
        elif winner == team_1:
            connections.append([team_2_idx, team_1_idx, 'w'])
        else:
            connections.append([team_1_idx, team_2_idx, 'w'])
    return connections
```

---

## 2. PageRank Calculation

The `rank_return` function calculates player or team rankings using the PageRank algorithm.

### **Inputs**
- **`n`**: The number of players/teams.
- **`connections`**: The directed connections generated by `connect_list`.
- **`damping`**: The damping factor (0–1) defining the probability of random transitions.

### **Outputs**
- A list of PageRank values for each player/team, normalized to percentages and rounded to two decimals.

### **Code**
```python
def rank_return(n: int, connections: list[list[int]], damping: float) -> list[float]:
    """Calculate PageRank values for players based on connections.

    Args:
        n (int): Number of players.
        connections (list[list[int]]): Directed game connections [loser, winner, result].
        damping (float): Probability of random transition (0–1).

    Returns:
        list[float]: Normalized PageRank values for each player/team.
    """
    import copy

    # Initialize adjacency matrix and rank
    matr = [[0] * n for _ in range(n)]
    rank = [100 / n] * n
    damp_const = damping * 100 / n
    counter_from = [0] * n

    # Build adjacency matrix
    for i, j, result in connections:
        if result == 'w':
            counter_from[i] += 1
            matr[j][i] = 1
        elif result == 'd':
            counter_from[i] += 0.5
            matr[j][i] = 0.5

    # Normalize adjacency matrix
    for i, mas in enumerate(matr):
        matr[i] = [el / counter_from[j] if el else 0 for j, el in enumerate(mas)]

    # Iterative rank calculation
    for _ in range(50):
        rank_cop = copy.copy(rank)
        for i in range(n):
            rank[i] = sum(rank_cop[j] * el for j, el in enumerate(matr[i]))
        summ_r = sum(rank)
        rank = [(100 - damp_const * n) * el / summ_r + damp_const for el in rank]

    return [round(el, 2) for el in rank]
```

---

## Example Usage

### **Code**
```python
players = ["TeamA", "TeamB", "TeamC"]
results = [
    ("TeamA", "TeamB", "TeamA", ""),
    ("TeamB", "TeamC", "tie", ""),
    ("TeamC", "TeamA", "TeamC", ""),
]

# Step 1: Generate connections
connections = connect_list(players, results)

# Step 2: Calculate rankings
ranks = rank_return(n=len(players), connections=connections, damping=0.85)

print("Player Rankings:", ranks)
```

### **Output**
```
Player Rankings: [34.78, 32.61, 32.61]
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
