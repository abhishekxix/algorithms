#include <iostream>
#include <stack>

class Node {
 private:
  int data;
  int height;
  Node* left;
  Node* right;
  Node* parent;

 public:
  Node(int data)
      : data{data}, height{0}, left{nullptr}, right{nullptr}, parent{nullptr} {}
  Node(int data, int height, Node* left, Node* right, Node* parent)
      : data{data}, height{height}, left{left}, right{right}, parent{parent} {}
  Node(int data, Node* left, Node* right, Node* parent)
      : data{data}, height{height}, left{left}, right{right}, parent{parent} {}
  Node() : data{0}, height{0}, left{nullptr}, right{nullptr}, parent{nullptr} {}

  int getData() { return data; }
  int getHeight() { return height; }
  Node* getLeft() { return left; }
  Node* getRight() { return right; }
  Node* getParent() { return parent; }

  void setData(int newData) { data = newData; }
  void setHeight(int newHeight) { height = newHeight; }
  void setLeft(Node* leftNode) { left = leftNode; }
  void setRight(Node* rightNode) { right = rightNode; }
  void setParent(Node* parentNode) { parent = parentNode; }
};

class AVL {
 private:
  Node* root;
  size_t size;

  Node* getPotentialParent(int value) {
    Node* curr = root;
    Node* potentialParent = nullptr;

    while (curr) {
      if (value == curr->getData()) return curr;

      potentialParent = curr;

      if (value > curr->getData())
        curr = curr->getRight();
      else
        curr = curr->getLeft();
    }

    return potentialParent;
  }

  int getNodeHeight(Node* target) { return target ? target->getHeight() : -1; }

  int calculateHeight(Node* target) {
    return std::max(
               getNodeHeight(target->getLeft()),
               getNodeHeight(target->getRight())
           ) +
           1;
  }

  int getBalance(Node* target) {
    return getNodeHeight(target->getLeft()) - getNodeHeight(target->getRight());
  }
  void rotateLeft(Node* pivot) {
    Node* pParent = pivot->getParent();    //! can be null
    Node* pRight = pivot->getRight();      //  can't be null
    Node* pRightLeft = pRight->getLeft();  //! can be null

    pRight->setParent(pParent);
    if (pParent) {
      if (pParent->getLeft() == pivot)
        pParent->setLeft(pRight);
      else
        pParent->setRight(pRight);
    }

    pRight->setLeft(pivot);
    pivot->setParent(pRight);

    pivot->setRight(pRightLeft);
    if (pRightLeft) pRightLeft->setParent(pivot);

    pivot->setHeight(calculateHeight(pivot));
    pRight->setHeight(calculateHeight(pRight));
  }

  void rotateRight(Node* pivot) {
    Node* pParent = pivot->getParent();    //! can be null
    Node* pLeft = pivot->getLeft();        //  can't be null
    Node* pLeftRight = pLeft->getRight();  //! can be null

    pLeft->setParent(pParent);
    if (pParent) {
      if (pParent->getLeft() == pivot)
        pParent->setLeft(pLeft);
      else
        pParent->setRight(pLeft);
    }

    pLeft->setRight(pivot);
    pivot->setParent(pLeft);

    pivot->setLeft(pLeftRight);
    if (pLeftRight) pLeftRight->setParent(pivot);

    pivot->setHeight(calculateHeight(pivot));
    pLeft->setHeight(calculateHeight(pLeft));
  }

  void fixBalance(Node* target) {
    Node* curr = target;

    while (curr) {
      Node* parent = curr->getParent();
      if (getBalance(curr) > 1) {  // left heavy
        Node* left = curr->getLeft();

        if (getBalance(left) < 0) {
          // lr imbalance
          rotateLeft(left);
        }
        rotateRight(curr);
      } else if (getBalance(curr) < -1) {  // right heavy
        Node* right = curr->getRight();

        if (getBalance(right) > 0) {
          // rl imbalance
          rotateRight(right);
        }
        rotateLeft(curr);
      }
      curr = parent;
    }
  }

 public:
  AVL(int data) : root{new Node(data)} {}
  AVL() : root{nullptr} {}
  ~AVL() {
    Node* curr = root;
    std::stack<Node*> toDelete;

    while (true) {
      while (curr) {
        toDelete.push(curr);
        curr = curr->getLeft();
      }

      if (toDelete.empty()) break;

      Node* tmp = toDelete.top();
      toDelete.pop();
      curr = tmp->getRight();
      delete tmp;
      size--;
    }
  }

  Node* getRoot() { return root; }
  size_t getSize() { return size; }
  Node* insert(int value) {
    Node* newNode = new Node(value);
    size++;

    if (!root) {
      root = newNode;
      return root;
    }

    Node* potentialParent = getPotentialParent(value);

    // do not insert duplicate values
    if (potentialParent->getData() == value) return potentialParent;

    if (value > potentialParent->getData())
      potentialParent->setRight(newNode);
    else
      potentialParent->setLeft(newNode);

    newNode->setParent(potentialParent);

    fixBalance(newNode);

    return newNode;
  }

  void inOrderTraversal(Node* curr) {
    if (!curr) return;

    inOrderTraversal(curr->getLeft());
    std::cout << curr->getData() << " ";
    inOrderTraversal(curr->getRight());
  }
};

int main() {
  AVL avl;

  for (int i = -3; i < 3; i++) {
    avl.insert(i);
  }

  avl.inOrderTraversal(avl.getRoot());
  return 0;
}