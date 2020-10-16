##########################################
#Author: Jakub Korecek

#########################################


# import speccial object dictionary
from collections import defaultdict


class Conquest(object):

    def __init__(self, data=[], col_data=[]):

        # data for GCC
        self.data = data

        # Data for Colateral
        self.col_data = col_data

        # data not provided, plat csv will be loaded
        if not (data and col_data):
            self.readCSV()


        # initiliaze variablees to hold data
        self.graph = defaultdict(list) # data in, to construct graph witth all nodes and paths

        # this holds data out
        self.data_out = defaultdict(set)

        # procedure to fill data for graph
        self.GraphData()

        # call algorithm for data
        self.FindAllGroups()

        # basic stats
        self.Stats()

    def readCSV(self):
        """
        read Plat CSV
        :return:
        """

        import csv # import module to read csv

        ######################################
        #   WARNING
        #####################################
        # in python files must be readed within context manger , that is WITH context, in oreder to not
        # overload file system of OS
        with open('GCC.csv') as gcc:
            readCSV = csv.reader(gcc, delimiter=',')
            for row in readCSV:
                self.data.append([row[0], row[1]])
        with open('COLL.csv') as col:
            readCSV = csv.reader(col, delimiter=',')
            for row in readCSV:
                self.data.append([row[0], row[1]])

    def FindAllGroups(self):
        """
        find all groups
        :return:
        """

        ########
        # Function iterating over all posible nodes in seracheng algorithm called DEEPTH FIRST SEARCH
        ########


        collection_of_nodes = set(self.graph.keys())
        while collection_of_nodes:
            i = collection_of_nodes.pop()
            group = self.DFS_iterative(self.graph,i)
            self.data_out[i].add(tuple(group))
            collection_of_nodes -= group

    def GraphData(self):
        """
        prepare data
        :return:
        """

        for i in range(len(self.data)):

            self.graph[self.data[i][0]].append(self.data[i][1])
            self.graph[self.data[i][1]].append(self.data[i][0])

        for i in range(len(self.col_data)):

            self.graph[self.col_data[i][0]].append(-self.col_data[i][1])
            self.graph[-self.col_data[i][1]].append(self.col_data[i][0])


    def DFS_iterative(self, graph,start):
        """
            DEPTH FIRST SEARCH algorithm
        :param graph:
        :param start:
        :return:
        """
        stack = [start] # stack
        visited = set() # set of visited nodes
        while stack: # if stack is not empty then perform
            node = stack.pop() # get first element of stack
            if node not in visited: # mark as visited
                visited.add(node)
                new_nodes = set(graph[node]) - visited # find all nodes which were not visited
                stack.extend(new_nodes) # fill stack with all nodes which are connected
        return visited


    def Stats(self):
        """
        Some basic stats out.
        :return:
        """

        for  k,v in self.data_out.items():
            col = list()
            s = list()
            for i in v:
                for j in i:
                    #print(j)
                    if str(j).startswith('-'):
                        col.append(j)
                    else:
                        s.append(j)
            self.data_out[k].add((len(col),len(s),))

    def networx(self):
        """
        Using networx to draw and so.
        :return:
        """

        col_data = [] # store colateral data, that is this node is with -, GABO idea
        color_map = [] # store colors for that nodes
        for item in self.col_data:
            col_data.append([item[0], -item[1]])
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.Graph()
        G.add_edges_from(col_data + self.data)
        for node in G:
            if node < 0:
                color_map.append('blue')
            else:
                color_map.append('green')
        big = max(nx.connected_components(G), key=len)
        print(len(big))
        nx.draw_networkx(G,node_color = color_map,with_labels = True)
        plt.show()


if __name__ == '__main__':
    gcc_small = [[11, 23], [11, 2], [23, 3], [23, 4], [32, 5], [32, 6], [32, 7], [41, 3], [41, 5], [50, 6], [50, 2],
                 [41, 3], [110, 10], [110, 20], [230, 30], [230, 40], [320, 50], [320, 60], [320, 70], [410, 30],
                 [410, 50], [500, 60], [500, 20]]
    collateral = [[1, 1000], [11, 1000], [41, 2000], [230, 2000]]

    a = Conquest(gcc_small,collateral)
    a.networx()
    print(a.data_out)
    b = Conquest()
    print(len(b.data_out))


