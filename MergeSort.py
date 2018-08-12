def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):

            #print("lefthalf",lefthalf[i])
            #print("righthalf",righthalf[j])
            #print("i",i)
            #print("j",j)
            #print("k",k)

            if lefthalf[i] < righthalf[j]:
                #print("lefthalf",lefthalf[i])
                #print("righthalf",righthalf[j])
                alist[k]=lefthalf[i]
                #print("righthalf is bigger",alist[k])
                i=i+1
            else:
                #print("lefthalf",lefthalf[i])
                #print("righthalf",righthalf[j])
                alist[k]=righthalf[j]
                #print("righthalf is smaller",alist[k])
                j=j+1

            k=k+1
            #print("i",i)
            #print("j",j)
            #print("k",k)

        while i < len(lefthalf):
            #print("New While loop lefthalf",lefthalf[i])
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            #print("i",i)
            #print("j",j)
            #print("k",k)

        while j < len(righthalf):
            #print("New While loop righthalf",righthalf[j])
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            #print("i",i)
            #print("j",j)
            #print("k",k)
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
