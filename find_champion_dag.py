"""
You are given the integer n and a 0-indexed 2D integer array edges of length m 
representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed
edge from team ui to team vi in the graph.
A directed edge from a to b in the graph means that team a is stronger than team b
and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger
than team a.

Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. 
So the champion is team 0.
"""

from typing import List

def findChampion(n: int, edges: List[List[int]]) -> int:
    # Create an array to track incoming edges (number of teams stronger than current team)
    incoming = [0] * n
    
    # Count incoming edges for each team
    for u, v in edges:
        incoming[v] += 1
    
    # The champion will be the team with no incoming edges
    # (no team is stronger than them)
    for i in range(n):
        if incoming[i] == 0:
            return i
    
    return -1  # This case won't occur as per problem constraints