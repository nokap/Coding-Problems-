def path_finder(maze):

#turn that string into a 2d array
    s = [0,0]
#starting point of the first node
 e = [len(maze)-1, len(maze-1)]
 #setting the paramters of the maze
 maze = list(map(list, a.splitlines()))
 #slack stuff we don't need to know (creating the maze??)
 level = {s: 0}
parent = {s : None}
#Ask for help on this, don't understand level = {} and parent {}
i = 1
#i = integers you are searching?
frontier = [s] #integers you have searched starting with the starting point
while frontier:
#while there are numbers you have searched through....
    next = []
    #the next node goes into the empty set
    for u in frontier: #for variable in the frontier
         for v in maze [e]:
         #for variable in the parameters of the maze e = [len(maze)-1, len(maze-1)]
             if v not in level: #if the node is not in the level...
                level[v] = i
                parent[v] = u
                #not sure what this means if node is not in level the index value of the node is equal to 1...
                #if the index value of the node is not in the level...
                next.append(v)
                #add v to frontier
    frontier = next
    i += 1 #continuously add one to the node value as you search each time it loops
    #find connecting nodes
    #check if connecting nodes are explored
    #add connectting ndoes to level
    #add next to our frontier
    #add one to i 
