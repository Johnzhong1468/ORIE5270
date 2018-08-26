import heapq


def create_edges(line):
    """
    line: tuple string
    return: edges dictionary
    """
    edges = {}
    paren = 0
    tup = "("
    for i in line:
        if i == '(':
            paren += 1
        elif i == ')':
            paren += -1
            tup += ')'
            tup_eval = eval(tup)
            edges[float(tup_eval[0])] = float(tup_eval[1])
            tup = '('
        elif paren == 1:
            tup += i
    return edges


def find_shortest_path(text_file, source, end):
    """
    file: txt file that contains graph
    source: starting point, an item in graph
    end: ending point, an item in graph
    return: shortest distance from source to end
    """
    file = open(text_file, "r")
    lines = file.readlines()
    graph = dict()
    for i in range(len(lines)):
        if i % 2 == 1:
            graph[float(lines[i-1])] = create_edges(lines[i])
    # S is set
    # F is list of tuples of the form (distance, graph item)
    # dist is a dictionary that records distance of each point to source
    # previous is a dict to store shortest path
    Settled = set()
    Frontier = [(0, source)]
    heapq.heapify(Frontier)
    dist = {source: 0}
    previous = {}
    while len(Frontier) > 0:
        # f is the item with smallest dist from F
        f = heapq.heappop(Frontier)
        Settled.add(f[1])
        for item in graph[f[1]].keys():
            if item not in Settled and item not in [i[1] for i in Frontier]:
                dist[item] = dist[f[1]]+graph[f[1]][item]
                heapq.heappush(Frontier, (dist[item], item))
                previous[item] = f[1]
            elif dist[f[1]]+graph[f[1]][item] < dist[item]:
                dist[item] = dist[f[1]]+graph[f[1]][item]
                previous[item] = f[1]
    # print path
    path = [end]
    if end not in Settled:
        dist[end] = None
        path = None
    else:
        path = [end]
        trace_back = previous[end]
        while trace_back and source != trace_back:
            path.append(trace_back)
            trace_back = previous[trace_back]
        path.append(trace_back)
        path = path[::-1]
    return(dist[end], path)


def find_negative_cycles(text_file):
    """
    file: txt file that contains graph
    source: starting point, an item in graph
    return: whether it has a negative cycle and the cycle
    """
    file = open(text_file, "r")
    lines = file.readlines()
    graph = dict()
    for i in range(len(lines)):
        if i % 2 == 1:
            graph[float(lines[i-1])] = create_edges(lines[i])
    for init in graph:
        # initialize
        # set initial distance from souce to of all points is 0
        # previous contains the chain of shortest path
        distance = {}
        previous = {}
        for node in graph:
            distance[node] = float('inf')
            previous[node] = None
        # distance from source to source is 0
        distance[init] = 0
        pre = {**distance}
        for i in range(len(graph)-1):
            temp = {**distance}
            for node in graph:
                if i > 0 and distance[node] != pre[node]:
                    for next_node in graph[node]:
                        if distance[next_node] > \
                                distance[node] + graph[node][next_node]:
                            distance[next_node] = \
                                distance[node] + graph[node][next_node]
                            previous[next_node] = node
                elif i == 0:
                    for next_node in graph[node]:
                        if distance[next_node] > \
                                distance[node] + graph[node][next_node]:
                            distance[next_node] = \
                                distance[node] + graph[node][next_node]
                            previous[next_node] = node
            pre = {**temp}
            if distance == temp:
                break
        # one more iteration to reach last node t, detect negative loop
        for node in graph:
            for next_node in graph[node]:
                if distance[next_node] > distance[node] + \
                        graph[node][next_node]:
                    print("Negative cycle exist:")
                    neg_cycle = [node]
                    start = node
                    trace_back = previous[start]
                    while start != trace_back and trace_back:
                        neg_cycle.append(trace_back)
                        trace_back = previous[trace_back]
                    neg_cycle.append(trace_back)
                    neg_cycle = neg_cycle[::-1]
                    return(neg_cycle)
    return(None)
