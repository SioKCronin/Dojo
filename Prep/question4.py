# Question 4

'''
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents
of the root's left child, then that left child might be the lowest common ancestor.
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.
The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing
the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

with an answer of 3

'''

a1 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
      5,
      1,
      4)

# with an answer of 0

def question4(T, r, n1, n2):
    # Iterate through rows to find where n1 and n2 are created as children
    n1_pos = 0
    n2_pos = 0
    for x in T:
        for i in range(x):
            if x[i] == 1 and i == n1:
                n1_pos = x
            else:
                if x[i] == 1 and i == n2:
                    n2_pos = x
    if n2_pos > n1_pos:
        return n1_pos
    return n2_pos

