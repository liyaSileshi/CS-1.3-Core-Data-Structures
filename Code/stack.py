#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        #Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.

        Running time: O(1) – We're inserting at the head, 
        so we're not looping through the entire linked list.
        Just switching were the head points to."""
        #Push given item
        self.list.insert_at_index(0, item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        
        Running time: O(1) – we're simply returning the data at head"""
        #Return top item, if any
        if self.is_empty():
            return None

        return self.list.get_at_index(0) #return the head

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.

        Running time: O(1) – deleting the first item doesn't require
        looping through the entire list. We're just moving the head pointer"""
        #Remove and return top item, if any
        if self.is_empty():
            raise ValueError

        first_item = self.list.get_at_index(0)
        self.list.delete(first_item)
        return first_item

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        #Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        #Count number of items
        return len(self.list) #length of array

    def push(self, item):
        """Insert the given item on the top of this stack.

        Running time: O(1) – Dynamic arrays have extra empty spaces,
        so when we push an item it goes to that space. Instead of making 
        a new array (for most cases) """
        # Insert given item
        self.list.append(item) #inserts item at end

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        
        Running time: O(1) – returning the last item in the array is O(1)"""
        # Return top item, if any
        if self.is_empty():
            return None 
        return self.list[self.length() - 1] #item at last of the array

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.

        Running time: O(1) – Last item, so it doesn't require shifting
        the array left or right, so we don't have to loop."""
        #Remove and return top item, if any
        if self.is_empty():
            raise ValueError

        last_item_index = self.length() - 1
        return self.list.pop(last_item_index)
# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
