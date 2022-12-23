#include <iostream>
#include <vector>

class Node {
 private:
  int data;
  Node* left;
  Node* right;
  Node* parent;

 public:
  Node(int data, Node* left, Node* right, Node* parent)
      : data{data}, left{left}, right{right}, parent{parent} {}

  Node(int data) : data{data}, left{nullptr}, right{nullptr}, parent{nullptr} {}

  Node() : data{0}, left{nullptr}, right{nullptr}, parent{nullptr} {}

  int getData() { return data; }

  void setData(int newVal) { data = newVal; }

  Node* getLeft() { return left; }
  Node* getRight() { return right; }
  Node* getParent() { return parent; }
  void setLeft(Node* newLeft) { left = newLeft; }
  void setRight(Node* newRight) { right = newRight; }
  void setParent(Node* newParent) { parent = newParent; }
};

class BST {
 private:
  Node* root;
  size_t size;

  Node* getPotentialparent(int val) {
    Node* potentialParent = nullptr;
    Node* tmp = root;

    while (tmp) {
      if (val == tmp->getData()) return tmp;
      potentialParent = tmp;

      if (val > tmp->getData())
        tmp = tmp->getRight();
      else
        tmp = tmp->getLeft();
    }

    return potentialParent;
  }

  void replaceNode(Node* original, Node* replacement) {
    Node* oParent = original->getParent();
    Node* oLeft = original->getLeft();
    Node* oRight = original->getRight();

    if (oParent) {
      if (oParent->getLeft() == original)
        oParent->setLeft(replacement);
      else
        oParent->setRight(replacement);
    } else {
      root = replacement;
    }

    if (replacement) {
      Node* rParent = replacement->getParent();
      Node* rRight = replacement->getRight();

      // getting replacement out of place
      if (/* rRight and  */ rParent != original) {
        if (rRight) rRight->setParent(rParent);

        if (rParent->getLeft() == replacement)
          rParent->setLeft(rRight);
        else
          rParent->setRight(rRight);

        replacement->setRight(oRight);
        if (oRight) oRight->setParent(replacement);
      }

      // assigning left child to replacement
      if (replacement != oLeft) {
        replacement->setLeft(oLeft);
        if (oLeft) oLeft->setParent(replacement);
      }

      // assigning right child to replacement
      // if (rParent != original) {
      //   replacement->setRight(oRight);
      //   if (oRight) oRight->setParent(replacement);
      // }

      // assigning parent to replacement
      replacement->setParent(oParent);
    }
  }

  Node* getSmallestDescendant(Node* curr) {
    if (!curr->getLeft()) return curr;

    return getSmallestDescendant(curr->getLeft());
  }

 public:
  BST(int data) : root{new Node(data)}, size{0} {}
  BST() : root{nullptr}, size{0} {}

  Node* getRoot() { return root; }
  void setRoot(Node* newRoot) { root = newRoot; }
  size_t getSize() { return size; }
  void setSize(int newSize) { size = newSize; }

  Node* find(Node* currNode, int key) {
    if (currNode == nullptr) return nullptr;

    if (currNode->getData() == key) return currNode;

    if (key > currNode->getData()) return find(currNode->getRight(), key);

    return find(currNode->getLeft(), key);
  }

  Node* insert(int val) {
    Node* newNode = new Node(val);
    size++;

    if (root == nullptr) {
      root = newNode;
      return root;
    }

    Node* potentialParent = getPotentialparent(val);

    // do not insert duplicate values
    if (potentialParent->getData() == val) return potentialParent;

    if (val > potentialParent->getData()) {
      potentialParent->setRight(newNode);
    } else {
      potentialParent->setLeft(newNode);
    }

    newNode->setParent(potentialParent);

    return newNode;
  }

  void inorderTraversal(Node* currNode) {
    if (!currNode) {
      std::cout << "\n";
      return;
    }

    inorderTraversal(currNode->getLeft());
    std::cout << currNode->getData() << " ";
    inorderTraversal(currNode->getRight());
  }

  void remove(int val) {
    Node* toDelete = find(root, val);
    size--;

    if (!toDelete) return;

    if (toDelete->getRight())
      replaceNode(toDelete, getSmallestDescendant(toDelete->getRight()));
    else
      replaceNode(toDelete, toDelete->getLeft());

    delete toDelete;
  }
};

int main() {
  BST bst;

  // for (int i = 0; i < 10; i++) {
  //   bst.insert(i);
  // }

  bst.insert(5);
  bst.insert(3);
  bst.insert(1);
  bst.insert(4);
  bst.insert(8);
  bst.insert(7);
  bst.insert(10);

  // bst.remove(5);
  // bst.remove(10);
  // bst.remove(8);
  // bst.remove(3);

  while (bst.getSize()) {
    bst.remove(bst.getRoot()->getData());
  }
  bst.inorderTraversal(bst.getRoot());

  return 0;
}