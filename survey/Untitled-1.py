"""
Project 4: Circular Double-Ended Queue
CSE 331 SS24
David Rackerby
solution.py
"""

from typing import TypeVar, List, Optional

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: Optional[List[T]] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            # front will get set to 0 by front_enqueue if the initial data is empty
            data = ['Start']
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    # ============ Modify Functions Below ============#

    def __len__(self) -> int:
        """
        Return int representing length of the circular deque
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Return True if empty, False otherwise
        """
        return self.size == 0

    def front_element(self) -> Optional[T]:
        """
        Return the first element if it exists, otherwise None
        """
        if self.is_empty():
          return None
        else:
          return self.queue[self.front]

    def back_element(self) -> Optional[T]:
        """
        Returns the last element if it exists, otherwise None
        """
        if  self.is_empty():
          return None
        else:
          return self. queue[(self.front + self.size - 1) % self.capacity]

    def grow(self) -> None:
        """
        Doubles the capacity of deque and compies the values over from the current list
        """
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.queue = new_queue
        self.capacity = new_capacity
        self.front = 0
        self.back = self.size - 1

    def shrink(self) -> None:
        """
        Halves the capacity of the deque and copies over the contents of the old list
        """
        new_capacity = self.capacity // 2
        if new_capacity >= 4:
            new_queue = [None] * new_capacity
            for i in range(self.size):
                new_queue[i] = self.queue[(self.front + i) % self.capacity]
            self.queue = new_queue
            self.capacity = new_capacity
            self.front = 0
            self.back = self.size - 1

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Add a value to either the front or back of the circular deque
        :param value: value to add into the circular deque
        :paran front: which end of the deque to add the value
        """

        if front:
            if self.front is None:
                self.front = 0
                self.back = 0
            else:
                self.front = (self.front - 1) % self.capacity
            self.queue[self.front] = value

        else: 
            if self.back is None:
                self.back = 0
                self.front = 0
            else:
                self.back = (self.back + 1) % self.capacity
            self.queue[self.back] = value 

        self.size += 1

        if self.size == self.capacity:
            self.grow()

    def dequeue(self, front: bool = True) -> Optional[T]:
        """
        Remove an item from either the front or back of the circular deque
        :param front: remove the front or back item from the dequeue 
        """

        if self.is_empty():
            return None

        if front:
            value = self.queue[self.front]
            if self.size ==1:
                self.front = None
                self.back = None
            else:
                self.front = (self.front + 1) % self.capacity
        else:
            value = self.queue[self.back]
            if self.size ==1:
                self.front = None
                self.back = None
            else:
                self.back = (self.back - 1) % self.capacity

        self.size -= 1

        if self.size > 0 and self.size <= self.capacity // 4:
            self.shrink()

        return value


def maximize_profits(profits: List[int], k: int) -> int:
    """
    Takes in a pay period, a work interval and returns the max profit that can be made within the pay period
    :param profits: A list of profits representing the amount of money made for a given day
    :param k: A work interval. You must work at least once every k days.
    """
    b = 0  
    j = 1 
    n = len(profits)
    circular_deque = CircularDeque() 
    circular_deque.enqueue(profits[0], front=False)
    current_profit = profits[0]
    max_profit = profits[0]

    for i in range(1, n):
        profit = profits[i]
        if profit > 0 or i == n - 1:
            current_profit = max_profit + profit
            max_profit = current_profit
            circular_deque.enqueue(current_profit, front=False)
            j = 1
        elif j % k == 0:  
            past = circular_deque.back_element()
            current_profit = max_profit + profit
            if current_profit >= past:
                max_profit = current_profit
                circular_deque.enqueue(current_profit, front=False)
                j = 1
            elif current_profit < past:
                max_profit = past
                circular_deque.enqueue(current_profit, front=False)
                j = b + 1
                b = 0
        elif j % k != 0:
            past = circular_deque.back_element()
            current_profit = max_profit + profit
            if past > current_profit:
                b += 1
                if profits[0] != past:
                    current_profit = past
                    circular_deque.enqueue(current_profit, front=False)
                    j += 1
                else:
                    circular_deque.enqueue(current_profit, front=False)
                    j += 1
            elif past < current_profit:
                circular_deque.enqueue(current_profit, front=False)
                j += 1
    return circular_deque.back_element()
 




