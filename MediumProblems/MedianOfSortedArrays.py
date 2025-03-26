def median_sorted_arrays( arr1: list[int], arr2 :list[int]) -> float:
    arr1L, arr2L, arr1P, arr2P, m1, m2 = len(arr1), len(arr2), 0, 0, 0, 0
    for count in range( (arr1L+arr2L)//2 + 1) :
        m2 = m1
        if arr1P < arr1L and arr2P < arr2L :
            if arr1[arr1P] > arr2[arr2P]:
                m1 = arr2[arr2P]
                arr2P += 1
            else :
                m1 = arr1[arr1P]
                arr1P += 1
        elif arr1P < arr1L :
            m1 = arr1[arr1P]
            arr1P += 1
        else :
            m1 = arr2[arr2P]
            arr2P += 1
    if (arr1L + arr2L) %2 == 1:
        return float(m1)
    else: 
        return (m1 + m2) / 2.0
    
print( median_sorted_arrays([1,3], [2]))
print( median_sorted_arrays([1,3], [2,4]))
