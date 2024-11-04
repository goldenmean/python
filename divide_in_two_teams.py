"""
A teacher must divide a class of students into two teams to play dodgeball.
Unfortunately, not all the kids get along, and several refuse to be put on
the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm 
that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams 
{0, 1, 4, 5} and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
On the other hand, given the input below, you should return False.

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
"""


def can_divide_teams(students):
    # Initialize teams dictionary with -1 (unassigned)
    teams = {student: -1 for student in students}
    
    def can_assign_team(student, team):
        # If student is already assigned to a team
        if teams[student] != -1:
            # Return True if it matches the proposed team
            return teams[student] == team
        
        # Assign the team
        teams[student] = team
        
        # Check all enemies of this student
        for enemy in students[student]:
            # Enemy must be on opposite team (1-team flips between 0 and 1)
            if not can_assign_team(enemy, 1-team):
                return False
                
        return True
    
    # Try to assign first student to team 0
    for student in students:
        if teams[student] == -1:
            if not can_assign_team(student, 0):
                return False
    
    # Create the two teams
    team0 = {student for student, team in teams.items() if team == 0}
    team1 = {student for student, team in teams.items() if team == 1}
    
    return [team0, team1]

# Test cases
def test_teams():
    # Test case 1 - Should work
    students1 = {
        0: [3],
        1: [2],
        2: [1, 4],
        3: [0, 4, 5],
        4: [2, 3],
        5: [3]
    }
    
    # Test case 2 - Should fail
    students2 = {
        0: [3],
        1: [2],
        2: [1, 3, 4],
        3: [0, 2, 4, 5],
        4: [2, 3],
        5: [3]
    }
    
    result1 = can_divide_teams(students1)
    result2 = can_divide_teams(students2)
    
    print("Test case 1:", result1)
    print("Test case 2:", result2)

if __name__ == "__main__":
    test_teams()