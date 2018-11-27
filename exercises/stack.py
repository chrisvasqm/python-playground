# Design a class that represents a stack.
# It hould provide the following methods:
# push, pop and clear.
#
# Push should add a new item to the stack.
# Pop should remove the last element and return it.
# Clear should remove all items from the stack.


def main():
    stack = Stack()

    # Add a few items
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Display all items
    print(stack.items)

    # Remove last item
    print(stack.pop())

    # Display remaining items
    print(stack.items)

    # Clear all items
    stack.clear()

    # Display empty stack
    print(stack.items)


class Stack(object):

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        lastIndex = len(self._items) - 1
        removed = self._items[lastIndex]
        self._items.pop()
        return removed

    def clear(self):
        self._items.clear()


if __name__ == "__main__":
    main()
