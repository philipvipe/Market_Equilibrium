import numpy as np
import random as rm

# define statespace
states = ["Starbucks, Tim_Hortons"]

# define possible sequences of events
transitions = [["SS", "ST"], ["TS", "TT"]]

# Probabilities matrix (transition matrix)
transition_matrix = [[.8, .2],[.1,.9]]

if sum(transition_matrix[0]) != 1 and sum(transition_matrix[1]) != 1:
    print("Somewhere, something went wrong. The rows in your transition matrix do not add up to 0")

def activity_forecast(days, start_state):

	# Choose starting state

    activityToday = start_state
    # print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Starbucks":
            change = np.random.choice(transitions[0],replace=True,p=transition_matrix[0])
            if change == "SS":
                prob = prob * 0.8
                activityList.append("Starbucks")
                pass
            elif change == "ST":
                prob = prob * 0.2
                activityToday = "Tim_Hortons"
                activityList.append("Tim_Hortons")
        elif activityToday == "Tim_Hortons":
            change = np.random.choice(transitions[1],replace=True,p=transition_matrix[1])
            if change == "TS":
                prob = prob * 0.1
                activityList.append("Starbucks")
                pass
            elif change == "TT":
                prob = prob * 0.9
                activityToday = "Tim_Hortons"
                activityList.append("Tim_Hortons")
        i += 1  
    return activityList
    # print("Possible states: " + str(activityList))
    # print("End state after "+ str(days) + " days: " + activityToday)
    # print("Probability of the possible sequence of states: " + str(prob))

# To save every activityList
SIM_COUNT = 1000000
sb_start_sims = []
th_start_sims = []
starbucks_count = 0.0
tim_hortons_count = 0.0

sb_market_share = .4
th_market_share = .6


# Run x # of small 2-day simulations starting with Starbucks and Tim Hortons where x is determined 
# by the respective market share
for iterations in range(1,int(sb_market_share*SIM_COUNT+1)):
        sb_start_sims.append(activity_forecast(2, "Starbucks"))
for iterations in range(1, int(th_market_share*SIM_COUNT+1)):
        th_start_sims.append(activity_forecast(2, "Tim_Hortons"))

print len(sb_start_sims)
# Iterate through the list to get a count of all activities ending in Starbucks and Tim_Hortons respectively
for sim in sb_start_sims:
    if(sim[2] == "Starbucks"):
        starbucks_count += 1
    elif(sim[2] == "Tim_Hortons"):
    	tim_hortons_count += 1

print len(th_start_sims)
for sim in th_start_sims:
    if(sim[2] == "Starbucks"):
        starbucks_count += 1
    elif(sim[2] == "Tim_Hortons"):
        tim_hortons_count += 1

print("Starbucks count: ", starbucks_count)
print("Tim Hortons count: ", tim_hortons_count)
# Calculate the final market shares (from a population of SIM_COUNT simulations)
starbucks_probability = float(starbucks_count/SIM_COUNT)
tim_hortons_probability = float(tim_hortons_count/SIM_COUNT)
final_market_share = [starbucks_probability, tim_hortons_probability]

print(final_market_share)