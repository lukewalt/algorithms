# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree[3, 9, 20, null, null, 15, 7],


def max_depth(head):
    # base 
    if head == None:
        return 0
    # subroutine
    left = max_depth(head.left)
    right = max_depth(head.right)

    # returns max of left and right plus one because each time the function is exectude, its current state is one ahead of next recursive call
    return max(left, right) + 1