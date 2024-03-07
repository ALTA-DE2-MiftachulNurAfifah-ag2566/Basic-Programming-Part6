def remove_duplicates(array):
    for i in range(len(array) - 1, 0, -1):
        if array[i] == array[i - 1]:
            array.remove(array[i])
    
    return len(array)

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4