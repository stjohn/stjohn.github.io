# Lab 15: Naive Tree Search
# RGGS 670:  Algorithmic Approaches to Biological Data
# Spring 2016

# Uses parsimony scoring function written for Lab 15:
import parsimonyScore as ps
import random 
import copy

"""
Takes a list of (name, sequence) and builds up a random tree
"""  
def buildRandomTree(seqList): 
    t = {}
    for (k,v) in seqList:
        t[k] = ["", v, []]
    parentless = t.keys()
    count = 0
    while len(parentless) > 2:
        newNode = "i"+str(count)
        count += 1
        kid1 = random.choice(parentless)
        parentless.remove(kid1)
        kid2 = random.choice(parentless)
        parentless.remove(kid2)
        t[newNode] = ["", "", [kid1,kid2]]
        t[kid1][0] = newNode
        t[kid2][0] = newNode
        parentless.append(newNode)
    t["root"] = ["", "", [parentless[0], parentless[1]]] 
    t[parentless[0]][0] = "root"
    t[parentless[1]][0] = "root"
    return t
    
"""
Input: A tree dictionary, t, and node, n.
Returns: The subtree at node n in Newick format.
""" 
def convertNewick(t,n):
    if len(t[n][2]) == 0:
        return n
    else:
        left = convertNewick(t, t[n][2][0])
        right = convertNewick(t, t[n][2][1])
        s = "("+ left + "," + right + ")"
        return s
    
def treeSample(sequences):
    bestTree = buildRandomTree(sequences)
    bestScore = ps.scoreTree(bestTree)
    #For 1000 steps:
    for i in range(100):
        #Choose randomly a tree.
        newTree = buildRandomTree(sequences)
        #Score the tree.        
        newScore = ps.scoreTree(newTree)
        
        #We'll add in a print to see what's going on:
        print convertNewick(newTree,"root"), newScore

        #If better score than <tt>bestScore</tt>, 
        if newScore < bestScore:
           #choose it to be the current tree
           bestScore = newScore
           bestTree = newTree
    #Return best tree and score.
    return bestTree, bestScore    
    
        
"""
Takes a tree stored as dictionary and an internal node 
in the tree, and
Returns the two NNI neighbors of the tree around that node.
"""
def nniNeighbor(t, node):
    if node != "root":
        if len(t[node][2]) != 0:
            #Let sib be the sibling of node.
            p = t[node][0]
            sibs = copy.deepcopy(t[p][2])
            sibs.remove(node)
            sib = sibs[0]
            #Let kid1, kid2 be the children of node.
            kid1 = t[node][2][0]
            kid2 = t[node][2][1]
            #Make two (deep) copies of t: tree1 and tree2.
            tree1 = copy.deepcopy(t)
            tree2 = copy.deepcopy(t)
            #Switch sib and kid1 in tree1.
            tree1[p][2] = [node,kid1]   #Set p's kids to be node and kid1
            tree1[kid1][0] = p          #Set kid1's parent to be p
            tree1[node][2] = [sib,kid2]    #Set n's kids to be sib and kid2
            tree1[sib][0] = node        #Set sib's parent to be node
            #Switch sib and kid2 in tree2.
            tree2[p][2] = [node,kid2]   #Set p's kids to be node and kid1
            tree2[kid2][0] = p          #Set kid1's parent to be p
            tree2[node][2] = [sib,kid1]    #Set n's kids to be sib and kid2
            tree2[sib][0] = node        #Set sib's parent to be node           
            #Return tree1 and tree2.
            return (tree1,tree2)
            
            
def maxNeighbor(t0):
    toDo = copy.deepcopy(t0["root"][2])     #Start the to do list with the kids of root.
    bestTree = t0  #Use the inputs as the best tree and best score.
    bestScore = ps.scoreTree(t0)

    print "Neighbors:"
    while len(toDo) > 0:
        nextNode = toDo.pop()
        toDo.extend(copy.deepcopy(t0[nextNode][2]))
        if len(t0[nextNode][2]) > 0: 
            t1, t2 = nniNeighbor(t0,nextNode)
            s1 = ps.scoreTree(t1)
            s2 = ps.scoreTree(t2)            
            print "\t", convertNewick(t1, "root"), s1
            print "\t", convertNewick(t2, "root"), s2
            if s1 < bestScore:
                print s1, bestScore
                bestTree = t1
                bestScore = s1
            if s2 < bestScore:
                print s2, bestScore
                bestTree = t2
                bestScore = s2  

    return bestTree, bestScore


 
"""
Input: A set of n sequences of length k
Output: The best scoring tree we could find after 1000 steps through 
the NNI search space.
"""
def treeSearch(sequences):
    #Choose randomly a tree to be bestSoFar.
    bestSoFar = buildRandomTree(sequences)
    #Score the tree, bestSoFar.
    bestScore = ps.scoreTree(bestSoFar)
    print "Start:", convertNewick(bestSoFar, "root"), bestScore
    #For 1000 steps:
    for i in range(5):
    #   Make a list of all the NNI neighbors of bestSoFar
        neighborBest, neighborScore = maxNeighbor(bestSoFar)
    #   if any of the NNI neighbors of bestSoFar have better score,
        if neighborScore < bestScore:
    #       choose it to be the current tree
            bestSoFar = neighborBest
            bestScore = neighborScore
        
        print "Best so far: ", convertNewick(bestSoFar, "root"), bestScore
    return bestSoFar, bestScore
       

if __name__ == "__main__":
    #Sample tree:
    tree = {"root" : ["","",["i1","i2"]],
        "i1": ["root","", ["a", "i3"]], 
        "i2": ["root","", ["b", "c"]],
        "i3": ["i1","", ["d","e"]],
        "a": ["i1","T A A A A", []],
        "b": ["i2","A A A A G", []],
        "c": ["i2","C A A A T", []],
        "d": ["i3","A A A A A", []],
        "e": ["i3","T A A A A", []]}

    print "\nTest tree:", convertNewick(tree,"root"),":", ps.scoreTree(tree)

    #Sample list of (species, sequence) pairs:    
    seqList = [("ape","A A A A A"),
               ("baboon","A A A A G"),
                ("chimp","C A A A A"),
                ("dog","T G G G G"),
                ("elephant","T G A C A"),
                ("fox","A A G G C")]
    
    #Test the tree sampling function:
    bestTree, bestScore = treeSample(seqList)
    print "\nBest from sample:", convertNewick(bestTree,"root"),":", bestScore
    
    print "\n"
    t,s = treeSearch(seqList)
    print convertNewick(t, "root"), s
