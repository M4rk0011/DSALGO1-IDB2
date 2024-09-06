''''
#insertion sort
array1 = [10, 2, 3, 1, 1, 4, 89, 21]
print( array1)
for i in range(1, len(array1)):
    key = array1[i]
    j = i - 1

    while j >= 0 and key < array1[j]:
        array1[j + 1] = array1[j]
        j -= 1

    array1[j + 1] = key

print(array1)


array2 = [10, 2, 3, 1, 1, 4, 89, 21]
for i in range(len(array2)):
    mid_indx = i
    for j in range(i + 1, len(array2)):
        if array2[mid_indx] > array2[j]:
            mid_indx = j
    array2[i], array2[mid_indx] = array2[mid_indx], array2[i]
print(array2)
#bubble sort
array3 = [10, 2, 3, 1, 1, 4, 89, 21]
print("Arr3 values before bubble sort")
print(array3)

for i in range(len(array3)):
    for j in range(0, len(array3) - i - 1):
        if array3[j] > array3[j+1]:
            array3[j], array3[j+1] = array3[j+1], array3[j]

print("Arr3 values after bubble sort")
print(array3)


'''
#1
Arr1 = [23, 89, 7, 56, 44]

print("Unsorted Array 1")
print(Arr1)
n = len(Arr1)
for i in range (n):
    for j in range(0,n-i-1):
        if (Arr1[j] > Arr1[j+1]):
              Arr1[j], Arr1[j+1] = Arr1[j+1],Arr1[j]
print("Sorted Array 1")
print(Arr1)
print("====================================================")
#2
Arr2 =[12, 78, 91, 34, 62]
print("Unsorted Array 2")
print(Arr2)
for i in range (1,len(Arr2)):
    key = Arr2[i]
    j=i-1
    while j >= 0 and key <Arr2[j]:
        Arr2[j+1]=Arr2[j]
        j-=1
        Arr2[j +1]=key
print("Sorted Array 2")
print(Arr2)
print("=====================================================")

#3
Arr3 =[5, 99, 48, 15, 67]
print("Unsorted Array 3")
print(Arr3)
for i in range(len(Arr3)):
    min_idx =i
    for j in range(i+1, len(Arr3)):
        if Arr3[min_idx] < Arr3[j]:
            min_idx = j - 1
            Arr3[i],Arr3[min_idx + 1] = Arr3[min_idx +1 ],Arr3[i]
print(" Sorted Array 3")
print(Arr3)
print("=====================================================")


#4
Arr4 =[38, 82, 25, 74, 13]
print(" Unsorted  Array 4")
print(Arr4)
for i in range (1,len(Arr4)):
    key = Arr4[i]
    j=i-1
    while j >= 0 and key > Arr4[j]:
        Arr4[j+1]=Arr4[j]
        j-=1
        Arr4[j +1]=key
print("Sorted Array 4")
print(Arr4)
print("=======================================================")


#5
Arr5 = [7,56, 91, 34, 48, 25, 74]
print("The Unsorted values Of The Array 5")
print(Arr5)
print()
for i in range (1,len(Arr5)):
    key = Arr5[i]
    j=i-1
    while j >= 0 and key <Arr5[j]:
        Arr5[j+1]=Arr5[j]
        j-=1
        Arr5[j +1]=key
print("The Sorted Values of The Array 5 in Ascending ORDER")
print(Arr5)
for i in range (1,len(Arr5)):
    key = Arr5[i]
    j=i-1
    while j >= 0 and key >Arr5[j]:
        Arr5[j+1]=Arr5[j]
        j-=1
        Arr5[j +1]=key
print("The Sorted Values of The Array 5 in Decending ORDER")
print(Arr5)
print("=======================================================")


#no 6
Arr6=[23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("item number 1 to 4 array 6: ")
print(Arr6)
for i in range(len(Arr6)):
    min_idx = i
    for j in range(i+1, len(Arr6)):
        if Arr6[i] > Arr6[j]:
            min_idx = j
            Arr6[i], Arr6[min_idx] = Arr6[min_idx],Arr6[i]
print("Sorted Ascending ORDER")
print(Arr6)
print("=======================================================")

#7
even = []
odd = []

for number in Arr6:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print("Even :", even)
print("Odd values:", odd)\

print("=======================================================")

