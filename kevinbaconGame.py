#Zev Stravitz
#5/25/16
#Kevin Bacon Game

from Graph import Graph

def makeGraph(G,database): #makeGraph is designed to make vertex for every actor and movie (Edges have no names)
    file = open(database,'r')
    previous = ' '
    movie_dict = {}
    for line in file:
        line = line.strip()
        name, movie = line.split('|')
        if name == previous:
            if movie in movie_dict:
                G.insert_edge(new_name,movie_dict[movie])
            else:
                current_movie = G.insert_vertex(movie)
                movie_dict[movie] = current_movie
                G.insert_edge(new_name,current_movie)
        else:
            new_name = G.insert_vertex(name)
            if movie in movie_dict:
                G.insert_edge(new_name,movie_dict[movie])
            else:
                current_movie = G.insert_vertex(movie)
                movie_dict[movie] = current_movie
                G.insert_edge(new_name,current_movie)
        previous = name
    return movie_dict

def BFS(G,center,discovered): #G is graph, center is starting vertice, discovered is discovered vertices
    table = {}
    level_num = 0
    level = [center]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in G.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        if level_num%2 == 0:
            table[level_num] = len(level)
        level_num += 1
        level = next_level
    return table

def Find(G,center,discovered,connect,function = True): #True determines whether to just print out bacon number or also path
    if center.element() == connect.element():
        if function == True:
            return str(center.element()) + ' is ' + str(connect.element()) + '(' + str(0) + ')'
        else:
            return 0
    elif connect not in discovered:
        return str(connect.element()) + ' is UNREACHABLE'
    else:
        bacon = 0
        connect_edge = discovered[connect]
        opposite = connect_edge.opposite(connect)
        path = str(connect.element()) + '->' + str(opposite.element())
        while opposite != center:
            connect_edge = discovered[opposite]
            opposite = connect_edge.opposite(opposite)
            path = path + ' -> ' + str(opposite.element())
            bacon +=1
        if function == True:
            return path + " (" + str((bacon/2 + 1)) + ")"
        else:
            return (bacon/2 + 1)

def avgdist(G,center,discovered,movie_dict,function = True): #Average distance from the center
    total_bacon = 0
    vert = 1
    for j in discovered:
        if j.element() not in movie_dict:
            if j != center:
                b = Find(G,center,discovered,j,function = False) #Call find each time with changing connection vertex
                total_bacon += b
                vert += 1
    unreachable = Unreachable(G,movie_dict,discovered)
    if function == True:
        return str(total_bacon/float(vert)) + " " + str(center.element()) + " (" + str(vert) +","+ str(unreachable) + ")"
    else:
        return total_bacon/float(vert)

def Unreachable(G,movie_dict,discovered): #This is to calculate the number of unreachable vertices from the current center
    actors = 0
    for i in G.vertices():
        if i.element() not in movie_dict:
            actors += 1
    found = 0
    for i in discovered:
        if i.element() not in movie_dict:
            found += 1
    unreachable = actors - found
    return unreachable

def Recenter(G,center_name,center): #Estabilish new center
    for i in G.vertices():
        if i.element() == center_name:
            center = i
            return center
    print 'NAME NOT IN DATABASE'
    return center #if the center isn't in the database, keep the current center as is


def suffix(G,name): #Allows for input lacking suffix (e.g. Kevin Bacon (I))
    for v in G.vertices():
        if v.element() not in movie_dict:
            if name in v.element():
                name = v.element()
    return name


def Topcenter(G,discovered,n): #prints the n actors/actresses with the lowest average Bacon Numbers 
    topcenter = []
    for h in discovered:
        if h.element() not in movie_dict:
            discovered = {h:None}
            BFS(G,h,discovered)
            average = avgdist(G,h,discovered,movie_dict,function = False)
            topcenter.append((average,h.element())) #Make tuple with avg bacon # and corresponding center
    topcenter.sort() #Sort based on avg bacon number
    for i in range(0,n):
        print str(topcenter[i][0]) + '     ' + str(topcenter[i][1])

