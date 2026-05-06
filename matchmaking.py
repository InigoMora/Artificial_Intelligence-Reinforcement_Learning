import mancala
import competition_player as player

#_______MATCHMAKING_________

mancala.play_game([mancala.human_player, player.competition_player], should_display=True, start_player=0)



#_______ALL_MATCHES_________
"""
print("\n")
# COMPETITION vs M Competition
print("COMPETITION vs M Competition")
player_zero, player_one, draws = mancala.run_simulations([competition_player, m_competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# M Competition vs COMPETITION
print("M Competition vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([m_competition_player, competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")


print("\n")
# M Competition vs SMART
print("M Competition vs SMART")
player_zero, player_one, draws = mancala.run_simulations([m_competition_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# SMART vs M Competition
print("SMART vs M Competition")
player_zero, player_one, draws = mancala.run_simulations([smart_player, m_competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# M Competition vs RANDOM
print("M Competition vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([m_competition_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# RANDOM vs M Competition
print("RANDOM vs M Competition")
player_zero, player_one, draws = mancala.run_simulations([random_player, m_competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# M Competition vs MINIMAX
print("M Competition vs MINIMAX")
player_zero, player_one, draws = mancala.run_simulations([m_competition_player, minimax_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MINIMAX vs M Competition
print("MINIMAX vs M Competition")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, m_competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# M Competition vs MONTE CARLO
print("M Competition vs MONTE CARLO")
player_zero, player_one, draws = mancala.run_simulations([m_competition_player, monte_carlo_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MONTE CARLO vs M Competition
print("MONTE CARLO vs M Competition")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, m_competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")




print("\n")
# COMPETITION vs SMART
print("COMPETITION vs SMART")
player_zero, player_one, draws = mancala.run_simulations([competition_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# SMART vs COMPETITION
print("SMART vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([smart_player, competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# COMPETITION vs RANDOM
print("COMPETITION vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([competition_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# RANDOM vs COMPETITION
print("RANDOM vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([random_player, competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# COMPETITION vs MINIMAX
print("COMPETITION vs MINIMAX")
player_zero, player_one, draws = mancala.run_simulations([competition_player, minimax_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MINIMAX vs COMPETITION
print("MINIMAX vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# COMPETITION vs MONTE CARLO
print("COMPETITION vs MONTE CARLO")
player_zero, player_one, draws = mancala.run_simulations([competition_player, monte_carlo_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MONTE CARLO vs COMPETITION
print("MONTE CARLO vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, competition_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")





print("\n")
# SMART vs RANDOM
print("COMPETITION vs SMART")
player_zero, player_one, draws = mancala.run_simulations([smart_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# SMART vs COMPETITION
print("SMART vs COMPETITION")
player_zero, player_one, draws = mancala.run_simulations([random_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# SMART vs MINIMAX
print("SMART vs MINIMAX")
player_zero, player_one, draws = mancala.run_simulations([smart_player, minimax_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MINIMAX vs SMART
print("MINIMAX vs SMART")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# SMART vs MONTE CARLO
print("SMART vs MONTE CARLO")
player_zero, player_one, draws = mancala.run_simulations([smart_player, monte_carlo_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MONTE CARLO vs SMART
print("MONTE CARLO vs SMART")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, smart_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")






print("\n")
# MINIMAX vs RANDOM
print("MINIMAX vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# RANDOM vs MINIMAX
print("RANDOM vs MINIMAX")
player_zero, player_one, draws = mancala.run_simulations([random_player, minimax_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")

print("\n")
# MINIMAX vs MONTE CARLO
print("MINIMAX vs MONTE CARLO")
player_zero, player_one, draws = mancala.run_simulations([minimax_player, monte_carlo_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# MONTE CARLO vs MINIMAX
print("MONTE CARLO vs MINIMAX")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, minimax_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")






print("\n")
# MONTE CARLO vs RANDOM
print("MONTE CARLO vs RANDOM")
player_zero, player_one, draws = mancala.run_simulations([monte_carlo_player, random_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
# RANDOM vs MONTE CARLO
print("RANDOM vs MONTE CARLO")
player_zero, player_one, draws = mancala.run_simulations([random_player, monte_carlo_player], 1000)
print("Player 0 won " + str(player_zero) + " times")
print("Player 1 won " + str(player_one) + " times")
print("It was a draw " + str(draws) + " times")
"""