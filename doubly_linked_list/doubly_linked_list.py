"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
          self.head = new_node
          self.tail = new_node
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = None
        if self.head and self.head.next:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
        elif self.head and not self.head.next:
            value = self.head.value
            self.head = None
            self.tail = None
        self.length -= 1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
          self.head = new_node
          self.tail = new_node
        else:
          new_node.prev = self.tail
          self.tail.next = new_node
          self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = None
        if self.head and self.head.next:
          value = self.tail.value
          self.tail = self.tail.prev
          self.tail.next = None
        elif self.head and not self.head.next:
          value = self.tail.value
          self.head = None
          self.tail = None
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
          return
        value = node.value
        if node is self.tail:
          self.remove_from_tail()
        else:
          node.delete()
          self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head:
          if node == self.tail:
            return
          self.length -= 1
          if self.length == 2 and node == self.head:
            value = self.head.value
            self.head.value = self.tail.value
            self.tail.value = value
          elif self.length > 2 and node == self.head:
            self.add_to_tail(self.head.value)
            self.head = self.head.next
            self.head.prev = None
          else:
            current = self.head
            while current:
              if current == node:
                self.add_to_tail(current.value)
                # currentPrev = current.prev
                currentNext = current.next
                # currentPrev.next = current.next
                currentNext.prev = current.prev
                break
              current = current.next

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head:
          self.length -= 1
          if self.length == 1 and node == self.head:
            self.head = None
            self.tail = None
          elif self.length >= 2 and (node == self.head or node == self.tail):
            if node == self.head:
              self.head = self.head.next
              self.head.prev = None
            else:
              self.tail = self.tail.prev
              self.tail.next = None
          else:
            current = self.head
            while current:
              if current == node:
                current.prev.next = current.next
                current.next.prev = current.prev
                break
              current = current.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head:
          max_val = self.head.value
          if self.head.next:
            current = self.head
            while current:
              if current.value > max_val:
                max_val = current.value
              current = current.next
          return max_val