def Table(G,discovered,center,table): #prints how many actors/actresses have each Bacon Number
    unreachable = Unreachable(G,movie_dict,discovered)
    print 'Table of distances for ' + str(center.element())
    for i in table:
        print 'Number ' + str(i) + ':   ' + str(table[i])
    print 'Unreachable' + ':   ' + str(unreachable)

def findAll(G,center,movie_dict): #finds the Bacon Number for all actors/actresses that are connected to the current center 
    for i in G.vertices():
        if i.element() not in movie_dict:
            print Find(G,center,discovered,i,function = True) + '\n'

def Most(G,center,movie_dict): #finds the actor/actress that was in the most movies in the database 
    counter,max_num = 0,0
    for e in G.incident_edges(center):
        counter +=1
    max_num = counter
    max_actor = ()
    for i in G.vertices():
        if i.element() not in movie_dict:
            counter = 0
            for e in G.incident_edges(i):
                counter += 1
            if counter > max_num:
                max_num = counter
                max_actor = (i.element(),max_num)
    print 'Actor/Actress with most credits is ' + str(max_actor[0]) + ' with ' + str(max_actor[1]) + ' credits'
    
        
def longest(G,center,discovered): # prints out one of the longest paths to the current center
    longest = 0
    longest_actor = ()
    for i in discovered:
        if i.element() not in movie_dict:
            length = Find(G,center,discovered,i,function = False)
            if length > longest:
                longest = length
                longest_actor = (i.element(),length)
    print 'The longest path to the center actor, ' + str(center.element()) + ', is from ' + str(longest_actor[0]) + ' with a length of ' + str(longest_actor[1])
    

def movies(G,vertex_name): #lists all movies for an actor or actress 
    for i in G.vertices():
        if i.element() == vertex_name:
            for e in G.incident_edges(i):
                print e.opposite(i).element()
    

if __name__ == '__main__':
    G = Graph()
    data = int(raw_input('What database would you like to use\n1. Test\n2. Small\n3. top250\nType in number: '))
    if data == 1:
        database = 'imdb.cslam.txt'
    elif data == 2:
        database = 'imdb.small.txt'
    else:
        database = 'imdb.top250.txt'
    movie_dict = makeGraph(G,database)
    center = None
    if data != 1:
        center_name = 'Kevin Bacon (I)'
        for i in G.vertices():
            if i.element() == center_name:
                center = i
    else:
        center_name = 'Alice'
        center = Recenter(G,center_name,center)
    command = ''
    while command[0:4] != 'quit':
        discovered = {center:None}
        table = BFS(G,center,discovered)
        print 'Pick your command'
        print '    find <name>\n    recenter <name>\n    avgdist\n    topcenter\n    table\n    findAll\n    most\n    longest\n    movies <name>\n    quit'
        command = raw_input('Enter a command:')
        if command[0:5] == 'find ':
            find_name = command[5:]
            find_name = suffix(G,find_name)
            connect = None
            for i in G.vertices():
                if i.element() == find_name:
                    connect = i
            if connect != None:
                print Find(G,center,discovered,connect)
            else:
                print 'CANNOT FIND: NAME NOT IN DATABASE'
        elif command[0:8] == 'recenter':
            center_name = command[9:]
            center_name = suffix(G,center_name)
            center = Recenter(G,center_name,center)
        elif command[0:7] == 'avgdist':
            print avgdist(G,center,discovered,movie_dict)
        elif command[0:9] == 'topcenter':
            n = int(command[10:])
            Topcenter(G,discovered,n)
        elif command[0:5] == 'table':
            Table(G,discovered,center,table)
        elif command[0:7] == 'findAll':
            findAll(G,center,movie_dict)
        elif command[0:4] == 'most':
            Most(G,center,movie_dict)
        elif command[0:7] == 'longest':
            longest(G,center,discovered)
        elif command[0:6] == 'movies':
            vertex_name = command[7:]
            vertex_name = suffix(G,vertex_name)
            movies(G,vertex_name)
        elif command[0:4] == 'quit':
            break
        else:
            print 'COMMAND NOT RECOGNIZED - TRY AGAIN'
