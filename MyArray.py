import numpy as np
from statistics import fmean
# usen in mean function
from copy import deepcopy


# used in copy function

class MyArray:
    def __init__(self, array):
        # Constructor accepts 1d and 2d arrays in list form, raises error input is not a list or not a nested lists of same length.
        if self.__arrayDepth__(array) == 0 and isinstance(array, list):
            self.array = array
        elif isinstance(array, list):
            length = len(str(array[0]))
            for i in array:
                if not isinstance(i, list):
                    raise TypeError(
                        "The input must be a list or a list containing nested lists")
                elif len(str(i)) != length:
                    raise ValueError(
                        "All rows of the array must be the same length")
            self.array = array
        else:
            raise TypeError(
                "The input must be a list or a list containing nested lists")

    def min(self, **kwargs):
        # Method returning the min of an array, calls the min method built into Pyhton. An axis can be specified using the keyword "axis=" and return an error if axis 1 is called on a 1d array.
        if kwargs == {}:
            if self.__arrayDepth__(self.array) == 0:
                print(min(self.array))
            else:
                minList = []
                for i in self.array:
                    minList += i
                print(min(minList))
        else:
            minList = []
            if kwargs["axis"] == 0 and self.__arrayDepth__(self.array) == 0:
                print(min(self.array))
            elif kwargs["axis"] == 0:
                for i in zip(*self.array):
                    minList.append(min(i))
                print(minList)
            elif kwargs["axis"] == 1:
                for i in self.array:
                    minList.append(min(i))
                print(minList)
            else:
                raise IndexError(
                    "Axis 1 is out of bounds for array of dimension 1")

    def max(self, **kwargs):
        # Method returning the max of an array, calls the max method built into Pyhton. An axis can be specified using the keyword "axis=" and return an error if axis 1 is called on a 1d array.
        if kwargs == {}:
            if self.__arrayDepth__(self.array) == 0:
                print(max(self.array))
            else:
                maxList = []
                for i in self.array:
                    maxList += i
                print(max(maxList))
        else:
            maxList = []
            if kwargs["axis"] == 0 and self.__arrayDepth__(self.array) == 0:
                print(max(self.array))
            elif kwargs["axis"] == 0:
                for i in zip(*self.array):
                    maxList.append(max(i))
                print(maxList)
            elif kwargs["axis"] == 1:
                for i in self.array:
                    maxList.append(max(i))
                print(maxList)
            else:
                raise IndexError(
                    "Axis 1 is out of bounds for array of dimension 1")

    def mean(self, **kwargs):
        # Method returning the mean of an array, calls the fmean method from the statistics module. An axis can be specified using the keyword "axis=" and return an error if axis 1 is called on a 1d array.
        if kwargs == {}:
            if self.__arrayDepth__(self.array) == 0:
                print(fmean(self.array))
            else:
                meanList = []
                for i in self.array:
                    meanList += i
                print(fmean(meanList))
        else:
            meanList = []
            if kwargs["axis"] == 0 and self.__arrayDepth__(self.array) == 0:
                print(fmean(self.array))
            elif kwargs["axis"] == 0:
                for i in zip(*self.array):
                    meanList.append(fmean(i))
                print(meanList)
            elif kwargs["axis"] == 1:
                for i in self.array:
                    meanList.append(fmean(i))
                print(meanList)
            else:
                raise IndexError(
                    "Axis 1 is out of bounds for array of dimension 1")

    def copy(self):
        # Method to make a copy of an instance in the martix format used by the rest of the class methods. Can copy both 1d and 2d arrays.
        if self.__arrayDepth__(self.array) == 0:
            array = self.array[:]
            return MyArray(array)
        else:
            array = [i[:] for i in self.array]
            return MyArray(array)

    @classmethod
    def zeros(cls, *args):
        # Class  method that acts  as an alternate constructor to create arrays composed of zeros. Error checking confirms that user inputs are ints or tuples of the correct length and that indexes are not out of range. it is also checked that inputs are positive.
        if len(args) > 2 or len(args) < 1 or not isinstance(args,
                                                            (int, tuple)):
            raise ValueError(
                "Input must be a single int or a pair of ints in a tuple to be valid")
        else:
            try:
                array = []
                if len(args) == 1:
                    for i in range(args[0]):
                        if args[0] < 1:
                            print(args[0])
                            raise ValueError("Input must be a positive number")
                        else:
                            array += str(0)
                    return cls(array)
                else:
                    for i in range(args[0]):
                        if args[0] < 1:
                            raise ValueError("Input must be a positive number")
                        else:
                            array2 = []
                            for j in range(args[1]):
                                if args[1] < 1:
                                    raise ValueError(
                                        "Input must be a positive number")
                                else:
                                    array2 += str(0)
                            array.append(array2)
                    return cls(array)
            except IndexError:
                raise IndexError(
                    "You must provide a valid index to create an array")

    @classmethod
    def __formatArray1d__(cls, array):
        # Private class method used by other methods of the class to format 1d arrays in a matrix format.
        arrayCopy = "| "
        for i in array:
            arrayCopy += str(i) + " "
            arrayCopy += "| "
        return arrayCopy

    @classmethod
    def __formatArray2d__(cls, array):
        # Private class method used by other methods of the class to format 2d arrays in a matrix format.
        arrayCopy = ""
        for i in array:
            arrayCopy += "| "
            for j in i:
                arrayCopy += str(j) + " "
            arrayCopy += "|\n"
        return arrayCopy[:-1]

    # Does this need to be a function?
    def __arrayDepth__(self, array):
        # Priavte utitlity method used by otehr methods in class that returns the depth of a list allowing 1d and 2d arrays to be identified.
        return sum(1 for i in array if isinstance(i, list))

    def __getitem__(self, arg):
        # Method overiding the built in getitem method. Allow parts of arrays from the class to be returned using square bracket notation, can handle both 1d and 2d arrays.
        if len(str(arg)) == 1:
            return self.array[arg]
        else:
            x, y = arg
            return self.array[x][y]

    def __setitem__(self, arg, arg2):
        # Method overriding  the built in setitem method. Allow parts of arrays from the class to be updated using square bracket notation, can handle both 1d and 2d arrays.
        if len(str(arg)) == 1:
            self.array[arg] = arg2
        else:
            x, y = arg
            self.array[x][y] = arg2

    def __repr__(self):
        # Method overriding  the built in repr method. Changes  the formatted printable representation returned for an object, formatted  to display arrays in a matrix layout.
        if self.__arrayDepth__(self.array) == 0:
            return MyArray.__formatArray1d__(self.array)
        else:
            return MyArray.__formatArray2d__(self.array)


ma1 = MyArray([5, 2])
ma2 = MyArray([[3, 3, 4, 5], [5, 6, 7, 8], [2, 3, 4, 5]])

print(ma2)
ma2.max()
ma2.max(axis=0)
ma2.max(axis=1)
print()
ma2.min()
ma2.min(axis=0)
ma2.min(axis=1)
print()
ma2.mean()
ma2.mean(axis=0)
ma2.mean(axis=1)

ma1[0] = 3
print(ma1[0])
print(repr(ma1))
print(repr(ma2))

ma1c = ma1.copy()
mac2 = ma2.copy()
ma1d = ma1
ma1[1] = 6
print(ma1d)
print(ma1c)
ma2d = ma2
ma2[1, 1] = 9
print(ma2d)
print(mac2)

z1 = MyArray.zeros(4)
print(z1)
z2 = MyArray.zeros(3, 7)
print(z2)

print(ma1[1])
ma1[1] = 0
print(ma1)

print(ma2)
print(ma2[1, 2])
ma2[1, 2] = 0
print()
print(ma2)

print(ma1)
print()
print(ma2)
