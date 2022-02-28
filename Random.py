import time
import math
import itertools
import os


class MyRandom():

    # numSeed = int.from_bytes(os.urandom(7), "big")

    # Input must be > 0
    def __init__(self, numSeed=None):
        self.seed(numSeed)

    def __randint(self):
        # MSVC LCG parameters used
        # multiplier
        a = 214013
        # increment
        c = 2531011
        # modulus
        m = 2 ** 32
        self._numSeed = (a * self._numSeed + c) % m
        return self._numSeed

    def __indexer(self, max):
        finish = str(max)
        if max < 10:
            return int(repr(self.__randint())[-len(finish):])
        else:
            return int(repr(self.__randint())[-len(finish):])

    def get_seed(self):
        return self._numSeed

    # error checking
    def seed(self, new_seed):
        if new_seed is None:
            self._numSeed = int(time.time())
        else:
            if isinstance(new_seed, int) and new_seed > 0:
                self._numSeed = new_seed
            else:
                raise ValueError("The seed must be a positive integer")

    # check int and a < b
    def randint(self, min, max):
        if not isinstance(min, int) or not isinstance(max,
                                                      int) or min < 0 or max < 0 or min > max:
            raise ValueError(
                "min must be smaller then max and they must both be positive integers")
        else:
            # cycle_array = itertools.cycle(self.__array_builder(min, max))
            # program updated to build its own array rather then use cycle array, removes issues with unending loops
            index = self.__indexer(max)
            cycle_array = []
            myResult = 0
            while True:
                cycle_array.extend([i for i in range(max + 1)])
                length = len(cycle_array)
                if length > index:
                    break
            for j in cycle_array:
                index -= 1
                if index == 0:
                    myResult = j
                    break
            return myResult

    def rand(self):
        number = self.__randint()
        length = int(math.log10(number) + 1)
        myFloat = number / 10 ** length
        x = "{:.10f}".format(myFloat)
        return "0." + x[3:]

        # raise IndexError if empty or not list

    def choice(self, _list):
        if not isinstance(_list, list) or len(_list) < 2:
            raise ValueError(
                "_list must be of type list and contain two or more items")
        else:
            length = len(_list) - 1
            index = self.randint(0, length)
            return _list[index]

    # raise IndexError if empty or type error of not list
    def shuffle(self, _list):
        if not isinstance(_list, list) or len(_list) < 3:
            raise ValueError(
                "_list must be of type list and contain three or more items")
        else:
            myList = _list
            for i, num in enumerate(myList[:-2]):
                index = self.randint(i, len(myList) - 1)
                # index = self.randint(0, i + 1)
                myList[i], myList[index] = myList[index], myList[i]
            return myList


class MyCoin(MyRandom):
    def toss(self):
        return self.choice(["Heads", "Tails", ])


class MyDie(MyRandom):
    def throw(self):
        return self.choice(["1", "2", "3", "4", "5", "6", ])


m = MyRandom(123)
print("seed", m.get_seed())
m.seed(200)
print("seed", m.get_seed())

for i in range(5):
    # print("Seed:", p.numSeed)
    print(m.randint(10, 55))

for i in range(5):
    # print("Seed:", p.numSeed)
    print(m.rand())

print("time", time.time())
print("seed", m.get_seed())
m.seed(200)
print("seed", m.get_seed())

for i in range(5):
    # print("Seed:", p.numSeed)
    print(m.choice(['Ace', 'King', 'Queen', 'Jack']))

for i in range(5):
    # print("Seed:", p.numSeed)
    print(m.shuffle(
        ['Ace', 'King', 'Queen', 'Jack', "mango", "banana", "apple",
         "cherry"]))

n = MyDie()
b = MyCoin()
for i in range(5):
    print(n.throw())

for i in range(5):
    print(b.toss())
