class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_data(self):
        return self.data


class Avl_Tree:
    def insert(self, root, key):

        # S1: normal BST
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # S2: update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # S3: balance
        balance = self.getBalance(root)

        # S4: if unbalanced, try 4 cases, Case 1 - Left Left
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)

        # case 2 - Right Right
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)

        # case 3 - Left Right
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # case 4 - Right Left
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # perform rotation
        y.letf = z
        z.right = T2

        # update height
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return

        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # def avl_tree_update_height(node):
    #    left_height = -1
    #    if node.left is not None:
    #       left_height = node.left.height
    #    right_height = -1
    #    if node.right is not None:
    #       right_height = node.right.height
    #    node.height = max(left_height, right_height) + 1
    #
    #
    # def avl_tree_set_child(parent, which_child, child):
    #    if which_child is not "left" and which_child is not "right":
    #       return False
    #
    #    if which_child == "left":
    #       parent.left = child
    #    else:
    #       parent.right = child
    #    if child is not None:
    #       child.parent = parent
    #
    #    avl_tree_update_height(parent)
    #    return True
    #
    #
    # def avl_tree_replace_child(parent, current_child, new_child):
    #    if parent.left == current_child:
    #       return avl_tree_set_child(parent, "left", new_child)
    #    elif parent.right == current_child:
    #       return avl_tree_set_child(parent, "right", new_child)
    #    return False
    #
    #
    # def avl_tree_get_balance(node):
    #     left_height = -1
    #     if node.left is not None:
    #         left_height = node.left.height
    #     right_height = -1
    #     if node.right is not None:
    #         right_height = node.right.height
    #     return left_height - right_height

    # AVLTreeRotateRight(tree, node) {
    #    leftRightChild = node->left->right
    #    if (node->parent != null)
    #       AVLTreeReplaceChild(node->parent, node, node->left)
    #    else { // node is root
    #       tree->root = node->left
    #       tree->root->parent = null
    #    }
    #    AVLTreeSetChild(node->left, "right", node)
    #    AVLTreeSetChild(node, "left", leftRightChild)

    # AVLTreeRebalance(tree, node) {
    #    AVLTreeUpdateHeight(node)
    #    if (AVLTreeGetBalance(node) == -2) {
    #       if (AVLTreeGetBalance(node->right) == 1) {
    #          // Double rotation case.
    #          AVLTreeRotateRight(tree, node->right)
    #       }
    #       return AVLTreeRotateLeft(tree, node)
    #    }
    #    else if (AVLTreeGetBalance(node) == 2) {
    #       if (AVLTreeGetBalance(node->left) == -1) {
    #          // Double rotation case.
    #          AVLTreeRotateLeft(tree, node->left)
    #       }
    #       return AVLTreeRotateRight(tree, node)
    #    }
    #    return node

    # def avl_tree_insert(tree, node):
    #     if tree.root is None:
    #       tree.root = node
    #       node.parent = None
    #       return
    #
    #     cur = tree.root
    #     while cur is not None:
    #       if node.key < cur.key:
    #          if cur.left is None:
    #             cur.left = node
    #             node.parent = cur
    #             cur = None
    #          else:
    #             cur = cur.left
    #       else:
    #          if cur.right is None:
    #             cur.right = node
    #             node.parent = cur
    #             cur = None
    #          else:
    #             cur = cur.right
    #
    #     node = node.parent
    #     while node is not None:
    #       avl_tree_rebalance(tree, node)
    #       node = node.parent


    # AVLTreeRemoveNode(tree, node)
    # {
    # if (node == null)
    # return false
    #
    # // Parent
    # needed
    # for rebalancing
    #     parent = node->parent
    #
    # // Case
    # 1: Internal
    # node
    # with 2 children
    # if (node->left != null & & node->right != null) {
    # // Find successor
    # succNode = node->right
    # while (succNode->left != null)
    #     succNode = succNode->left
    #
    # // Copy
    # the
    # value
    # from the node
    #
    # node = Copy
    # succNode
    #
    # // Recursively
    # remove
    # successor
    # AVLTreeRemoveNode(tree, succNode)
    #
    # // Nothing
    # left
    # to
    # do
    # since
    # the
    # recursive
    # call
    # will
    # have
    # rebalanced
    # return true
    # }
    #
    # // Case
    # 2: Root
    # node(
    # with 1 or 0 children)
    # else if (node == tree->root) {
    # if (node->left != null)
    #     tree->root = node->left
    # else
    #     tree->root = node->right
    #
    # if (tree->root)
    #     tree->root->parent = null
    #
    # return true
    # }
    #
    # // Case
    # 3: Internal
    # with left child only
    # else if (node->left != null)
    # AVLTreeReplaceChild(parent, node, node->left)
    #
    # // Case 4: Internal
    # with right child only OR leaf
    # else
    # AVLTreeReplaceChild(parent, node, node->right)
    #
    # // node is gone.Anything that was below node that has persisted is already correctly
    # // balanced, but ancestors of node may need rebalancing.
    # node = parent
    # while (node != null) {
    # AVLTreeRebalance(tree, node)
    # node = node->parent
    # }
    # return true
    # }

    # AVLTreeRemoveKey(tree, key) {
    #    node = BSTSearch(tree, key)
    #    return AVLTreeRemoveNode(tree, node)
    # }

