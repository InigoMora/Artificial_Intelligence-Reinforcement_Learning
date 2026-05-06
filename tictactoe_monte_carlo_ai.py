import tictactoe
import random
import math

# From Justin's video

def get_open_spots(curr_board : [int]) -> [int]:
    return [x for x in range(len(curr_board)) if curr_board[x] == " "]

def random_player(player_id : int, curr_board : [int]) -> int:
    # Find open spots
    open_spots = get_open_spots(curr_board)
    # Choose spot at random
    return random.choice(open_spots)

def always_pick_winner(player_id : int, curr_board : [int]) -> int:
    # Find open spots
    open_spots = get_open_spots(curr_board)
    # Check if there is a winning spot
    for spot in open_spots:
        new_board = curr_board.copy()
        new_board[spot] = tictactoe.player_strings[player_id]
        state = tictactoe.game_state(new_board)
        if state == player_id:
            return spot
    # If no winning places are found
    return random.choice(open_spots)

def score_board(player_id : int, curr_board : [int]) -> (int, bool):
    game_state = tictactoe.game_state(curr_board)
    opponent_id = (player_id + 1) % 2
    if game_state == player_id:
        return 1, True
    elif game_state == opponent_id:
        return -1, True
    elif game_state == tictactoe.DRAW:
        return 0, True
    else:
        return 0, False

# print(score_board(0, ["X","X","X","X","X","X","X","X","X",]))

def generate_possible_board(player_id : int, curr_board : [int], spot_to_play : int) -> [int]:
    new_board = curr_board.copy()
    # Fill the selected spot with the player in turn's id
    new_board[spot_to_play] = tictactoe.player_strings[player_id]
    return new_board

def minimax(player_id : int, curr_board : [int], depth : int, should_maximize : bool, alpha = float('-inf'), beta= float('inf')) -> int:
    # Check current score and if the game is finished
    curr_score, is_done = score_board(player_id, curr_board)

    # If we are at the bottom of the tree (bepth == 0) or the game is done, return score and nothing else
    if depth == 0 or is_done:
        return curr_score * (depth + 1) # previously "return curr_score", adding the multiplication of the peth will prioritize moves that win sooner (in less moves)

    # Find open spots
    open_spots = get_open_spots(curr_board)

    # During the player_id's turn, we should maximize
    if should_maximize:
        # Initialize max score
        max_score = float('-inf')
        # Get all possible boards after the player_id's move
        for spot in open_spots:
            board = generate_possible_board(player_id, curr_board, spot)
            # Score boards recursively
            score = minimax(player_id, board, depth -1, False, alpha, beta)
            # Update max score
            max_score = max(max_score, score)
            # Set max alpha
            alpha = max(alpha, max_score)
            # Contrast alpha and beta (alpha-beta pruning)
            if alpha >= beta:
                break
        # Return max score
        return max_score
    # In case we are minimazing (opponent's move)
    else:
        # Initialize min score
        min_score = float('inf')
        # Get all possible boards after the opponent's move
        for spot in open_spots:
            board = generate_possible_board((player_id + 1)%2, curr_board, spot)
            # Score boards recursively
            score = minimax(player_id, board, depth -1, True, alpha, beta)
            # Set min score
            min_score = min(min_score, score)
            # Set min beta
            beta = min(beta, min_score)
            # Contrast alpha and beta (alpha-beta pruning)
            if alpha >= beta:
                break
        # Return the min score
        return min_score

def minimax_player(player_id : int, curr_board : [int]) -> int:
    # Find all the open spots
    open_spots = get_open_spots(curr_board)
    # Generate all possible game boards
    possible_boards = list(map(lambda x: generate_possible_board(player_id, curr_board, x), open_spots))
    # Score boards recursively
    scored_boards = list(map(lambda x: minimax(player_id, x, 9, False), possible_boards)) # depth is set to 9 beause we know that there is a maximum of 9 moves (9 spaces available) in this game.

    """
    # For visual representation only
    print("Which board should we pick?")
    for board, score in zip(possible_boards, scored_boards):
        print("This one has a score of " + str(score))
        tictactoe.display_board(board)
        print("------------------------")
    """

    # From the best moves, pick one at random
    best_score = max(scored_boards)
    best_moves = [x for x, score in zip(open_spots, scored_boards) if score == best_score]
    return random.choice(best_moves)


