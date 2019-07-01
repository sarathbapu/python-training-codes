import itertools

def sprint(x):
    '''
    Special Print 
    :param x: Any iterable or not will be printed
    '''
    for c in x :
        try :
            for v in c :
                print (v, end=" " )
        except :
            print(c)
        print("")

if __name__ == "__main__" :
    list1 = [ 1, 2, 3, 4, 5]
    list2 = [ 'a', 'b', 'c', 'd']
    
    print("Zip")
    sprint(zip(list1,list2))
    print("Product")
    sprint(itertools.product(list1,list2))   
    print("Combination")
    sprint(itertools.combinations(list2,3)) 
    print("Permutations")
    sprint(itertools.permutations(list2,3))
    print("PowerSets")
    #sprint(itertools.powerset(list1))