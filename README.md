# Maze : Depth First Traversal Project
## Description - "490. The Maze" - LeetCode
Problem Define: Determine if we can find the route from the entrance to exit.

Maze Define: A maze is a path or collection of paths, typically from an entrance to a goal.

This project is an extension of Maze DFS, we use Breadth-First Traversal to solve Maze this problem
* Depth-First Traversal - does not find the Shortest Path
* Breadth-First Traversal - find the Shortest Path

Leetcode question description: 
https://leetcode.com/problems/the-maze/solution/

## KeyIdea

* A people starts at a position (source) and can move in four directions, the goal is to reach the destination:
  * Up
  * Down
  * Left
  * Right

* Direction Priority:  Right, Left, Up, Down <br>

In this case, we try to explore the search space on a level by level basis. i.e. We try to move in all the directions at every step. When all the directions have been explored and we still don't reach the destination, then only we proceed to the new set of traversals from the new positions obtained.


## Solution
* Tree     [Tree Explaination](https://www.geeksforgeeks.org/binary-tree-data-structure/?ref=gcse)
* Graph    [Graph Explaination](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=gcse) 
* Depth-First-Search      [DFS Explaination](https://brilliant.org/wiki/depth-first-search-dfs/#complexity-of-depth-first-search)
* Breadth-First-Search      [BFS Explaination](https://www.youtube.com/watch?v=xlVX7dXLS64) 

## Code: 
https://github.com/jesalshah14/Maze_DFS_Project/blob/main/MAZE_DFS/maze_dfs_code.py


## How to run?

### VSC on windows:
```python
1. copy maze_bfs_code.py to your working directory
2. click the run button on the VSC
```
### On ubuntu:
```python
1. copy the source file to your directory: 
    copy ~/maze_bfs_code.py to your dir 
2. run python script file: 
    python3 maze_bfs_code.py
```
    
### LeetCode platform:
1.Just copy the Class Solution to the Python editor in Leetcode
2.Submit

# Document(Google Slide): 
https://docs.google.com/presentation/d/16ZQbAPRJan5bkXqwwvvEDFscu4jPn6f8/edit?usp=sharing&ouid=107793102389817418175&rtpof=true&sd=true
