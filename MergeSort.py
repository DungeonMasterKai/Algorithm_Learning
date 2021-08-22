def sort(slist):
    a = slist[0]
    b = slist[1]
    if a > b:
        return [b, a]
    else:
        return [a, b]

def merge(lista, listb):
    new_list = []
    i = 0
    j = 0
    while len(new_list) < len(lista) +len(listb):
        if len(lista) == i:
            new_list = new_list + listb[j:]
        elif len(listb) == j:
            new_list = new_list + lista[i:]
        elif lista[i]<listb[j]:
            new_list.append(lista[i])
            i+=1
        else:
            new_list.append(listb[j])
            j+=1
    return new_list



def mergesort(total_list):
    list_len = len(total_list)
    if len(total_list)>=2:
        first_half = total_list[:list_len//2]
        second_half = total_list[list_len//2:]
        sorted_first_half = mergesort(first_half)
        sorted_second_half = mergesort(second_half)
        sorted_total_list = merge(sorted_first_half, sorted_second_half)
        return sorted_total_list
    elif len(total_list) == 1:
        return total_list

print(mergesort([1, 5, 9, 10, 20, 23, 4, 3, 5]))


