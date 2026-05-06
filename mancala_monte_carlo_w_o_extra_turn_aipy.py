import mancala
import random
import math

#mancala.play_game([mancala.human_player, mancala.human_player], should_display=True)

# Indications are to "Write a random AI function that makes a random legal play",
# meaning player 0 can choose from 0-5 and player 1 from 7-12.
def get_open_spots(curr_board : [int]) -> [int]:
    return [x for x in range(len(curr_board)) if curr_board[x]>0]

def random_player(player_id : int, curr_board : [int]) -> int:
    # Find open spots
    open_spots = get_open_spots(curr_board)
    # Choose spot at random
    # Create choice variable (random choice)
    choice = random.choice(open_spots)
    # Player 0 can only choose from 0-5
    if player_id == 0:
        while not choice < 6:
            choice = random.choice(open_spots)
        return choice
    # Player 1 can only choose from 7-12
    while not choice > 6 and choice < 13:
        choice = random.choice(open_spots)
    return choice

# Play human vs random_player
#mancala.play_game([mancala.human_player, random_player], should_display=True)

def get_viable_spots(player_id : int, curr_board : [int]) -> [int]:
    open_spots = get_open_spots(curr_board)
    viable_spots = []
    # Append viable spots
    if player_id == 0:
        for spot in open_spots:
            if spot < 6:
                viable_spots.append(spot)
    if player_id == 1:
        for spot in open_spots:
            if spot > 6 and spot < 13:
                viable_spots.append(spot)
    # Check if the movement would end in the bucket
    # NOTE: viable_spots cannot be empty, as the game would be over (handled by mancala.py).
    return viable_spots

def smart_player(player_id : int, curr_board : [int]) -> int:
    # Get viable spots
    # NOTE: get_viable_spots is not able to return an empty list empty, as the game would be over first (handled by mancala.py).
    viable_spots = get_viable_spots(player_id, curr_board)
    # We traverse the list backwards because in case of there being more than one movement that allow for an extra turn, we want to make sure to take the move on the left first, to avoid ruining the other movement (check "Game Programming Write-ups" pdf, section "Artificial Inteligence - part 1" for reference).
    for spot in reversed(viable_spots):
        if player_id == 0:
            if curr_board[spot] == (6-spot):
                return spot
        # Else player_id == 1
        if curr_board[spot] == (13-spot):
            return spot
    return random.choice(viable_spots)


# random_player vs random_player 1000 times
"""
player_zero, player_one, draws = mancala.run_simulations([random_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
"""

# human vs smart_player
#mancala.play_game([mancala.human_player, smart_player], should_display=True)

# random_player vs smart_player 1000 times, followed by change in place.
"""
print("RANDOM VS SMART")
player_zero, player_one, draws = mancala.run_simulations([random_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
print("----Change Sides----")
print("SMART VS RANDOM")
player_zero, player_one, draws = mancala.run_simulations([smart_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
"""




#   --------------- ALTERNATIVE IMPLEMENTATION ---------------
# Trying to plan for future additions to the AI


def _get_viable_spots(player_id : int, curr_board : [int]) -> [int]:
    open_spots = get_open_spots(curr_board)
    viable_spots = []
    # Append viable spots
    if player_id == 0:
        for spot in open_spots:
            if spot < 6:
                viable_spots.append(spot)
    if player_id == 1:
        for spot in open_spots:
            if spot > 6 and spot < 13:
                viable_spots.append(spot)
    # Check if the movement would end in the bucket
    # NOTE: viable_spots cannot be empty, as the game would be over (handled by mancala.py).
    return viable_spots

def _check_for_extra_turn_move(player_id : int, curr_board : [int], viable_spots : [int]) -> int:
    # We traverse the list if viable spots backwards because in case of there being more than one movement that allow for an extra turn, we want to make sure to take the move on the left first, to avoid ruining the other movement (check "Game Programming Write-ups" pdf, section "Artificial Inteligence - part 1" for reference).
    for spot in reversed(viable_spots):
        if player_id == 0:
            if curr_board[spot] == (6-spot):
                return spot
        # Else player_id == 1
        if curr_board[spot] == (13-spot):
            return spot
    return False

def _smart_player(player_id : int, curr_board : [int]) -> int:
    viable_spots = _get_viable_spots(player_id, curr_board)
    extra_turn_move = _check_for_extra_turn_move(player_id, curr_board, viable_spots)
    if extra_turn_move:
        return extra_turn_move
    return random.choice(viable_spots)

# random_player vs smart_player_v2 1000 times, followed by change in place.

"""
print("RANDOM VS SMART")
player_zero, player_one, draws = mancala.run_simulations([random_player, _smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
print("----Change Sides----")
print("SMART VS RANDOM")
player_zero, player_one, draws = mancala.run_simulations([_smart_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
"""





