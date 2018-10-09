# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 01:40:49 2018

@author: johor
"""
import math
class RadixSort:

# A function to do counting sort of arr[] according to
# the digit represented by exp.
    def countingSort(self,arr, exp1):
  
        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = math.floor(arr[i]/exp1)
            count[ (index)%10 ] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1,10):
            count[i] += count[i-1]

        # Build the output array
        i = n-1
        while i>=0:
            index = math.floor(arr[i]/exp1)
            output[ count[ (index)%10 ] - 1] = arr[i]
            count[ (index)%10 ] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0,len(arr)):
            arr[i] = output[i]

    # Method to do Radix Sort
    def radixSort(self,arr):

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1/exp > 0:
            self.countingSort(arr,exp)
            exp *= 10





test2 = RadixSort()

iinput = [125,100,478,634,258,741,745,123,954,6,158,463,248,777,639,143]
print("input")
print(iinput)
test2.radixSort(iinput)

print(iinput)
