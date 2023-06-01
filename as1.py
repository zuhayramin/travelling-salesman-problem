import sys
import time
from queue import Queue

def State_Space():
     
    coordinate= []
    checkpoints={}
    dark_blocks=[]
    
    for y in range(8):
        for x in range(7):
            coordinate.append((x,y))
             
    checkpoints["A"]=(1,0)
    checkpoints["B"]=(2,7)
    checkpoints["C"]=(5,5)
    checkpoints["D"]=(5,0)
    
    
    dark_blocks=[(0,7),(0,1),(0,2),(1,7),(1,5),(2,2),(2,1),(3,4),(3,3),(4,1),(5,6),(5,4),(5,3),(5,2),(5,1),(6,6)]
    
    
    return coordinate,checkpoints,dark_blocks


# In[14]:


coordinate,checkpoints,dark_blocks= State_Space()


# In[15]:


def Estimate_cost(current,final):
    #calculates the h()
    estimated_cost = (abs(current[0]-final[0])+abs(current[1]-final[1]))
    return estimated_cost


# In[16]:


def Next_steps_estimate_cost(current,final):
    #returns the h() of RLTB
    Right= Estimate_cost((current[0]+1,current[1]),final)
    Left=  Estimate_cost((current[0]-1,current[1]),final)
    Top=   Estimate_cost((current[0],current[1]+1),final)
    Bottom=Estimate_cost((current[0],current[1]-1),final)
    return [Right,Left,Top,Bottom]


# In[17]:


def Next_steps_coordinate(current):
    #returns the coordinates of RLTB
    Right= (current[0]+1,current[1])
    Left=  (current[0]-1,current[1])
    Top=   (current[0],current[1]+1)
    Bottom=(current[0],current[1]-1)
    return [Right,Left,Top,Bottom]


# In[18]:


def tuple_merger(tuple_list):
    values=[]

    for num in range(len(tuple_list)):
        for num2 in range(len(tuple_list[num])):
            values.append(tuple_list[num][num2])

    return tuple(values)
        


# In[19]:


def possible_options(coordinate):
    new_coordinate=[]
    for num in coordinate:
        if (num[0]>=0) and (num[1]>=0) and (num[0]<=6) and (num[1]<=7) :
            if (num in dark_blocks) == False:
                new_coordinate.append(num)
    return new_coordinate
    


# In[20]:


def Estimate_cost_v2(attached_tuple,final):
    current = (attached_tuple[-2],attached_tuple[-1])
    #calculates the h()
    estimated_cost = (abs(current[0]-final[0])+abs(current[1]-final[1]))
    return estimated_cost


# In[21]:


def index_finder(max_min_value,fun_one):
    # Function used to find the index of max and min values inside a list 
    max_v = max_min_value
    e_choices=fun_one 
    multi_index=[]
    
    if e_choices.count(max_v) == 1:
        for num in range(len(e_choices)):
            if e_choices[num] == max_v:
                index = int(num )

    elif e_choices.count(max_v) > 1:
        for num in range(len(e_choices)):
            if e_choices[num] == max_v:
                multi_index.append(num)
        
    if e_choices.count(max_v) == 1:
        return index
    elif e_choices.count(max_v) > 1:
        return multi_index
        
        
    return index


# In[22]:


def Choice_by_tiebreaker(options,h_cost):
    candidates=[]
    a=(-1,-1)
    for num in options:
        candidates.append((num[-2],num[-1]))

    for x,num in enumerate(candidates):

        if type(index_finder(min(h_cost),h_cost)) == int:
            if x == index_finder(min(h_cost),h_cost):

                if num[1]>a[1]:
                    a=num
                    b=x
                elif num[1]==a[1] and num[0]<a[0]:
                    a=num
                    b=x
                else:
                    pass
            else:
                pass
        if type(index_finder(min(h_cost),h_cost)) == list:
            if x in index_finder(min(h_cost),h_cost):
                
                if num[1]>a[1]:
                    a=num
                    b=x
                elif num[1]==a[1] and num[0]<a[0]:
                    a=num
                    b=x
                else:
                    pass
            else:
                pass      
    
    return b


# In[23]:


def Choice_by_cost(options,h_cost):
    
    index=[]

    if h_cost.count(min(h_cost)) >= 1:
        
        index.append(Choice_by_tiebreaker(options,h_cost))
        #index.append(index_finder(min(h_cost),h_cost))
    elif h_cost.count(min(h_cost)) == 1: 
        index = index_finder(min(h_cost),h_cost)
    else:
        print("Error")
        

    
    return index


# In[24]:


def SPG(current,final):
    h_cost = [] #h_cost here actually represents total cost 
    coordinate = Next_steps_coordinate(current)
    coordinate = possible_options(coordinate)
    options =[]
    p_cost=1
    
    for num in coordinate:
        options.append(tuple_merger([current,num]))
    for num in options:
        h_cost.append((Estimate_cost_v2(num,final)+p_cost))
    #------------------------------------------------------------
    loop = True
    while loop== True:
        
        
        parent = options[Choice_by_cost(options,h_cost)[0]]

        parent_cost= h_cost[Choice_by_cost(options,h_cost)[0]]
        parent_index= Choice_by_cost(options,h_cost)[0]
        current = (parent[-2],parent[-1])
        coordinate = Next_steps_coordinate(current)
        coordinate = possible_options(coordinate)
        
        if current != final :
            for num in coordinate:
                options.append(tuple_merger([parent,num]))

            options.pop(parent_index)
            h_cost=[]
            for num in options:
                h_cost.append((Estimate_cost_v2(num,final)+int(len(num)/2)))
                
        
        else:
            loop = False

    #------------------------------------------------------------  
    return options[parent_index],h_cost[parent_index]


# In[25]:


import time


# In[26]:


ab_path,ab=SPG(checkpoints["A"],checkpoints["B"])
ac_path,ac=SPG(checkpoints["A"],checkpoints["C"])
ad_path,ad=SPG(checkpoints["A"],checkpoints["D"])


bc_path,bc=SPG(checkpoints["B"],checkpoints["C"])
bd_path,bd=SPG(checkpoints["B"],checkpoints["D"])


cd_path,cd=SPG(checkpoints["C"],checkpoints["D"])


ba,ca,da,cb,db,dc=(ab,ac,ad,bc,bd,cd)


# In[52]:

if sys.argv[1] == 'spg':
    print("---------Shortest Paths---------")
    print(f"a,b,{ab}")
    print(f"a,c,{ac}")
    print(f"a,d,{ad}")
    print(f"b,c,{bc}")
    print(f"b,d,{bd}")
    print(f"c,d,{cd}")

if sys.argv[1] == 'tour':
    graph = {
        'A': [['B',ab],['C',ac],['D',ad]],
        'B': [['C',bc],['D',bd],['A',ba]],
        'C': [['D',cd],['A',ca],['B',cb]],
        'D': [['A',da],['B',db],['C',dc]]
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



