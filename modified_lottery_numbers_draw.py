

from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple
import random

@dataclass
class LotteryRules:
    main_numbers: int
    max_main: int
    bonus_numbers: int = 0
    max_bonus: int = 0

class LotteryGame(Enum):
    EUROMILLIONS = LotteryRules(5, 51, 2, 13)
    LOTTO = LotteryRules(6, 60)
    SET_FOR_LIFE = LotteryRules(5, 48, 1, 11)
    THUNDERBALL = LotteryRules(5, 40, 1, 15)
    LOTTO_HOTPICKS = LotteryRules(5, 60)

class LotteryDrawer:
    def __init__(self):
        self.shuffle_count = random.randint(1, 100)
    
    def draw_numbers(self, k: int, max_num: int) -> List[int]:
        """
        Draw k unique random numbers from 1 to max_num
        
        Args:
            k: Number of numbers to draw
            max_num: Maximum number that can be drawn
            
        Returns:
            List of k unique random numbers
            
        Raises:
            ValueError: If k > max_num or if either parameter is negative
        """
        if k <= 0 or max_num <= 0:
            raise ValueError("Parameters must be positive integers")
        if k > max_num:
            raise ValueError(f"Cannot draw {k} numbers from range of {max_num}")
            
        try:
            nums = list(range(1, max_num))
            for _ in range(self.shuffle_count):
                random.shuffle(nums)
            return sorted(random.sample(nums, k))
        except Exception as e:
            raise ValueError(f"Error drawing numbers: {str(e)}")

    def play_game(self, game: LotteryGame) -> Tuple[List[int], List[int]]:
        """
        Play a specific lottery game
        
        Args:
            game: LotteryGame enum value
            
        Returns:
            Tuple of (main numbers, bonus numbers)
        """
        rules = game.value
        main_numbers = self.draw_numbers(rules.main_numbers, rules.max_main)
        bonus_numbers = []
        if rules.bonus_numbers > 0:
            bonus_numbers = self.draw_numbers(rules.bonus_numbers, rules.max_bonus)
        return main_numbers, bonus_numbers

def main():
    drawer = LotteryDrawer()
    
    print("Select lottery game:")
    for i, game in enumerate(LotteryGame):
        print(f"{i}: {game.name}")
    
    try:
        play = int(input("Enter game number: "))
        if not 0 <= play < len(LotteryGame):
            raise ValueError("Invalid game selection")
            
        selected_game = LotteryGame(list(LotteryGame)[play])
        main_nums, bonus_nums = drawer.play_game(selected_game)
        
        print(f"\n{selected_game.name} Draw Results:")
        print(f"Main numbers: {main_nums}")
        if bonus_nums:
            bonus_name = "Lucky Stars" if selected_game == LotteryGame.EUROMILLIONS else "Bonus Numbers"
            print(f"{bonus_name}: {bonus_nums}")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())