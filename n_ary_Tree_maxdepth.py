class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(child) for child in root.children)


def main():
    # Creating a sample N-ary tree
    # The tree structure is as follows:
    #       1
    #     / | \
    #    2  3  4
    #   / \
    #  5   6
    # / \
    # 7  8
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    root.children[0].children[0].children = [Node(7), Node(8)]

    # Calculating and printing the maximum depth of the N-ary tree
    print("Maximum depth of the N-ary tree is:", maxDepth(root))

if __name__ == "__main__":
    main()