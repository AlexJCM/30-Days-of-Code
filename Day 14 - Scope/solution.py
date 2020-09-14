class Difference:
    def __init__(self, a):
        self.__elements = a

    # Solution 1
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)
        #self.maximumDifference = max(a) - min(a)

    # Solution 2
    # def computeDifference(self):
    #     maximum = 0
    #     for i in range(len(self.__elements)):
    #         for j in range(i, len(self.__elements)-1):
    #             abs_value = abs(self.__elements[i] - self.__elements[j+1])
    #             if (abs_value > maximum):
    #                 maximum = abs_value

    #     self.maximumDifference = maximum
