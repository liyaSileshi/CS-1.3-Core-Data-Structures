#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class llIterator:

    def __init__(self, head):
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        while self.curr != None:
            item = self.curr.data
            self.curr = self.curr.next
            return item
        raise StopIteration

class DoublyLinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  #Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
    
    def __iter__(self):
        """ Returns the iteator object """
        return llIterator(self.head)

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1) Because it is returning size """
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        
        """Running time: If there was no item in the list before hand, it is O(n) 
        because you are assining variable to head, but n is the length of the list.
        Else, it is O(n) because you have to go through an entire
         linked list to check where the pointer becomes null to add """
        new_node = Node(item)
        if self.head is None:
            self.head  = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""

        """Running time: O(1) if the list was empty beforehand, you are
        assigning the nodes to head and tail variables. O(1) also
        if it is not empty since you are not looping."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.

            Best case running time: O(1) If the item is found on the first loop, 
            if it is the first item on the linked list

            Worst case running time: O(n) If the item is at tail, we have to traverse
            through the whole list to find the data."""
        curr = self.head
        while curr:
            if quality(curr.data) is True:
                return curr.data
            curr = curr.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.

         Best case running time: O(1) If the list is empty or if there is only
              one item in the list
         Worst case running time: O(n) If it is the last item in the list,
             traverse through the whole list."""

        if self.is_empty():    
            raise ValueError('List is empty: {}'.format(item))
           
        curr = self.head
        if self.size == 1 and curr.data == item:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        elif curr.data == item:
            self.head = curr.next
            curr = curr.next
            curr.prev = self.head
            self.size -= 1
            return

        elif self.tail.data == item:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        else:
            while curr.next != None:
                curr = curr.next
                if curr.data == item:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self.size -= 1
                    return

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        """
        Replaces an old item with a new one without creating a new node
        """
        curr = self.head
        while curr:
            if curr.data == old_item:
                curr.data = new_item
                return curr.data
            curr = curr.next

def test_linked_list():
    ll = DoublyLinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    # test_linked_list()
    liya = DoublyLinkedList()
    liya.append('A') 
    # print(liya.items())
    liya.append('B')
    liya.append('C')
    # print(liya.items())
    # liya.append('D')
    # liya.append('E')
    # liya.append('E')
    print(liya.items())
    # print(liya.find(lambda item : item == 'A'))
    print(liya.replace('B', 'D'))
    # print(liya.replace('A', 'D'))
    # print(liya.replace('C', 'D'))
    
    # print(liya.items())
    print(liya.size)
    # print(liya.__iter__())
    # iter(liya)
    # for item in liya:
    #     print(item)
    # liya.delete('A')
    print(liya.size)
    print(liya)
    
