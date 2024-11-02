from my_stack import Stack

original = Stack()
reverse = Stack()
original.push('apple')
original.push('pear')
original.push('grape')
original.push('orange')

print(original)

reverse.push(original.pop())
reverse.push(original.pop())
reverse.push(original.pop())
reverse.push(original.pop())

print(reverse)
