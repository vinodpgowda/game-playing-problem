import numpy as np
import sys

# To decide which action to take for a state
def alpha_beta_decision(current_state):
    v = -np.inf
    for action in actions:
        state = current_state.copy()
        if action == "R":
            left_value = min_value(result(action,state),-np.inf,np.inf)
        else:
            right_value = min_value(result(action,state),-np.inf,np.inf)
    if left_value > right_value:
        return "R"
    elif right_value > left_value:
        return "B"
    else:
        return "R"
    
# To get a sucessor state for a given action and a state 
def result(action,state):
    if action == "R":
        state["red"] -= 1
        return state
    elif action == "B":
        state["blue"] -= 1
        return state


# To get the maximum utitlity value from max player's perspective(Computer or AI)
def max_value(current_state,alpha,beta):
    if terminal_test(current_state):
        return utility(current_state)
    
    v = -np.inf # assigning negative infinity to the variable v

    for action in actions:
        state = current_state.copy()
        sucessor = result(action,state)
        v =  max(v,min_value(sucessor,alpha,beta))
        if v >= beta:
            return v
        alpha = max(alpha,v)
    return v


# To get the minimum utility value from max player's perspective
def min_value(current_state,alpha,beta):
    if terminal_test(current_state):
        return -abs(utility(current_state))

    v = np.inf # assigning positive infinity to the variable v
    
    for action in actions:
        state = current_state.copy()
        sucessor = result(action,state)
        v =  min(v,max_value(sucessor,alpha,beta))
        if v <= alpha:
            return v
        beta = min(beta,v)
    return v
    

# To check if a state is a terminal node(leaf)
def terminal_test(state):
    if state["red"] == 0 or state["blue"] == 0:
        return 1
    else:
        return 0


# To get the points of a state
def utility(state):
    return state["red"]*2 + state["blue"]*3
    # 2 points for every red ball and 3 points for every blue ball


# To pick a ball from a given action
def pick(action):
    if action == "R":
        return "picked a red ball"
    elif action == "B":
        return "picked a blue ball"


# Initialising the initial state and conditions
if len(sys.argv) >= 3:
    r = int(sys.argv[1])
    b = int(sys.argv[2])
else:
    print("\nERROR\nPlease pass the number of red and blue balls for the game to start!\n")
    exit()

actions = ["R","B"]
i = 1
initial_state = {}
initial_state["red"] = r
initial_state["blue"] = b
current_state = initial_state.copy()

# To check who's turn to play first
if len(sys.argv) > 3:
    if sys.argv[3].upper() == "HUMAN":
        i = 0

# Actual game starts now
print("\nRed Blue Nim game starts!")

while terminal_test(current_state) != 1:
    
    
    if i == 0:
        # Human's turn
        print("\n\nYour turn to pick a ball\n")
        print("Balls available\nRed : {}\tBlue : {}".format(current_state["red"],current_state["blue"]))
        a = input('''\nEnter "R" to pick up a red ball or "B" to pick up a blue ball: ''').upper()
        if a in actions:
            print("\nYou " + pick(a))
        else:
            print("\nERROR\nPlease enter a valid input")
            continue
        current_state = result(a,current_state)
        i = 1
    else:
        # Computer's turn
        print("\n\nComputer's turn to pick a ball\n")
        print("Balls available\nRed : {}\tBlue : {}".format(current_state["red"],current_state["blue"]))
        v = alpha_beta_decision(current_state)
        print("\nComputer " + pick(v))
        current_state = result(v,current_state)
        i = 0

# Game over
print("\nBalls available\nRed : {}\tBlue : {}".format(current_state["red"],current_state["blue"]))
print("~~~~~GAME OVER~~~~~")
if i == 0:
    print("\nYou won with {} points\n".format(utility(current_state)))
else:
    print("\nComputer won with {} points\n".format(utility(current_state)))

