#Merge 2 sorted arrays. Assume arrays are already sorted, increase the length of first array by the same number of 2nd array and then compare items in the array one by one. 
# Use a new counter to store the compared values
def MergeSortedArray(lista,m,listb,n):
   
    i = m-1
    j = n-1
    k = m+n-1

    while j>=0:
        if i>=0 and lista[i] >= listb[j]:
            lista[k] = lista[i]
            i = i-1
        else:   
            lista[k] = listb[j]
            j = j-1
        k=k-1
    print(lista)
    print(listb)

lista = [1,3,5,0,0,0]
listb = [2,4,7,9]
MergeSortedArray(lista,3,listb,3)