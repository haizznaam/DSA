class DoublyNode:
    def __init__(self,data,pre = None,next = None):
        self.data = data
        self.pre = pre
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self, k):
        current = self.head
        for i in range(k):
            current = current.next
        return current.data

    def insert(self,k,val):
        insert_value = DoublyNode(val)
        if self.head is None:
            self.head = insert_value
        elif k == 0:
            insert_value.next = self.head
            self.head.pre = insert_value
            self.head = insert_value
        else:
            current = self.head
            for i in range(k - 1):
                current = current.next
            insert_value.next = current.next
            insert_value.pre  = current
            current.next = insert_value
        self.size += 1
    def remove_first(self):
        if self.head is None:
            raise Exception('List is Empty')
        remove_node = self.head
        self.head = self.head.next
        self.head.pre = None
        self.size -= 1
        return remove_node

    def remove_last(self):
        if self.head is None:
            raise Exception('List is Empty')
        current = self.head
        if current.next is None:
            self.head = None
            self.size -= 1
            return current
        while current.next is not None:
            current = current.next
        remove_node = current
        current.pre.next = None
        self.size -= 1
        return remove_node

    def __delitem__(self, k):
        if k == 0:
            return self.remove_first()
        elif k == self.size - 1:
            return self.remove_last()
        else:
            current = self.head
            for i in range(k-1):
                current = current.next
            remove_node = current.next
            current.next = remove_node.next
            remove_node.next.pre = current
            self.size -= 1
            return remove_node
    def reverse(self):
        current = self.head
        while current:
            temp = current.pre
            current.pre = current.next
            current.next = temp
            current = current.pre

        self.head = temp.pre
    def sort_by_value(self):
        if self.size < 2:
            return
        node = self.head
        while node.next :
            current = self.head

            while current.next:
                if current.data[1] < current.next.data[1]:
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp

                current = current.next

            node = node.next
        return


    def __repr__(self):
        node = self.head
        res = ''
        count = 0
        while node:
            res += "{}.  {:<5}  {:<5}".format(count, node.data[0], node.data[1]) + '\n'
            count += 1
            node = node.next
        return res

stock_codes = [('VNM ', 100.6) , ('HPG ', 46.05) , ('GAS ', 94) , ('MSN ', 86.8) ,
              ('FPT ', 75.7) , ('VIC ', 104.7) , ('VCB ', 94.3) ,('MWG ', 128.2) ,
              ('PNJ ', 83.2) , ('DHG ', 98.6)]
L = DoublyLinkedList()
for i in range(len(stock_codes)):
    L.insert(i,stock_codes[i])
print(L)

count = 0
while count < len(L):
    if L[count][1] < 80:
        del L[count]
        count -= 1
    count += 1
print(L)

L.insert(3,('VJC',101.2))
print(L)

L.reverse()
print(L)

L.sort_by_value()
print(L)

