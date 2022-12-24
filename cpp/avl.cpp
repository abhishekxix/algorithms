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
  int getBalance() { return left->height - right->height; }

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

  Node* insert(int value) {
    Node* newNode = new Node(value);

    if (!root) {
      root = newNode;
      return;
    }

    Node* potentialParent = getPotentialParent(value);

    // do not insert duplicate values
    if (potentialParent->getData() == value) return potentialParent;
  }
};

int main() { return 0; }