#_______MONTE_CARLO_________

def playout(player_id : int, curr_board : [int]) -> int:
    score, is_finished = score_board(player_id, curr_board)
    if is_finished:
        return score == 1 # return true if score == 1 (a int 1)

    next_board = curr_board
    next_player = 1 - player_id
    while not is_finished:
        spot_to_play = random_player(next_player, next_board)
        next_board = generate_possible_board(next_player, next_board, spot_to_play)
        score, is_finished = score_board(player_id, next_board)
        next_player = 1 - next_player

    return score == 1

def simple_monte_carlo_player(player_id : int, curr_board : [int]) -> int:
    # Find all the open spots
    open_spots = get_open_spots(curr_board)
    # Generate all possible game boards
    possible_boards = list(map(lambda x: generate_possible_board(player_id, curr_board, x), open_spots))

    # Playout each possible board a set number of times
    num_simulations = 100
    wins = [sum([1 for _ in range(num_simulations) if playout(player_id, board)]) for board in possible_boards]
    print(wins)

    # Choose the spot that generated the most wins
    index = max(range(len(open_spots)), key=lambda i: wins[i])
    return open_spots[index]

class TicTacToeNode:
    def __init__(self, player_id : int, board : [int], parent=None, spot : int = -1):
        self.player_id = player_id
        self.board = board
        self.parent = parent
        self.spot = spot
        self.children = []
        self.wins = 0
        self.pulls = 0

    def is_leaf(self):
        return self.children == []  # If it has no children, then it returns True

    def add_child(self, board : [int], spot : int):
        self.children.append(TicTacToeNode(1 - self.player_id, board, self, spot))

    def find_best_ucb(self):
        return max(self.children, key=lambda child: calculate_upper_confidence_bound(child.wins, child.pulls, 2, self.pulls)) # This is hard coding the c value (its the 2)

    def record_play(self, did_win : bool):
        self.pulls += 1
        if did_win:
            self.wins += 1
        if self.parent:
            self.parent.record_play(not did_win)

def calculate_upper_confidence_bound(wins : int, pulls : int, c : float, t : float) -> float:
    if pulls == 0:
        return float ("inf")

    # (Wins / Pulls) + C(sqrt(ln(t)/Pulls))
    return wins / pulls + c * math.sqrt(math.log(t)/pulls)

def monte_carlo_player(player_id : int, curr_board : [int]) -> int:
    root = TicTacToeNode(1 - player_id, curr_board)

    num_simulations = 100
    for _ in range(num_simulations):
        # Selection - find most promising child at each level until we reach a leaf (a node with no children)
        curr_node = root
        while not curr_node.is_leaf():
            curr_node = curr_node.find_best_ucb()
        
        # Expansion - generate the game boards for the children (at curr level)
        score, is_finished = score_board(curr_node.player_id, curr_node.board)
        if not is_finished:
            # Find all open spots
            open_spots = get_open_spots(curr_node.board)
            # Generate all possible gameboards at this level
            possible_boards = list(map(lambda x: generate_possible_board(1 - curr_node.player_id, curr_node.board, x), open_spots))
            for board, spot in zip(possible_boards, open_spots):
                curr_node.add_child(board, spot)
            
            curr_node = random.choice(curr_node.children)

        # Simulation - playout randomly to the end
        did_win = playout(curr_node.player_id, curr_node.board)

        # Backpropagation - update tree to the root
        curr_node.record_play(did_win)

    # Return the index of the generated move with the best wins/pulls score
    winning_child = max(root.children, key=lambda child: child.wins / child.pulls)
    return winning_child.spot






tictactoe.play_game([simple_monte_carlo_player, monte_carlo_player], should_display=True, start_player=0)

"""
x_wins, o_wins, draws = tictactoe.run_simulations([simple_monte_carlo_player, monte_carlo_player], 100, x_always_starts=False)
print("X won " + str(x_wins) + " times")
print("O won " + str(o_wins) + " times")
print("It was a draw " + str(draws) + " times")
"""