#________________MINIMAX__________________

def score_board(player_id : int, curr_board : [int]) -> (int, bool):
    # Initialize opponent id
    opponent_id = (player_id + 1) % 2
    # Check if the game is over
    is_game_over = mancala.game_is_over(curr_board) #curr_board contains a number and a list, so mancala.py does not like it. I do not know when it got modified e.g. (0, [0, 6, 1, 3, 0, 0, 8, 0, 0, 8, 4, 4, 1, 13])
    if is_game_over:
        winner = mancala.who_won(curr_board)
        if winner == player_id:
            return 1, True
        elif winner == opponent_id:
            return -1, True
        else:   # When winner == 2, This is a draw in the mancala.who_won() function.
            return 0, True
    else:
        return 0, False #Game continues

def generate_possible_board(player_id : int, curr_board : [int], spot_to_play : int) -> [int]:
    # Fill the selected spot with the player in turn's id
    next_player, new_board = mancala.sow(spot_to_play, player_id, curr_board)   #mancala.sow returns (player_id, [board]). We used to only take board (list), but now we also check if the current player to see if they got an extra turn
    # Check for extra turn
    extra_turn = False
    if next_player == player_id:
        extra_turn = True
    return new_board, extra_turn

def minimax(player_id : int, curr_board : [int], depth : int, should_maximize : bool, alpha = float('-inf'), beta= float('inf'), check_depth = int(5)) -> int:
    # Check current score and if the game is finished
    curr_score, is_done = score_board(player_id, curr_board)

    # Get the difference in score for the currwnt board
    who_is_winning=0
    if(player_id == 0):
        who_is_winning = int(curr_board[6])-int(curr_board[13])
    else:
        who_is_winning = int(curr_board[13])-int(curr_board[6])

    # If we are at the bottom of the tree (bepth == 0) or the game is done, return score and nothing else
    if depth == check_depth or is_done: # Depth will dictate how many turns it looks ahead
        return (curr_score*100) + who_is_winning # We multiply times a 100 so that the value of points ahead can never surpass a the value of a win.

    # Find open spots
    open_spots = _get_viable_spots(player_id, curr_board)

    # During the player_id's turn, we should maximize
    if should_maximize:
        # Initialize max score
        max_score = float('-inf')
        # Get all possible boards after the player_id's move
        for spot in open_spots:
            board, extra_turn = generate_possible_board(player_id, curr_board, spot)
            # Check for extra turn
            if extra_turn:
                # Score boards recursively as player (again) if extra turn
                score = minimax(player_id, board, depth, True, alpha, beta, check_depth) #* We do not increase the depth, as it is an extra turn
            else:
                # Score boards recursively as opponent
                score = minimax(player_id, board, depth + 1, False, alpha, beta, check_depth)
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
            board, extra_turn = generate_possible_board((player_id + 1)%2, curr_board, spot)
            # Check for extra turn
            if extra_turn:
                # Score boards recursively as oponent (again) if extra turn
                score = minimax(player_id, board, depth +1, False, alpha, beta, check_depth) # For some reason it breaks if I do not do depth + 1
            else:
                # Score boards recursively as player
                score = minimax(player_id, board, depth + 1, True, alpha, beta, check_depth)
            #
            # Set min score
            min_score = min(min_score, score)
            # Set min beta
            beta = min(beta, min_score)
            # Contrast alpha and beta (alpha-beta pruning)
            if alpha >= beta:
                break
        # Return the min score
        return min_score

