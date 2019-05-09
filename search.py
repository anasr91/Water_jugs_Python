def depth_first_search(problem, node, space, visited=set()):
    token = problem.token(node)
    if token in visited: return
    # we have tried this node already
    visited = visited.union(set([token]))

    # create new set that contains the node
    if problem.goal(node): return [node]
    # base case
    #print(problem.succ(node))
    for n_succ in problem.succ(node):
        #print(problem.succ(node))

        print(space,n_succ)
        sol = depth_first_search(problem, n_succ, space +"        ", visited)

        if sol:
            # first path is returned
            return [node] + sol
