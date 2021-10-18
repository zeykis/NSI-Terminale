#def merge(L1,L2):
#    T=["AAAA" for i in range (len(L1)+len(L2))]
#    i1=i2=j=0
#    while i1<len(L1) and i2<len(L2):
#        if L1[i1]<=L2[i2]:
#            T[j]=L1[i1]
#            i1+=1
#        else:
#            T[j]=L2[i2]
#            i2+=1
#        j+=1
#    while i1<len(L1):
#        T[j]=L1[i1]
#        i1+=1
#        j+=1
#    while i2<len(L2):
#        T[j]=L2[i2]
#        i2+=1
#        j+=1
#    return T
#
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
