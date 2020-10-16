

class BinarySerach(object):

    def __init__(self, sequence = []):

        self.sequence = sequence

        if not sequence:

            self.sequence = self.RandomGenerator()

    def RandomGenerator(self):
        import random
        a = [random.randrange(10000) for i in range(100000)]
        a.append(8000)
        return a

    @staticmethod
    def Recursive( A=[],value =0, low=0, high=1):
        mid = int((low + high) / 2)
        print(low, high,mid)
        if high < low:
            raise ValueError("This state high < low is IMPOSSIBLE",low, high)
        if A[mid] > value:

            BinarySerach.Recursive(A,value,low,mid-1)

        elif A[mid] < value:

            BinarySerach.Recursive(A,value, mid+1,high)

        return int((low + high) / 2)



if __name__ == '__main__':

    a = BinarySerach()
    #print(len(a.sequence))
    index = BinarySerach.Recursive(sorted(a.sequence),8000,0,len(a.sequence))
    print(index, a.sequence[80077])
