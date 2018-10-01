#include <iostream>

class Item {
  public:
    Item() {
      this->data = 0;
    }
    Item(int _data) {
      this->data = _data;
    }

  private:
    int data;
    // Item below;
};

class Stack {
  public:
    Stack() {
      this->head = Item(0);
    }
  private:
    Item head;

};

int main() {
  printf("Hello World!\n");
  // printf("%s\n", );
}
