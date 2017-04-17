"""
Lab 11 Demonstration:  Assembling reads using deBruijn graphs
"""

def getReadsFromFile(infile):
     f = open(infile)
     #Depending on the file, could have extra newlines at end, strip off:
     data = f.read().rstrip()
     return data.split("\n")

def createDeBruijnGraph(reads):
     #Initialize a dictionary to hold the adjacency list.
     adjList = {}
     for read in reads:
          #Get the prefix and suffix:
          prefix = read[:2]
          suffix = read[1:]
          if prefix in adjList:
               #It's in the list, and by construction, it's value is a list:
               adjList[prefix].append(suffix)
          else: #create a new entry for it:
               adjList[prefix] = [suffix]
          if suffix not in adjList:
               #Add it in with no outgoing neighbors:
               adjList[suffix] = []
     return adjList

def balanceGraph(g):
     """
     Add extra edges to g to make it "balanced"-- that is every
     node has the same incoming and outcoming edges.
     Will assume the g has a Hamiltonian path, so, only need to add in one edge.
     """
     #Make a single list of the nodes with in-coming edges:
     allNeighborLists = g.values()
     allNeighbors = [i for nList in allNeighborLists for i in nList]

     #Find the node with no outgoing edges:
     for node in g.keys():
          #Find the node with no outgoing edges:
          if not g[node]:
               endNode = node
          #Find the node with no incoming edges:
          if g not in allNeighbors:
               begNode = node
     #Attach them
     g[endNode] = [begNode]
     

def eulerianCycle(graph):
     """
     Form a cycle Cycle by randomly walking in Graph
     (don't visit the same edge twice!)
     """
     #Put all edges into the unexplored edges:
     unexplored = graph.copy()
     #Grab an edge from graph to start off the cycle:
     key, value = unexplored.popitem()
     #Use that as the start of our cycle:
     cycle = [key,value[0]]
     #Add back to the dictionary if there's > 1 outgoing edges
     if len(value) > 1:
          unexplored[key] = value[1:]
     
     #While there are unexplored edges in graph:
     while unexplored:
          print "Currently, cycle is: ", cycle
          print "\t unexplored is: ", unexplored
          #Check if you can go extend the cycle:
          if cycle[-1] in unexplored:
               neighbors = unexplored.pop(cycle[-1])
               if len(neighbors) > 0:
                    if len(neighbors) > 1:
                         #Put back the remaining unvisited edges:
                         unexplored[cycle[-1]] = neighbors[1:]
                    #Add to cycle
                    cycle.append(neighbors[0])                         
          #Select a node newStart in cycle with still unexplored edges.
          else:                   
               for i in range(len(cycle)):
                    print i, cycle
                    if cycle[i] in unexplored:
                         neighbors = unexplored.pop(cycle[i])
                         print "neighbors", neighbors
                         if len(neighbors) > 1:
                              #Put back the remaining unvisited edges:
                              unexplored[cycle[-1]] = neighbors[1:]
                         if len(neighbors) > 0:
                              #Reorder cycle to put i at the end:
                              cycle = cycle[:i] + cycle[i:] 
                              #Add to cycle
                              cycle.append(neighbors[0])
                         break

     return cycle

def assemble(k_mers):
     """
     Takes k_mers and returns a sequence
     """
     g = createDeBruijnGraph(reads)
     print "The graph is: ", g     
     balanceGraph(g)
     print "The balanced graph is: ", g
     
     print "\n\nBuilding up the Eulerian cycle"
     c = eulerianCycle(g)
     print "\n\nFound the cycle:", c

     #Missing step:  convert the cycle c into the sequence:
     return c

if __name__ == "__main__":
     reads = getReadsFromFile("textbookReads.txt")
     assemble(reads)

