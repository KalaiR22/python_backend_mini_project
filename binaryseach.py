def binary_search(list,search_element):
    start = 0
    middle=0
    end=len(list)
    steps = 0

    while start<=end:
        print("step",steps,":",str(list[start:end+1]))
        steps=steps+1
        middle=(start+end)//2

        if(search_element==list[middle]):
            return middle
        if(search_element<list[middle]):
            end= middle-1
        if(search_element>list[middle]):
            start= middle+1
    return -1

list=[1,2,3,4,5,6,7]
search_element=3
binary_search(list,search_element)