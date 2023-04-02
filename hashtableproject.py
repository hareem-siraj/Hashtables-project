from typing import Any, Optional
import random
import sys
import math

# coding influenced by ODS book


class Chainedhashtable:
    
    def __init__(self):
        self.size = 10  #initial size of the hashtable
        self.elements = 0 #number of elements stored in hastable
        objects = {None}  #a dictionary of objects where every index of hashtable is key to which a skiplist is attached
        for x in range (10):
            objects[x] = SkipList
    
    def _hash_(self, element: Any) -> int: #returns hash value
        hash_value = element % self.size
        return hash_value
    
    def _find_(self, element: Any) -> bool: 
        index = self._hash_(element) 
        #Takes hash(element) and searches on skiplist in that index
        self.objects[index].find(element)
        return self.objects[index].find(element)
    
    def resizeup(self) -> None:
        self.size = self.size*2
        for x in range(self.size // 2, self.size): #since objects is a dictionary, we just increase the dictionary
            self.objects[x] = SkipList
            
    def resizedown(self) -> None:
        pass

    def add(self, data: (Any,Any)) -> bool:
        if self.elements + 1 > (self.size*0.75):
            self.resize() 
        # check resize need
        index = self._hash_(data[0]) 
        if self.objects[index].find(data[0]) == None: 
            # not found
            #hash value calculation
            self.objects[index].insert(data)
             #append element
            self.elements += 1 
            #Increment no of elements
            return True # adding happened
        return False # add nahi hua
    
    def discard(self, element: Any) -> Any:
        if 3 * self.elements < self.size: 
            self.resizedown() 
            # resize as per ODS
        index = self._hash_(element) 
        # hash value calculation
        if self.objects[index].find(element) == element: 
            # item is the one to be deleted
            self.objects[index].remove(element)
            #removal happens
            self.elements -= 1 
            # no of elements decrease
            return True # done 
        return None #not done

    def __iter__(self) -> Any: # iteration
        pass



class Node(object):
    '''A node in a skiplist. It stores a (key, value) pair along with pointers
    for each level in its tower.

    The key is used to compare nodes. The tower automatically includes level 0.    '''
    data = (None,None)
    def __init__(self, data: (Any, Any)=(None,None), height: int=0) -> None:
        '''Construct node with given data and of given height.       
          The height is the largest level, starting from 0, of the tower.
        Parameters:
        - self: mandatory reference to this object
        - data: the (key, value) pair to store in this node
        - height: the number of levels in the tower (excludes level 0)        Returns:
        None
        '''
        self.data=data      #initailizes data tuple 
        self.height=height  #initailizes height of the node
        self.forwards=[None]*(height+1)      #to store pointers for each level of the node
        return 

    def __repr__(self) -> str:
        '''Returns the representation of this node.
        Implement any representation that helps you debug.
        Parameters:
        - self: mandatory reference to this object
        Returns:        this node's string representation.'''
        strng = ''
        strng = (str(self.data[0]) +' '+ str(self.data[1]) + ' ') * (self.height) #representation for debuggin 
        return strng #to print

    def __str__(self) -> str:
        '''Returns a string representation of this node.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this node's string representation.
        '''
        return self.__repr__()  #calling repr for representing string
    
    # def height(self) -> int:
    #     '''Returns the height of this node's tower.
    #     The height is the largest level, starting from 0, of the tower.

    #     Parameters:
    #     - self: mandatory reference to this object

    #     Returns:
    #     the height of this node's tower.
    #     '''
    #     return self.height

    def key(self) -> Any:
        '''Returns the key stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the key stored in this node.
        '''
        return self.data[0] #key of (key , value )

    def value(self) -> Any:
        '''Returns the value stored in this node.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the value stored in this node.
        '''
        return self.data[1] #value of (key , value )

    def add_level(self, forward: Optional ['Node'] = None) -> None:        #     changed Node to Any
        '''Adds a level to this node which points to forward.

        Parameters:
        - self: mandatory reference to this object
        - forward: the node that this node will point to in the new level.

        Returns:
        None.        '''
        self.height=self.height+1       #adds height 
        self.forwards[-1]=forward       #the node thie new level points to 
        return 

class SkipList(object):
    '''A skiplist of nodes containing (key, value) pairs. Nodes are ordered
    according to keys. Keys are unique, reinserting an existing key overwrites
    the value.    The skiplist contains a sentinel node by default and the height of the
    sentinel node is the height of the list.    '''
    def __init__(self) -> None:
        '''Construct empty skiplist        Parameters:
        - self: mandatory reference to this object
        Returns:        None '''
        self.senti = Node((math.inf,''),0)  #sentinel value key is infinity and height initially 0
        return
        
    def __len__(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        dunder method allows calling len() on this object.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        temp = self.senti       #starting traversal
        l=0     
        while (temp.forwards[0]!=None): #until next pointer at 0th level is none, i.e, skiplist ended 
            temp=temp.forwards[0]
            l+=1 #inc l
        return l

    def __repr__(self) -> str:
        '''Returns a string representation of this skiplist.
        Implement any representation that helps you debug.
        Parameters:
        - self: mandatory reference to this object
        Returns:
        this skiplist's string representation.'''
        s = ''
        temp = self.senti       #starting node for traversal
        while (temp.forwards[0]!=None):     
            s+=(temp.__repr__())        #calls node's repr method and uses it to represent the skiplist
            s+='\n'
            temp=temp.forwards[0]       #continues traversal
        s+=(temp.__repr__())
        return s
    
    def __str__(self) -> str:
        '''Returns a string representation of this skiplist.

        See the link below for the difference between the __repr__ and __str__
        methods: https://www.geeksforgeeks.org/str-vs-repr-in-python/

        Parameters:
        - self: mandatory reference to this object

        Returns:
        this skiplist's string representation.
        '''
        return self.__repr__() #calls repr to represent str 

    def _search_path(self, key: Any) -> [Node]:
        '''Returns the search path in this skiplist for key.

        The search path contains one node for each level of the skiplist
        starting from the highest and ending at level 0. The node for each
        level is the one corresponding to a descend in the search path.
        
        Parameters:
        - self: mandatory reference to this object
        - key: the key being searched for
        
        Returns:
        the descend nodes at each level of the skiplist, ordered from highest
        level to level 0.        '''
        Path =[Node]       #to have a record of the traverdal
        temp = self.senti
        for i in range(self.height(), -1, -1):
            Path.append(temp)       #storing nodes at each level of the traversal
            while(temp.forwards[i] and temp.forwards[i].key() < key):
                temp = temp.forwards[i]
        return Path

    def _find_prev(self, key: Any) -> Node:
        '''Returns the node in the skiplist that contains the predecessor key.
        Parameters:
        - self: mandatory reference to this object
        - key: the key being searched for

        Returns:
        the node in the skiplist that contains the predecessor key.'''
        if (self.find(key)==None):
            return
        temp = self.senti       #starting traversal
        for i in range(self.height(), -1, -1):
            while(temp.forwards[i] and temp.forwards[i].key() < key):
                temp = temp.forwards[i]
        return temp

    def reset(self) -> None:
        '''Empty the skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:

        None
        '''
        self.__init__()
        return

    def height(self) -> int:
        '''Returns the height of the skiplist.

        The height is the largest level of the sentinel's tower.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the height of this skiplist.
        '''
        return self.senti.height#sentinel height is skiplists height
    
    def find(self, key: Any) -> Optional[Any]:
        '''Returns the value stored in this skiplist corresponding to key, None
        if key does not exist in this skiplist.

        Parameters:
        - self: mandatory reference to this object
        - key: the key whose value is sought
        
        Returns:
        the stored value for key, None if key does not exist in this skiplist.
        '''
        temp = self.senti
        for i in range(self.height(), -1, -1):
            while(temp.forwards[i] and temp.forwards[i].key() < key):
                temp = temp.forwards[i]
        temp= temp.forwards[0]  #this is either desired node or the successor of the key to be found
        if temp and temp.key() == key:    #if matches return the value
            return temp.value()
        return None #not found
  
#  ---------------------
    def find_range(self, key1: Any, key2: Any) -> [Any]:
        '''Returns the values stored in this skiplist corresponding to the keys
        between key1 and key2 inclusive in sorted order of keys.

        Parameters:
        - self: mandatory reference to this object
        - key1: starting key in the range of keys whose value is sought
        - key2: ending key in the range of keys whose value is sought

        Returns:
        the stored values for the keys between key1 and key2 inclusive in sorted
        order of keys.
        '''
        if self.find(key1)==None or self.find(key2)==None:
            return
        start = self._find_prev(key1)                 #exclusive
        values = []
        while (start.forwards[0]!=None and start.forwards[0].key()<=key2):  #runs until the forward node of key1 is not none and the key is less than or equals to key2
            values.append(start.forwards[0].value())        #appends the value of the key in the path inclusive
            start=start.forwards[0] #next
        return values   #returns the range of values
    
    def remove(self, key: Any) -> Optional[Any]:
        '''Returns the value stored for key in this skiplist and removes
        (key, value) from this skiplist, returns None if key is not stored in
        this skiplist.

        Parameters:
        - self: mandatory reference to this object
        - key: the key to be removed

        Returns:
        the stored value for key in this skiplist, None if key does not exist
        in this skiplist
        '''
        travers = [None]*(self.height()+1)      #to keep track of the traversal
        temp = self.senti   #starting node
        for i in range(self.height()+1, -1, -1):        #top down
            while(temp.forwards[i] and temp.forwards[i].key() < key):   #until the level is 0 or the forward is greater than or equals to the current node, keep moving forward
                temp = temp.forwards[i]         #next
            travers[i] = temp   #same fucntion as current in insert
        temp = temp.forward[0]  #prev's forward is the position to be removed 
        if temp != None and temp.key == key:
            for i in range(self.level+1):
                if travers[i].forwards[i] != temp:
                    break
                travers[i].forwards[i] = temp.forwards[i]
            # Remove levels having no elements
            while(self.height()>0 and self.senti.forwards[self.senti.height-1]==None):
                self.senti.height -= 1
            return temp.value()
        return None 

    def insert(self, data: (Any,Any)) -> None:
        '''Inserts a (key value) pair in this skiplist, overwrites the old value if key already exists.
        Parameters:        - self: mandatory reference to this object - data: the (key, value) pair
        Returns:        None        '''
        traverse = [None]*int(self.height()+1) # the traversal will be atheight
        current = self.senti        #starting node is sentinel, current will shift to find insertion position
        for i in range(self.height(), -1, -1):  #0 inclusive
            while current.forwards[i]!=None and current.forwards[i].key()<data[0]:  #until the level is 0 or the forward is greater than or equals to the current node, keep moving forward
                current = current.forwards[i]   #next on the same level
            traverse[i] = current   #keeping a record of all the nodes in the traversal where level changes
        current = current.forwards[0]      #the same key node or sucessor
        if current != None and current.key()==data[0]:  #key already exists
            current.data=data   #updates value
            return
        elif current is None or current.key()!=data[0]: #new key is being inserted
            rr = 0  #random value
            h=0     #height
            while (rr!=1):   #for height of new node — heads tail analogy: 0 is for heads 1 is for tails
                rr = random.randint(0,1)        #generates random numbers 0 or 1
                h+=1        #inc height in case of 0
            n = Node (data,h)   #creating new node
            if h>self.height():     #in case new height exceed height of existing skiplist
                for i in range(self.height()+1,h+1):    #from old height to new height
                    self.senti.forwards.append(None)      #incrementing sentinal's height because it is also skiplist's height
                    traverse.append(None)       #appending traverse for later use in asigning pointers
                    self.senti.height+=1        #inc sentinal nodes' height attribute
                    traverse[i]=self.senti      #initailizing new traverse indices with sentinnal node 
            for i in range(h+1):                      #linking pointers at each level of the new node
                n.forwards[i]=traverse[i].forwards[i]      #assigning n's forwards to traverse's forwards 
                traverse[i].forwards[i] = n               #assigning prev pointers going through to n 
        return


    
    def size(self) -> int:
        '''Returns the number of pairs stored in this skiplist.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        the number of pairs stored in this skiplist.
        '''
        # assuming that it means the number of nodes
        size=1
        temp=self.senti #for traversal
        while (temp.forwards[0]!=None):     #until traversal on level 0 is at the end  
            temp=temp.forwards[0]   #next 
            size+=1 #inc size
        return size
    
    def is_empty(self) -> bool:
        '''Returns whether the skiplist is empty.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        True if no pairs are stored in this skiplist, False otherwise.
        '''
        if self.__len__()==0:   #if length is 0, skiplist is empty 
            return True
        return False    #if length is not 0, its not empty, negative cant be possible



