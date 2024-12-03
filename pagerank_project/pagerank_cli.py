'''cli'''
import argparse

def cli():
    '''
    interracts with user through console
    returns file with players, with games and output file
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--players", type=str, help="write the name of the file with players")
    parser.add_argument("-g", "--games", type=str, help="write the name of the file with games")
    parser.add_argument("-r", "--results", type=str, help="write the name of the output file")
    parser.add_argument("-w", "--win", type=int, help="write how much points player will get for the win")
    parser.add_argument("-dr", "--draw", type=int, help="write how much points player will get for the draw")
    parser.add_argument("-dmp", "--damping", type=float, help="write how much points will be damped by algorithm")

    args = parser.parse_args()
    return [args.players, args.games, args.results, args.win, args.draw, args.damping]