# class red_Black_tree:
    # RBTreeSetChild(parent, whichChild, child)
    # {
    # if (whichChild != "left" & & whichChild != "right")
    # return false
    #
    # if (whichChild == "left")
    #     parent->left = child
    # else
    #     parent->right = child
    # if (child != null)
    #     child->parent = parent
    # return true

    # RBTreeReplaceChild(parent, currentChild, newChild)
    # {
    # if (parent->left == currentChild)
    # return RBTreeSetChild(parent, "left", newChild)
    # else if (parent->right == currentChild)
    #     return RBTreeSetChild(parent, "right", newChild)
    # return false

    # RBTreeRotateLeft(tree, node)
    # {
    #     rightLeftChild = node->right->left
    # if (node->parent != null)
    # RBTreeReplaceChild(node->parent, node, node->right)
    # else { // node is root
    # tree->root = node->right
    # tree->root->parent = null
    # }
    # RBTreeSetChild(node->right, "left", node)
    # RBTreeSetChild(node, "right", rightLeftChild)

    # RBTreeRotateRight(tree, node)
    # {
    #     leftRightChild = node->left->right
    # if (node->parent != null)
    # RBTreeReplaceChild(node->parent, node, node->left)
    # else { // node is root
    # tree->root = node->left
    # tree->root->parent = null
    # }
    # RBTreeSetChild(node->left, "right", node)
    # RBTreeSetChild(node, "left", leftRightChild)

    # RBTreeInsert(tree, node)
    # {
    #     BSTInsert(tree, node)
    # node->color = red
    # RBTreeBalance(tree, node)
    # }

    # RBTreeGetGrandparent(node)
    # {
    # if (node->parent == null)
    # return null
    # return node->parent->parent
    # }
    #
    # RBTreeGetUncle(node)
    # {
    # grandparent = null
    # if (node->parent != null)
    #     grandparent = node->parent->parent
    # if (grandparent == null)
    #     return null
    # if (grandparent->left == node->parent)
    #     return grandparent->right
    # else
    #     return grandparent->left

    # RBTreeBalance(tree, node)
    # {
    # if (node->parent == null)
    # {
    #     node->color = black
    # return
    # }
    # if (node->parent->color == black)
    #     return
    # parent = node->parent
    # grandparent = RBTreeGetGrandparent(node)
    # uncle = RBTreeGetUncle(node)
    # if (uncle != null & & uncle->color == red) {
    # parent->color = uncle->color = black
    # grandparent->color = red
    # RBTreeBalance(tree, grandparent)
    # return
    # }
    # if (node == parent->right & &
    #     parent == grandparent->left) {
    # RBTreeRotateLeft(tree, parent)
    # node = parent
    # parent = node->parent
    # }
    # else if (node == parent->left & &
    #     parent == grandparent->right) {
    # RBTreeRotateRight(tree, parent)
    # node = parent
    # parent = node->parent
    # }
    # parent->color = black
    # grandparent->color = red
    # if (node == parent->left)
    # RBTreeRotateRight(tree, grandparent)
    # else
    # RBTreeRotateLeft(tree, grandparent)

    # RBTreeRemove(tree, key)
    # {
    #     node = BSTSearch(tree, key)
    # if (node != null)
    # RBTreeRemoveNode(tree, node)

    # RBTreeRemoveNode(tree, node)
    # {
    # if (node->left != null & & node->right != null)
    # {
    #     predecessorNode = RBTreeGetPredecessor(node)
    # predecessorKey = predecessorNode->key
    # RBTreeRemoveNode(tree, predecessorNode)
    # node->key = predecessorKey
    # return
    # }

    # RBTreeRemoveNode(tree, node)
    # {
    # if (node->left != null & & node->right != null)
    # {
    #     predecessorNode = RBTreeGetPredecessor(node)
    # predecessorKey = predecessorNode->key
    # RBTreeRemoveNode(tree, predecessorNode)
    # node->key = predecessorKey
    # return
    # }
    # if (node->color == black)
    #     RBTreePrepareForRemoval(node)
    #     BSTRemove(tree, node->key)

    # RBTreeGetSibling(node)
    # {
    # if (node->parent != null)
    # {
    # if (node == node->parent->left)
    # return node->parent->right
    # return node->parent->left
    # }
    # return null
    # }

    # RBTreeIsNonNullAndRed(node)
    # {
    # if (node == null)
    # return false
    # return (node->color == red)

    # RBTreeIsNullOrBlack(node)
    # {
    # if (node == null)
    # return true
    # return (node->color == black)

    # RBTreeAreBothChildrenBlack(node)
    # {
    # if (node->left != null & & node->left->color == red)
    # return false
    # if (node->right != null & & node->right->color == red)
    #     return false
    # return true

    # RBTreePrepareForRemoval(tree, node)
    # {
    # if (RBTreeTryCase1(tree, node))
    # return
    #
    # sibling = RBTreeGetSibling(node)
    # if (RBTreeTryCase2(tree, node, sibling))
    #     sibling = RBTreeGetSibling(node)
    # if (RBTreeTryCase3(tree, node, sibling))
    #     return
    # if (RBTreeTryCase4(tree, node, sibling))
    #     return
    # if (RBTreeTryCase5(tree, node, sibling))
    #     sibling = RBTreeGetSibling(node)
    # if (RBTreeTryCase6(tree, node, sibling))
    #     sibling = RBTreeGetSibling(node)
    #
    # sibling->color = node->parent->color
    # node->parent->color = black
    # if (node == node->parent->left) {
    # sibling->right->color = black
    # RBTreeRotateLeft(tree, node->parent)
    # }
    # else {
    # sibling->left->color = black
    # RBTreeRotateRight(tree, node->parent)




def print_anagrams(word, prefix=""):
    if len(word) <= 1:
        st = prefix + word

        if str in engish_words:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur

           # if cur not in before: # Check if permutations of cur have not been generated.
           #     print_anagrams(before + after, prefix + cur)


def main():
    print("Please select an option: ")
    print("1. AVL Tree")
    print("2. Red-Black Tree")

    file = open("words.txt", "r")
    line = file.readline()
    # for single in file:
        # print(single)


main()
