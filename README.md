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

