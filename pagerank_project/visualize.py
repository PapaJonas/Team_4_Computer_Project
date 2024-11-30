"""
This code is responisble for visualization task.
"""
def graph_create(filename_results: str, filename_games: str) -> None:
    """
    This function visualizes tournament table in a
    graph form. The data it takes should be written
    in a file with path (filename). Data is represented
    in form:

    team,points,rank
    ----------------------------------------------------
    param: filename (str) - name of the file with data.
    """
    import networkx as nx
    import matplotlib.pyplot as plt
    from random import choice

    with open(filename_results, mode='r', encoding='utf-8') as file:
        content = file.readlines()[1:]
        results = {el.strip().split(',')[0]: float(el.strip().split(',')[2]) for el in content}

    teams = results.keys()
    ranks = [value * 250 if value != 0.0 else 1200 for value in results.values()]
    colors = ["#66ff66", "#ffccff", "#ffcc99", "#cce5ff", "#ffff99", "#00af3a", "#ffbb30", "#d41b6b"]
    colors_to_choose = [choice(colors) for i in range(len(teams))]

    G = nx.DiGraph()
    G.add_nodes_from(results.keys())

    for team, rank in results.items():
        G.nodes[team]['rank'] = rank

    node_labels = {key: f"{key}\n{results[key]}" for key in teams}

    with open(filename_games, mode='r', encoding='utf-8') as file:
        content = file.readlines()[1:]
        to_check = content.copy()
        for el in to_check:
            if len(set(el.strip().split(',')[2])) == 2:
                content.append(','.join([el.strip().split(',')[1], el.strip().split(',')[0]]))
        games = [(el.strip().split(',')[0], el.strip().split(',')[1]) for el in content]

    G.add_edges_from(games)

    nx.draw(G, pos=nx.circular_layout(G), arrows = True, arrowsize = 15, node_color=colors_to_choose, node_size=ranks, with_labels=True, labels=node_labels, font_family="Times New Roman", font_color='black', font_size = 11)

    plt.margins(0.1)
    plt.show()