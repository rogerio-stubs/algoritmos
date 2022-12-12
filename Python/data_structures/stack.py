import unittest
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next= None

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


    def push(self, elem):
        node = Node(elem)

        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            node = self.top.data
            self.top = self.top.next
            self._size -= 1
            return node
        else:
            raise IndexError('The stack is empty!')

    def peek(self):
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError('The stack is empty!')


class StackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.__len__())
        self.stack.push(2)
        self.assertEqual(2, self.stack.__len__())


    def test_pop(self):
        self.assertRaises(IndexError, self.stack.pop)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.pop())

    def test_peek(self):
        self.assertRaises(IndexError, self.stack.peek)
        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())

if __name__ == '__main__':
    unittest.main()