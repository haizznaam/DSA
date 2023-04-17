class Node:
    def __init__(self, data,next = None):
        self.data = data
        self.next = next

    def update_score(self, new_score):
        list_data = list(self.data)
        list_data[1] = new_score
        self.data = tuple(list_data)

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
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
        insert_value = Node(val)
        if self.head is None:
            self.head = insert_value
        elif k == 0:
            insert_value.next = self.head
            self.head = insert_value
        else:
            current = self.head
            for i in range(k-1):
                current = current.next
            insert_value.next = current.next
            current.next = insert_value
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            removed_node = self.head
            self.head = removed_node.next
            self.size -= 1
            return removed_node

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        elif self.size == 1:
            return self.remove_first()
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            removed_node = current_node
            current_node = None
            self.size -= 1
            return removed_node

    def __delitem__(self, k):
        if k < 0 or k >= self.size:
            raise IndexError("Index out of range")
        elif k == 0:
            return self.remove_first()
        elif k == self.size - 1:
            return self.remove_last()
        else:
            current = self.head
            for i in range(k-1):
                current = current.next
            remove_node = current.next
            current.next = remove_node.next
            self.size -= 1
            return remove_node

    def delete_by_value(self, val):
        remove_list = []
        current = self.head
        count = 0
        while current:
            if val in current.data:
                remove_list.append((self.__delitem__(count).data))
                count -= 1
            current = current.next
            count += 1
        return remove_list

    def search(self, val):
        search_list = []
        current = self.head
        for i in range(self.size):
            if val in current.data:
                search_list.append((i,self.__getitem__(i)))
            current = current.next

        if len(search_list) != 0:
            return search_list
        else:
            return "Value is not found"

    def update(self, k, val):
        if not isinstance(k,int):
            return "Update false. Can only update score"
        current = self.head
        for i in range(k):
            current = current.next
        old = current
        res = f"Update: {str(old)}"
        current.update_score(val)
        res += f" -->  {str(current)}"
        return res

    def __repr__(self):
        res = ''
        current_node = self.head
        while current_node is not None:
            res += f"{current_node.data} "
            current_node = current_node.next
        return res

    def remove_duplicate(self):
        current = self.head
        seen = set()
        seen.add(self.head.data)
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

    def reverse(self, start, k):
        count = 0
        pre_node = None
        current_node = start
        while count < k:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node
            count += 1
        start = pre_node

    def reverseByGroup(self,k):
        node = self.head
        length = self.size
        while node:
            if length > k:
                self.reverse(node,k)
                length -= k
                node = node.next
            else:
                self.reverse(node,length)
                break

num_list = [1,2,3,4,5,6,7,8]
l = SinglyLinkedList()
for i in range(len(num_list)):
    l.insert(i,num_list[i])
print(l)

l.reverseByGroup(3)
print(l)

