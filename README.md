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

1. Create a file with teams' names (csv format)

*Example*:

        УКУ1
        УКУ2
        УКУ3
        УКУ4
        УКУ5
        УКУ6
        УКУ7
        УКУ8
    
2. Create a file with games list (csv format: **winner,loser,score**)

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

3. Write a simple code:

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
4. graph_create function takes two arguments: filename_ranks (str), and filename_games (str).

    - filename_ranks - address of the file with teams' ranks. For the previous code it is **filename**
    variable.
    - filename_games - address of the file with teams' games. For the previous code it is **games_file** variable.

5. To see the visualization of optimized standings you need to run a command:

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
        
![photo_2024-12-01_18-27-19](https://github.com/user-attachments/assets/6b75bcd8-f36a-4594-b1af-348a7d229262)


## Pagerank Algorithm Reader
    This Python program reads and processes two types of CSV files to analyze game results and calculate player or team rankings. It is         part of a larger project implementing the Pagerank algorithm for sports or competitive standings.
1. Player Data Reading
The read_players function reads a list of players or teams from a file and initializes their scores to 0.

        Input: A CSV file with team/player names (one name per line).
        Output: A list of team/player names.
2. Game Data Reading
The read_games function parses game results from a CSV file, calculates the winner for each game, and formats the data.

        Input: A CSV file with columns: Player1, Player2, and Score (e.g., 3-1).
        Output: A list of tuples containing:
            Player1: Name of the first team.
            Player2: Name of the second team.
        Winner: Name of the winner (or 'tie' for draws).
        Score: Game score in X-Y format.
