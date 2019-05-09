class emptyandfill():


    #takes the start and goal and the capacity from the run file
    # chs is a flag that determines either just vessels or has 2 vessels and a sink and a tap
    def choose(self, startdiff, goaldiff, capacitydiff, chs):
        self.startdiff = startdiff
        self.goaldiff = goaldiff
        self.capacitydiff = capacitydiff
        self.chs = chs

    def start(self):
        # returns the start state that was given from the run file
        return self.startdiff

    def goal(self, node):
        # if the node given is equal to the goal it will return True otherwise False
        return self.goaldiff == node

    def succ(self, node):

        if self.chs == 1:# that means its only vessels
            # two for loops to loop through the vessels
            for key1, value1 in node.items():
                for key2, value2 in node.items():

                    if (key1 != key2) and (value1 != 0):# when the loops not pointing on the same vessel and the first point is not 0
                        newnode = node.copy()
                        # self.capacitydiff[(list(newnode.keys()).index(key2))] - value2)
                        # this gets the capacity by taking the index of the vessel list and using it in the capacity list...
                        # ...then we - the value so we can get the empty space.
                        if (value1 <= (self.capacitydiff[(list(newnode.keys()).index(key2))] - value2)):
                            # if the empty space in vessel 2 is more than whats in vessel 1 we will just pour
                            newnode[key2] = value2 + value1
                            newnode[key1] = value1 - value1

                            yield newnode

                        elif (value2 != (self.capacitydiff[(list(newnode.keys()).index(key2))])):
                            cap = self.capacitydiff[(list(newnode.keys()).index(key2))]
                            # we will pour from vessel 1 to vessel 2 until vessel 2 is full or vessel 1 is empty
                            newnode[key2] = value2 + (cap - value2)
                            newnode[key1] = value1 - (cap - value2)

                            yield newnode

        elif self.chs ==0: # that means that it contains a sink and tap
             # the first part has the same code as the first
            for key1, value1 in node.items():
                for key2, value2 in node.items():
                    if (value1 != 0):
                        newnode2 = node.copy()
                        if (value1 <= (self.capacitydiff[(list(newnode2.keys()).index(key2))] - value2)):

                            newnode2[key2] = value2 + value1
                            newnode2[key1] = value1 - value1

                            yield newnode2

                        elif (value2 != (self.capacitydiff[(list(newnode2.keys()).index(key2))])):
                            cap = self.capacitydiff[(list(newnode2.keys()).index(key2))]

                            newnode2[key2] = value2 + (cap - value2)
                            newnode2[key1] = value1 - (cap - value2)

                            yield newnode2
                 # this part is for the tap so it fills till full
                newnode2 = node.copy()
                if value1 != (self.capacitydiff[(list(newnode2.keys()).index(key1))]) :
                    newnode2[key1] = self.capacitydiff[(list(newnode2.keys()).index(key1))]
                    yield newnode2
                 # this is the sink so it drains all the water
                newnode2 = node.copy()
                if value1 != 0:
                    newnode2[key1] = 0
                    yield newnode2

