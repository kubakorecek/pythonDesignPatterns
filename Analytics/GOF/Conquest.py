
gcc_small  = [[11,1],[11,2],[23,3],[23,4],[32,5],[32,6],[32,7],[41,3],[41,5],[50,6],[50,2],[41,3],[110,10],[110,20],[230,30],[230,40],[320,50],[320,60],[320,70],[410,30],[410,50],[500,60],[500,20]]

import math


gcc_ = [[11,1],[11,2],[32,5],[2,32]]
gcc_small = [[11,1],[11,2],[23,3],[23,4],[32,5],[32,6],[32,7],[41,3],[41,5],[50,6],[50,2],[41,3],[110,10],[110,20],[230,30],[230,40],[320,50],[320,60],[320,70],[410,30],[410,50],[500,60],[500,20]]

collateral = [[1,1000],[11,1000],[41,2000],[230,2000]]

# a pokud by někdo chtěl testovat rychlost (což si určitě taky změříme a vyhodnotíme) tak tady je algoritmus na generování většího setu
# delitel zřejmě bude třeba odladit oproti pocet tak, aby to dávalo rozumně velké ingoty ...ale napřed je třeba mít ingotovací mechanismus, že?? :-D
delitel = 5
pocet =10000
gcc= []
for i in range(pocet):
    gcc.append([int(abs(math.sin(math.sqrt(i)))*pocet/delitel),int(abs(math.cos(100*math.log(i+1)))*pocet/delitel)])


class CON(object):
    def __init__(self, gcc):
        self.gcc = list(set((tuple(sorted(i))) for i in gcc))
        self.col = []

        self.store_in = {i:set((i,)) for i in self.gcc}
        self.store_out = {}
        self.count = 0

        print(self.store_in)
        self.g(self.store_in)

    def compare(self):
        one = self.list_group.pop()
        #print(self.list_group,888888888888888)
        # self.store_in.pop(one)
        if not self.list_group:
            #print(7777777777777)
            return self.store_in
        else:

            for value in one:
                for group in self.list_group:
                    #print('v', value)
                    #print('g', group, self.list_group)
                    #print('o', one)
                    if value in group:
                        #print('c', self.count)
                        #print('d', self.store_in)

                        new_group = tuple(set(one + group))

                        new_path = self.store_in.get(one)
                        #print('np', new_path, 'dd', self.store_in.get(group), 'dddd', self.store_in.get(one))
                        new_path.update(self.store_in.get(group))

                        #print('group:', group, '\n', self.store_in, '\n', one)
                        self.store_in[new_group] = new_path
                        self.store_in.pop(one)
                        self.store_in.pop(group)
                        #break#
                        self.GCC_compare(self.store_in)
                        break


    def GCC_compare(self, data_in):
        self.list_group = set(data_in.keys())
        #print('GGGG',self.list_group)
        if self.list_group:
            #print(777)
            self.compare()


            #self.count+=1

            #one = list_group.pop()
            #self.store_in.pop(one)

           # for group in list_group:
                #for value in one:
                  #  print('v', value)
                 #   print('g', group,list_group,data_in.keys())
                 #   print('o', one)
                   # if value in group:

                      #  print('c', self.count)
                      #  print('d',self.store_in)

                      #  new_group = tuple(set(one + group))

                      #  new_path = self.store_in.get(one)
                      #  print('np', new_path, 'dd', self.store_in.get(group), 'dddd', self.store_in.get(one))
                      #  new_path.update(data_in.get(group))

                      #  print('group:',group,'\n' ,self.store_in,'\n' ,one)
                      #  self.store_in[new_group] = new_path
                      #  data_in.pop(one)
                      #  data_in.pop(group)#
                      #  self.g(self.store_in)
                   # else:
                        #self.store_out[one] = self.store_in.get(one)
                        #print(self.store_in,'out')
                        #break
        return self.store_in





    def g(self,data_in=dict()):
        print(data_in,'data')
        self.GCC_compare(data_in)
        #print('call',call)
        #self.GCC_compare(call)
        #return self.g(call)
        #return self.g(self.store_out)
        #print(self.store)
        #return self.g(self.store)





a = CON(gcc)
print(a.store_in,0)