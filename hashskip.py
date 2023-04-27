from typing import Any, Optional
import sys
from skiplist import SkipList
# coding influenced by ODS book

class Chainedhashtable:
    def __init__(self) -> None:
        self.n=0                                                    #initial number of elements added to the set
        self.k = 1                                                  #to keep track of 2^k for resize purposes (many hash functions only work for sizes of 2's power)
        self.table=[None]*(2**self.k)                               #initial table
    
    def _hash_(self, x):
        return (hash(x)%len(self.table))                #hashing the value and taking mod with the size
    
    def __setitem__(self, key, value):
        i = self._hash_(key)                     #hash value calculation
        if self.table[i] is not None:            #if skiplist exists
            self.table[i].insert((key,value))    #add to it
            self.n=self.n+1
        else:                                    #if skiplists is exists
            self.table[i] = SkipList()           #new skiplist
            self.table[i].insert((key,value))    #insert new key,value pair
            self.n=self.n+1
        if type(self.table[i])==SkipList:
            if self.table[i].size()>len(self.table):
                self.resize()                        #if new size of skiplist is greater than the hashtable, resize and rehash 
        elif self.n > len(self.table)*0.75:        # check resize need       IMPLEMENT  load factor = 0.75
            self.resize()

    def resize(self) -> None:
        self.k = 1                                       #reinitializing k for new size
        while (1 << self.k) <= self.n:                   #finding the lowest value of k such that 2^k > n
            self.k += 1 
        oldtable = self.table                            #storing table into oldtable
        self.table=[None]*(2**self.k)                    #reinitializing new table
        self.n=0                                         #reinitializing n so the add function doesn't increment n twice 
        for skip in oldtable:
            if skip:                            #checks if skiplist at an index exists
                items=skip._items_()            #gets the items in the skiplist
                for i in items:   
                    if len(i)!=0:            
                        self.__setitem__(i[0],i[1]) #adds them to the table

    def _find_(self, key) -> bool:
        i = self._hash_(key)                            #Takes hash(element) and searches on skiplist in that index
        found=None
        if type(self.table[i])==SkipList:               #checking if there is a skiplist at the hashed index 
            found=self.table[i].find(key)               #calls skiplist function to find the key in the skiplist
            if found:                                   #checks if the value is found
                return found                            #returns the found data (key,value) pair
        return False                                    #didnt find the key

    def items(self) -> [(Any, Any)]:
        items=[]                                      
        for element in self.table:                    #iterating over the chains  in the table
            if type(element)==SkipList:               #checking if there is a skiplist at the hashed index 
                items.append(element._items_())       #adds its items
        return items                                  #returns list of all (key,value) pairs
    
    def discard(self, key) -> Any:
        if 3 * self.n < len(self.table): 
            self.resize() 
            # resize as per ODS
        i = self._hash_(key)
        # hash value calculation
        if type(self.table[i])==SkipList and self.table[i].find(key)[0] == key:      # searches the skiplist at the index in O(1 + logn) complexity
            self.table[i].remove(key)           #removes from skiplist
            # print(self.table[i].items())
            self.n -= 1                         #decrements number of elements
            return True                         #element deleted
        return None                             #not done

    def clear(self) -> None:
        self.k = 1                                      #reinitializing k 
        self.table=[[None]*(2**self.k)]                     #initial table
        self.n=0                                        #setting no. of elements to 0





####### Trial code: Another implementation 

    
    # def __init__(self):
    #     self.size = 10  #initial size of the hashtable
    #     self.elements = 0 #number of elements stored in hastable
    #     objects = {None}  #a dictionary of objects where every index of hashtable is key to which a skiplist is attached
    #     for x in range (10):
    #         objects[x] = SkipList()
    
    # def _hash_(self, element: Any) -> int: #returns hash value
    #     hash_value = element % self.size
    #     return hash_value
    
    # def _find_(self, element: Any) -> bool: 
    #     index = self._hash_(element) 
    #     #Takes hash(element) and searches on skiplist in that index
    #     self.objects[index].find(element)
    #     return self.objects[index].find(element)
    
    # def resizeup(self) -> None:
    #     self.size = self.size*2
    #     for x in range(self.size // 2, self.size): #since objects is a dictionary, we just increase the dictionary
    #         self.objects[x] = SkipList
            
    # def resizedown(self) -> None:
    #     pass

    # def add(self, data: (Any,Any)) -> bool:
    #     if self.elements + 1 > (self.size*0.75):
    #         self.resize() 
    #     # check resize need
    #     index = self._hash_(data[0]) 
    #     if self.objects[index].find(data[0]) == None: 
    #         # not found
    #         #hash value calculation
    #         self.objects[index].insert(data)
    #          #append element
    #         self.elements += 1 
    #         #Increment no of elements
    #         return True # adding happened
    #     return False # add nahi hua
    
    # def discard(self, element: Any) -> Any:
    #     if 3 * self.elements < self.size: 
    #         self.resizedown() 
    #         # resize as per ODS
    #     index = self._hash_(element) 
    #     # hash value calculation
    #     if self.objects[index].find(element) == element: 
    #         # item is the one to be deleted
    #         self.objects[index].remove(element)
    #         #removal happens
    #         self.elements -= 1 
    #         # no of elements decrease
    #         return True # done 
    #     return None #not done

    # def __iter__(self) -> Any: # iteration
    #     pass

