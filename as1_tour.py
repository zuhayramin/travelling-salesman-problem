
import sys
from queue import Queue
import time

graph = {
    'A': [['B',9],['C',10],['D',5]],
    'B': [['C',6],['D',13],['A',9]],
    'C': [['D',8],['A',10],['B',6]],
    'D': [['A',5],['B',13],['C',8]]
}

visited = [] 
queue = []
bfs_start_time = time.time()
def bfs(visited, graph,node):
    total_cost = 0
    visited.append(node)
    queue.append(node)
    last_node = ''
    A_node = 0
    while queue:
        s = queue.pop(0) 
        print (s, end = '-')
        for num in range(len(graph[s])):
            if graph[s][num][0] not in visited:
                min_index = graph[s][num][0]
                visited.append(min_index)
                queue.append(min_index)
                total_cost = graph[s][num][1] + total_cost
                break
            
        
        last_node = s
        for num in range(len(graph[last_node])):
            if graph[last_node][num][0] == 'A':
                A_node = num
        
    total_cost = total_cost + graph[last_node][A_node][1] #adds the cost of going back to A from the last node
            
    print('A')
    print('\nTotal Tour Cost is: ' + str(total_cost))
    
print('--------------------')
print('Algorithm Used: BFS')
bfs(visited, graph,'A')
print('--------------------')
bfs_end_time = time.time()

visited = [] 
queue = []
ucs_start_time = time.time()
def ucs(visited, graph,node):
    total_cost = 0
    visited.append(node)
    queue.append(node)
    last_node = ''
    A_node = 0
    while queue:
        s = queue.pop(0) 
        print (s, end = '->')
        min_cost = 1000
        for num in range(len(graph[s])):
            min_index = graph[s][num][0]
            if min_index not in visited:
                if graph[s][num][1] < min_cost:
                    min_cost = graph[s][num][1]
                    min_index = graph[s][num][0]
        if min_index not in visited:
            visited.append(min_index)
            queue.append(min_index)
            total_cost = min_cost + total_cost
            
        
        last_node = s
        for num in range(len(graph[last_node])):
            if graph[last_node][num][0] == 'A':
                A_node = num
        
    total_cost = total_cost + graph[last_node][A_node][1] #adds the cost of going back to A from the last node
            
    print('A')
    print('\nTotal Tour Cost is: ' + str(total_cost))
print('--------------------')
ucs(visited, graph,'A')
print('Algorithm used: UCS')
print('--------------------')
ucs_end_time = time.time()

bfs_time = bfs_end_time -  bfs_start_time
ucs_time = ucs_end_time -  ucs_start_time
print('--------------------')
print('Statistics:\n')
print('Nodes        Time Cost')
print('BFS          ' + str(bfs_time))
print('UCS          ' + str(ucs_time))