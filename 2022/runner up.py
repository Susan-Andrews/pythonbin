#hackerrank 
if __name__ == '__main__':
    n = int(input())            # reads the input string
    arr = map(int, input().split())      # converts into a list
    arrnew=list(arr)                     
    res = [*set(arrnew)]                 # This is the fastest and smallest method to achieve a particular task. It first removes the duplicates and returns a dictionary which has to be converted to list. 
    y=max(res)
    res.remove(y)
    x=max(res)
    print(x)
    
    
    
    # map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    # The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) 
