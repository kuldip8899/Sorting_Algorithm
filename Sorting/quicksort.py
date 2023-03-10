# -*- coding: utf-8 -*-
"""quicksort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XU4C21tWTZBcnCiOjB7auhoJ3H84VK9C
"""

import time
import pandas as pd

def Sort_quick(A):

    elements = len(A)
    
    #Base case
    if elements < 2:
        return A
    
    current_position = 0   #Position of the partitioning element

    for i in range(1, elements):   #Partitioning loop
         if A[i] <= A[0]:
              current_position += 1
              temp = A[i]
              A[i] = A[current_position]
              A[current_position] = temp

    temp = A[0]
    A[0] = A[current_position] 
    A[current_position] = temp     #Brings pivot to it's appropriate position
    
    left = Sort_quick(A[0:current_position])           #Sorts the elements to the left of pivot
    right = Sort_quick(A[current_position+1:elements]) #sorts the elements to the right of pivot

    A = left + [A[current_position]] + right    #Merging everything together
    
    return A

# Reading the contents into an array
file20 = pd.read_csv('arr20.txt')
file100 = pd.read_csv('arr100.txt')
file1000 = pd.read_csv('arr1000.txt')
file4000 = pd.read_csv('arr4000.txt')

Array20 = [i[0] for i in file20.values.tolist()]
Array100 = [i[0] for i in file100.values.tolist()]
Array1000 = [i[0] for i in file1000.values.tolist()]
Array4000 = [i[0] for i in file4000.values.tolist()]

print("-----------------------------------Quick sort-----------------------------------------")
print("Unsorted Array of Random 20 numbers: ", Array20)

begin = time.process_time()             # Starting the stopwatch
sorted_Array20 = Sort_quick(Array20)     # Passing the Array20 into insertion sort algorithm
end = time.process_time()               # Ending the stopwatch
print('\nDuration for quick sorting array of 20 numbers : {}'.format(end - begin))
print('Sorted 20 Numbers: \t', sorted_Array20)

begin = time.process_time()
sorted_Array100 = Sort_quick(Array100)    # Passing the Array20 into quick sort algorithm
end = time.process_time()
print('\nDuration for quick sorting array of 100 numbers : {}'.format(end - begin))
print('Sorted 100 Numbers: \t', sorted_Array100)

begin = time.process_time()
sorted_Array1000 = Sort_quick(Array1000)  # Passing the Array20 into quick sort algorithm
end = time.process_time()
print('\nDuration for quick sorting array of 1000 numbers : {}'.format(end - begin))
print('Sorted 1000 Numbers: \t', sorted_Array1000)

begin = time.process_time()
sorted_Array4000 = Sort_quick(Array4000) # Passing the Array20 into quick sort algorithm
end = time.process_time()
print('\nDuration for quick sorting array of 4000 numbers : {}'.format(end - begin))
print('Sorted 4000 Numbers: \t', sorted_Array4000)