

import random

def draw_lottery_nos(k, max_num):
    num_shuffle = random.randint(1,100)

    nums = list(range(1,max_num)) # Euromillions

    for _ in range(num_shuffle):
        random.shuffle(nums)
    
    res = random.sample(nums, k)
    return res

play_type = ["Euromillions", "Lotto", "Set for life", "Thunderball", "Lotto Hotpicks"]
# Press 0 to win Euromillions, 1 to win Lotto, 2 to win Set for life, 3 to win Thunderball, 
      # 4 to win Lotto Hotpicks

play = 0 # choose one number to select type of lottery to play
if play > 4 or play < 0:
    print("Invalid input")
    print("Are you sure you don't want to win the lottery? ... ok quitting")
    quit()
    
game = play_type[play]

if game == "Euromillions" :    
    print(f"Euromillions numbers are: {draw_lottery_nos(5, 51)}") # Euromillions - 5 numbers
    print(f"Euromillions lucky stars are: {draw_lottery_nos(2, 13)}") # Euromillions - 2 lucky stars    
elif game ==  "Lotto":
    print(f"Lotto numbers are: {draw_lottery_nos(6, 60)}") # Lotto - 6 numbers

elif game == "Set for life":
    print(f"Set for life numbers are: {draw_lottery_nos(5, 48)}")
    print(f"Lifeball number is: {draw_lottery_nos(1, 11)}")

elif game == "Thunderball":
    print(f"Thunderball numbers are: {draw_lottery_nos(5, 40)}")
    print(f"Thunderball is : {draw_lottery_nos(1, 15)}")
elif game == "Lotto Hotpicks":
    print(f"Lotto Hotpicks numbers are: {draw_lottery_nos(5, 60)}")
