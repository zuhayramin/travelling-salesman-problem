This ReadMe file is to help execute the code used to generate a shortest path graph and the costs of the Breadth-First Search and Uniform-Cost Search on the path.

In order to generate the Shortest Path Graph, use the following line to execute, after moving to the appropriate directory:

>>python3 as1.py spg

NOTE: While the code executes all other distances very quickly, the distance from 'B' to 'D' takes approximately 6 minutes, due to the similarity in costs between multiple paths considered under the A* heuristic.

In case such a long runtime is not acceptable for the submission, we have also added another file "as1_tours.py". This file has the final values we received from "as1.py spg" hard-coded into the graph, before applying the search algorithms.

In order to determine the paths and costs of BFS and UCS:

>>python3 as1.py tour
*** Will take 6 minutes to execute completely

Or

>>python3 as1_tour.py
*** Search algorithms with hard-coded graph values