def minimax_player(player_id : int, curr_board : [int], check_depth : int = 5) -> int: # to do better agains the smart system, push check_depth to a higher number e.g. 7 NOTE: Changing it only here does not sem to be working, change it over in minimax as well
    # Find all the open spots
    open_spots = _get_viable_spots(player_id, curr_board)
    # Generate all possible game boards
    possible_boards = list(map(lambda x: generate_possible_board(player_id, curr_board, x)[0], open_spots)) # added [0] to only take the boards, as generate_possible_board now returns the board and if the player gets an extra turn
    # Score boards recursively
    scored_boards = list(map(lambda x: minimax(player_id, x, 0, False, check_depth), possible_boards)) # NOTE: if I start the depth at 0 and increase it as I create the moves (inverse to tic-tac-toe), I am ble to account for an infinite amount of moves. 

    """
    # For visual representation only
    print("Which board should we pick?")
    for board, score in zip(possible_boards, scored_boards):
        print("This one has a score of " + str(score))
        mancala.display_board(board)
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
    next_player = 1 - player_id     # Modify******* The next player is not always the other player
    while not is_finished:
        spot_to_play = random_player(next_player, next_board)
        next_board, extra_turn = generate_possible_board(next_player, next_board, spot_to_play) # added [0] to only take the baord #**MOdify generate_possible_board also retunrs extra turn 
        score, is_finished = score_board(player_id, next_board)
        next_player = 1 - next_player    # Modify******* The next player is not always the other player

    return score == 1

def simple_monte_carlo_player(player_id : int, curr_board : [int]) -> int:
    # Find all the open spots
    open_spots = get_viable_spots(player_id, curr_board)  # Modify to get viable spots******* Check if player ID is right
    # Generate all possible game boards
    possible_boards = list(map(lambda x: generate_possible_board(player_id, curr_board, x)[0], open_spots)) #**MOdify generate_possible_board also retunrs extra turn 

    # Playout each possible board a set number of times
    num_simulations = 100
    wins = [sum([1 for _ in range(num_simulations) if playout(player_id, board)]) for board in possible_boards]
    print(wins)

    # Choose the spot that generated the most wins
    index = max(range(len(open_spots)), key=lambda i: wins[i])
    return open_spots[index]

class MancalaNode:
    def __init__(self, player_id : int, board : [int], parent=None, spot : int = -1):   #******maybe add a c (prob with a default value) instead of hard coding it (store it in self)
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
        self.children.append(MancalaNode(1 - self.player_id, board, self, spot))  # Modify******* The next player is not always the other player

    def find_best_ucb(self):
        return max(self.children, key=lambda child: calculate_upper_confidence_bound(child.wins, child.pulls, 2, self.pulls)) # This is hard coding the c value (its the 2)

    def record_play(self, did_win : bool):
        self.pulls += 1
        if did_win:
            self.wins += 1
        if self.parent:
            self.parent.record_play(not did_win)    # Modify******* The next player is not always the other player

def calculate_upper_confidence_bound(wins : int, pulls : int, c : float, t : float) -> float:
    if pulls == 0:
        return float ("inf")

    # (Wins / Pulls) + C(sqrt(ln(t)/Pulls))
    return wins / pulls + c * math.sqrt(math.log(t)/pulls)

def monte_carlo_player(player_id : int, curr_board : [int]) -> int:
    root = MancalaNode(1 - player_id, curr_board) # Modify******* The next player is not always the other player

    num_simulations = 100   # ***** Maybe not hard code it and make it a default of 100
    for _ in range(num_simulations):
        # Selection - find most promising child at each level until we reach a leaf (a node with no children)
        curr_node = root
        while not curr_node.is_leaf():
            curr_node = curr_node.find_best_ucb()
        
        # Expansion - generate the game boards for the children (at curr level)
        score, is_finished = score_board(curr_node.player_id, curr_node.board)
        if not is_finished:
            # Find all open spots
            open_spots = get_viable_spots(player_id, curr_node.board) # ******* CHeci if i need player_id or the oother player
            # Generate all possible gameboards at this level
            possible_boards = list(map(lambda x: generate_possible_board(1 - curr_node.player_id, curr_node.board, x)[0], open_spots)) # ***MOdify generate_possible_board also retunrs extra turn ******* The next player is not always the other player
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






#mancala.play_game([monte_carlo_player, random_player], should_display=True, start_player=0)


# monte_carlo_player vs random_player
print("monte_carlo_player vs random_player")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, random_player], 15)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")



"""
# MINIMAX vs SMART
print("minimax_player vs smart")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, smart_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("smart vs minimax_player")
player_zero, player_one, draws = mancala.run_simulations([smart_player, minimax_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
"""
#__ALL_MATCHES__
"""

# MINIMAX vs RANDOM
print("minimax_player vs random")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, random_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("random vs minimax_player")
player_zero, player_one, draws = mancala.run_simulations([random_player, minimax_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

# MINIMAX vs SMART
print("minimax_player vs smart")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, smart_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("smart vs minimax_player")
player_zero, player_one, draws = mancala.run_simulations([smart_player, minimax_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

# SMART vs RANDOM
print("SMART vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([smart_player, random_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("RANDOM vs SMART")
player_zero, player_one, draws = mancala.run_simulations([random_player, smart_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

"""









# MINIMAX vs RANDOM
"""
print("minimax_player vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, random_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

# RANDOM vs MINIMAX
print("RANDOM vs minimax_player")
player_zero, player_one, draws = mancala.run_simulations([random_player, minimax_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

# MINIMAX vs SMART
print("minimax_player vs SMART")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, smart_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

# SMART vs MINIMAX
print("SMART vs minimax_player")
player_zero, player_one, draws = mancala.run_simulations([smart_player, minimax_player], 100)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
"""