import math
from time import time

print('Введите числа, требующие сортировки, через запятую')
strInput = input()
massif = strInput.split(',')

for integer in massif.copy():
    try:
        integer = int(integer)
    except ValueError:
        massif.remove(integer)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"       

def bubble_sort(arr):
    '''
    Sort given array via Buuble Sort
    '''
    n = 1

    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        n += 1

    return arr


def gnome_sort(arr):
    '''
    Sort given array via Gnome Sort
    '''
    i = 1

    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr


def bucket_sort(arr, bucketSize=3, ascending=True):
    '''
    Sort given array via Bucket Sort
    '''
    if len(arr) == 0: return arr
   
    if type(arr[0]) == type(str()):
        for i in range(0, len(arr)):
            arr[i] = int(arr[i])

    minValue = arr[0]; maxValue = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minValue: minValue = arr[i]
        elif arr[i] > maxValue: maxValue = arr[i]

    # Формирование блоков
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Распределение элементов массива по блокам 
    for i in range(0, len(arr)):
        buckets[math.floor((arr[i] - minValue) / bucketSize)].append(arr[i])

    # Сортирвка элементов внутри блоков и возвращение их в основной массив
    arr = []
    for i in range(0, len(buckets)):
        buckets[i] = bubble_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            arr.append(buckets[i][j])
    return arr


#Heapsort
def swap(i, j, arr): 
    '''
    Swaps array elements
    '''                   
    arr[i], arr[j] = arr[j], arr[i] 


def heapify(end,i, arr):
    '''
    Swaps in case 
    '''   
    l = 2 * i + 1  
    r = 2 * (i + 1)   
    maxValue = i   

    if l < end and arr[i] < arr[l]:   
        maxValue = l   
    if r < end and arr[maxValue] < arr[r]:   
        maxValue = r   
    if maxValue != i:   
        swap(i, maxValue, arr)   
        heapify(end, maxValue, arr)  
     

def heap_sort(arr):     
    '''
    Sort given array via Pyramid Sort
    '''
    end = len(arr)   
    start = math.floor(end/2 - 1)

    for i in range(start, -1, -1): heapify(end, i, arr)   
    
    for i in range(end-1, 0, -1):   
        swap(i, 0, arr)   
        heapify(i, 0, arr) 

    return arr  


def JoinNums(array):
    '''
    Turn every array element into a string, then joins them into a string
    '''
    for i in range(0, len(array)):
        array[i] = str(array[i])

    return ", ".join(array)

tic = time()
print('\n\nМетод сортировки - пузырьковый: '+JoinNums(bubble_sort(massif)))
toc = time()
print('\nВремя выполнения пузырьковой сортировки: ', toFixed((toc - tic)*1000,2), 'ms')

tic = time()
print('\n\nМетод сортировки - гномий: '+JoinNums(gnome_sort(massif)))
toc = time()
print('\nВремя выполнения гномий сортировки: ', toFixed((toc - tic)*1000,2), 'ms')

tic = time()
print('\n\nМетод сортировки - блочный: '+JoinNums(bucket_sort(massif)))
toc = time()
print('\nВремя выполнения блочной сортировки: ', toFixed((toc - tic)*1000,2), 'ms')

tic = time()
print('\n\nМетод сортировки - пирамидальный: '+JoinNums(heap_sort(massif)))
toc = time()
print('\nВремя выполнения пирамидальной сортировки: ', toFixed((toc - tic)*1000,2), 'ms')
