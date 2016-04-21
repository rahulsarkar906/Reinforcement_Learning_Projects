import pdb
from ttt import Board
from agent import Agent
from RandomPlayer import RandomPlayer
from user_tokens import UserTokens as user
from helper import Helper



def play_game(a1, a2):
    board = Board()
    players = [a1,a2]
    turns = 0

    while board.game_status() is user.available:
        player = players[turns % 2]
        board.take_space(player.token, player.next_move(board))
        turns += 1

    return board


def play_games(a1, a2, count, verbose=False):

    stats = {
        user.X: 0,
        user.O: 0,
        user.draw: 0
    }

    for i in range(count):
        board = play_game(a1,a2)

        stats[board.game_status()] += 1

        if verbose:
            print(board.print_board())
            print("\n\n")

    return stats

a1 = Agent(user.X)
a2 = RandomPlayer(user.O)
a3 = Agent(user.O)
stats = play_games(a1,a2, 1000)

print("X: {}".format(stats[user.X]))
print("O: {}".format(stats[user.O]))
print("D: {}".format(stats[user.draw]))

stats = play_games(a1,a3, 500)

print("X: {}".format(stats[user.X]))
print("O: {}".format(stats[user.O]))
print("D: {}".format(stats[user.draw]))


pdb.set_trace()
