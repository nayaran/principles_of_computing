"""
Stack class
"""

class Stack:
    """
    A simple implementation of a LIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def push(self, item):
        """
        Add item to the queue.
        """
        self._items.insert(0, item)

    def pop(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

def test_stack():
    list1 = Stack()

    list1.push(2)
    list1.push(3)
    list1.push(4)
    print list1
    list1.pop()
    print list1
    list1.pop()
    print list1
    list1.push(5)
    print list1

#test_stack()
