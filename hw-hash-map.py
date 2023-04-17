## Problem 1: Seperate Chaining Method
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class SepChainHash:
    def __init__(self, size):
        # self.cap = capacity
        self.size = size
        self.hash_table = [None] * self.size

    def hash(self, key):
        return hash(key) % self.size

    def add(self, key, val):
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is None:
            self.hash_table[hash_key] = Node((key,val))
        else:
            current = self.hash_table[hash_key]
            while current.next:
                current = current.next
            current.next = Node((key,val))
    def __getitem__(self, key):
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is not None:
            current = self.hash_table[hash_key]
            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next
        raise Exception('Invalid Key')
    def delete(self, key):
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is not None:
            current = self.hash_table[hash_key]
            prev_node = None
            while current:
                if current.data[0] == key:
                    if prev_node:
                        prev_node.next = current.next
                    else:
                        self.hash_table[hash_key] = current.next
                    return

                prev_node = current
                current = current.next

        raise Exception('Invalid Key')
    def __repr__(self):
        res = []
        for i in range(self.size):
            current = self.hash_table[i]
            if current is not None:
                list_nodes = []
                while current:
                    list_nodes.append(str(current.data))
                    current = current.next
                res.append(f"{i}: [{', '.join(list_nodes)}]")

            else:
                res.append(f"{i}. [{None}]")
        return '\n'.join(res)


hash_table = SepChainHash(5)
list_data = [ (6 , 'a') , (1 , 'b') , (12 , 'h') ,(10 , 'r') ,
              (6 , 'p') , (4 , 's') , (2 , 'n')]

for item in list_data:
    hash_table.add(item[0],item[1])

print(hash_table)

# print(hash_table[9])
print(hash_table[4])
hash_table.delete(6)
print(hash_table)
##########################################################################

## Problem 2: Linear Probing method

class LinProbHash:
    def __init__(self,size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self,key):
        return hash(key) % self.size

    def add(self,key,value,position = None):
        if position is None:
            position = self.hash(key)

        if position < self.size:
            if self.hash_table[position] is None:
                self.hash_table[position] = Node((key,value))
                return

            else:
                self.add(key, value, position + 1)
        else:
            raise Exception("There is no position to add value")

    def __getitem__(self, key):
        hash_key = self.hash(key)
        if self.hash_table[hash_key].data[0] == key:
            return self.hash_table[hash_key].data[1]
        raise Exception('Invalid key')

    def delete(self,key):
       for i in range(self.size):
           if self.hash_table[i] is not None and self.hash_table[i].data[0] == key:
               self.hash_table[i] = None
               return

       raise Exception('Invalid key')

    def __repr__(self):
        res = []
        for i in range(self.size):
            if self.hash_table[i]:
                res.append(f"{i}. {self.hash_table[i].data}")
            else:
                res.append(f"{i}. {None}")
        return '\n'.join(res)

data = [ (6 , 's') , (3 , 'd') , (11 , 'a') , (19 , 'p') ,
         (8 , 'd') , (14 , 'q') ]

H = LinProbHash(8)
for item in data:
    H.add(item[0],item[1])

print(H)
H.delete(11)
H.delete(3)
H.add(16,'l')
H.add(0,'o')
H.add(9,'a')
H.delete(8)
print(H)