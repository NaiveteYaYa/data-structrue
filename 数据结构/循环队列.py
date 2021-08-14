# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 18:50
# @Author  : WuxieYaYa

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.queue = []
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.k:
            return False
        else:
            self.queue.append(value)
            self.count += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        else:
            self.count -= 1
            self.queue.pop(0)
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        else:
            self.count -= 1
            return self.queue.pop(0)

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count == 0:
            return -1
        else:
            self.count -= 1
            return self.queue.pop()

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if self.count == self.k else False


if __name__ == '__main__':
    q = MyCircularQueue(3)
    print(q.enQueue(2))
    q.enQueue(4)
    q.enQueue(5)
    print(q.enQueue(3))
    print(q.Rear())
    print(q.isFull())
