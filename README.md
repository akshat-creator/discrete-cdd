# Robotics Path Planning with Dijkstra and A* Algorithms

This project is a collaborative exploration of path planning algorithms—specifically Dijkstra's and A*—to find efficient paths for a robot from point A to point B on a laid-out course. Through this project, we analyzed and implemented these algorithms and compared their effectiveness and efficiency in a robotics context. Additionally, we explored a genetic algorithm to solve a subset of the traveling salesman problem, useful for robots needing to visit multiple waypoints.

https://youtu.be/EJmOr4AEUi0?si=M0NTi2WHxgC31_Y4

## Table of Contents
- [Project Overview](#project-overview)
- [MVP Goals](#mvp-goals)
- [Stretch Goals](#stretch-goals)
- [Algorithm Implementation](#algorithm-implementation)
  - [Dijkstra’s Algorithm](#dijkstras-algorithm)
  - [A* Algorithm](#a-algorithm)
  - [Genetic Algorithm for Traveling Salesman](#genetic-algorithm-for-traveling-salesman)

## Project Overview
Our project involved implementing and comparing Dijkstra's and A* algorithms to optimize path planning for robotics applications. Both algorithms are widely used in robotics for finding the shortest paths, but each has unique advantages. Dijkstra’s explores all paths, making it thorough but less efficient. A* uses heuristics, making it more efficient by focusing primarily on paths closer to the end goal.

## MVP Goals
- Implement Dijkstra’s and A* algorithms for pathfinding.
- Compare the efficiency of Dijkstra’s and A* implementations.

## Stretch Goals
- Explore the Bellman-Ford algorithm and the traveling salesman problem (TSP).
- Implement our path planning solution on a **Neato** robot.
- Consider the impact of multiple robots traversing the same graph and how to adapt the algorithms for multi-robot scenarios.

## Algorithm Implementation

### Dijkstra’s Algorithm
Dijkstra's algorithm is a shortest-path algorithm that explores paths from a starting vertex to all other vertices in the graph. It calculates the minimum distance to all reachable nodes, making it thorough but sometimes inefficient for large graphs. This algorithm is effective in scenarios where finding paths to multiple nodes is necessary.

### A* Algorithm
A* is a pathfinding algorithm similar to Dijkstra’s but with a heuristic component, making it more efficient for single-source, single-destination problems. We used the **Manhattan Distance** heuristic in our project to guide the robot towards the end goal while avoiding nodes that take the robot away from it.

**Efficiency Note**: Dijkstra’s took approximately 25 steps, while A* achieved the same path in only 5 steps by avoiding unnecessary nodes.

### Genetic Algorithm for Traveling Salesman
We implemented a genetic algorithm to solve a suboptimal solution to the traveling salesman problem (TSP). For our robot, the TSP is relevant when the robot needs to visit multiple points and then return to its starting point.

- **Process**: The algorithm generates 100 random possible paths, evaluates each path’s length, and "mates" the best paths to produce shorter paths iteratively.
- **Outcome**: The genetic algorithm stopped when we found a path below a predefined length threshold. Our best solution achieved a path length of 169 units.

