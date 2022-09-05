

# list1 = [4,8,9,-1,10]

# list1.sort(reverse=True)
# print(list1)



def selctionsort(li):
    for i in range(len(li)-1):
        min_index = i
        for j in range(i+1,len(li)):
            if li[min_index] > li[j]:
                min_index=j
        if min_index != i :
            li[i],li[min_index] = li[min_index], li[i]
    return li


if __name__ == "__main__" :
    li =[4,6,1,10,7,-1,100,15,30,15]
    selctionsort(li)
