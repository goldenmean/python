"""
In chess, the Elo rating system is used to calculate player strengths based on game results.

A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.

Implement this system.
"""

import math

class EloRating:
    def __init__(self, base_rating=1200, k_factor=32):
        """
        Initialize the Elo rating system
        
        Args:
            base_rating (int): The starting rating for new players
            k_factor (int): The maximum rating change possible in one game
        """
        self.base_rating = base_rating
        self.k_factor = k_factor
        self.players = {}
    
    def add_player(self, player_name):
        """Add a new player with the base rating"""
        if player_name not in self.players:
            self.players[player_name] = self.base_rating
        return self.players[player_name]
    
    def get_rating(self, player_name):
        """Get the current rating of a player"""
        return self.players.get(player_name, self.base_rating)
    
    def expected_score(self, player_rating, opponent_rating):
        """
        Calculate the expected score of a player based on ratings
        
        Returns a number between 0 and 1 representing win probability
        """
        return 1 / (1 + math.pow(10, (opponent_rating - player_rating) / 400))
    
    def update_ratings(self, winner_name, loser_name):
        """
        Update ratings after a game
        
        Args:
            winner_name: Name of the winning player
            loser_name: Name of the losing player
        
        Returns:
            tuple: (winner's new rating, loser's new rating)
        """
        # Ensure both players are in the system
        self.add_player(winner_name)
        self.add_player(loser_name)
        
        # Get current ratings
        winner_rating = self.get_rating(winner_name)
        loser_rating = self.get_rating(loser_name)
        
        # Calculate expected scores
        winner_probability = self.expected_score(winner_rating, loser_rating)
        loser_probability = self.expected_score(loser_rating, winner_rating)
        print(f"winner_expected: {winner_probability}, loser_expected: {loser_probability}")
        
        # Calculate rating changes
        winner_new_rating = round(winner_rating + self.k_factor * (1 - winner_probability))
        loser_new_rating = round(loser_rating + self.k_factor * (0 - loser_probability))
        
        # Update ratings
        self.players[winner_name] = winner_new_rating
        self.players[loser_name] = loser_new_rating
        
        return winner_new_rating, loser_new_rating

def main():
    # Create an instance of the EloRating system
    elo = EloRating()
    
    # Example usage with some test games
    print("Initial ratings:")
    print("Player1:", elo.add_player("Player1"))  # 1200
    print("Player2:", elo.add_player("Player2"))  # 1200
    print("Player3:", elo.add_player("Player3"))  # 1200
    print()
    
    # Simulate some games
    print("Game Results:")
    
    # Game 1: Player1 beats Player2
    winner, loser = elo.update_ratings("Player1", "Player2")
    print(f"Player1 beats Player2: Player1 new rating: {winner}, Player2 new rating: {loser}")
    
    # Game 2: Player3 beats Player1 (upset since Player1 is now higher rated)
    winner, loser = elo.update_ratings("Player3", "Player1")
    print(f"Player3 beats Player1: Player3 new rating: {winner}, Player1 new rating: {loser}")
    
    # Game 3: Player3 beats Player2
    winner, loser = elo.update_ratings("Player3", "Player2")
    print(f"Player3 beats Player2: Player3 new rating: {winner}, Player2 new rating: {loser}")
    
    print("\nFinal Ratings:")
    for player, rating in elo.players.items():
        print(f"{player}: {rating}")

if __name__ == "__main__":
    main()