import random
import math

class Node:
    def __init__(self, value):
        self.value = value  # Operator or operand
        self.left = None    # Left child
        self.right = None   # Right child

def construct_expression_tree(value, operators, max_depth, current_depth=0):
    """
    Construct a random expression tree for a given total.
    :param value: The target value for this subtree.
    :param operators: Allowed operators (e.g., ['+', '-', '*', '/']).
    :param max_depth: Maximum depth of the tree.
    :param current_depth: Current depth of the tree.
    :return: Root of the expression tree.
    """
    if current_depth == max_depth or value <= 1:
        # Base case: leaf node with the current value
        return Node(value)

    # Randomly choose an operator
    operator = random.choice(operators)
    root = Node(operator)

    if operator == '+':
        # Split value into two random positive integers
        left_value = random.randint(1, value - 1)
        right_value = value - left_value
    elif operator == '-':
        # Ensure result is positive
        right_value = random.randint(1, value - 1)
        left_value = value + right_value
        # left_value = random.randint(value, 9) if value != 9 else 9
        # right_value = left_value - value
    elif operator == '*':
        # Find divisors of the value and pick one
        divisors = [i for i in range(1, int(math.sqrt(value)) + 1) if value % i == 0]
        if not divisors:
            return construct_expression_tree(value, operators, max_depth, current_depth)
        right_value = random.choice(divisors)
        left_value = value // right_value
    elif operator == '/':
        # Choose a random divisor as the denominator
        right_value = random.randint(1, 10)  # Keep denominators small for simplicity
        left_value = value * right_value
    else:
        raise ValueError("Unsupported operator!")

    # Recursively build left and right subtrees
    root.left = construct_expression_tree(left_value, operators, max_depth, current_depth + 1)
    root.right = construct_expression_tree(right_value, operators, max_depth, current_depth + 1)

    return root

def tree_to_expression(root):
    """
    Convert a binary expression tree to an infix expression string.
    :param root: Root node of the tree.
    :return: Infix expression string.
    """
    if not root.left and not root.right:
        return str(root.value)

    left_expr = tree_to_expression(root.left)
    right_expr = tree_to_expression(root.right)
    
    return f"({left_expr} {root.value} {right_expr})"

# Example configuration
operators = ['+', '-', '*', '/']
max_depth = 3

for i in range(0,10):
    total = random.randint(2, 9)

    # Generate tree
    expression_tree = construct_expression_tree(total, operators, max_depth)

    # Convert to expression string
    expression = tree_to_expression(expression_tree)
    print(f"Expr {i}: {expression} = {total}")