// package com.ccodes.structures;

class Item {
  public int data;
  public Item below;

  public Item(int _data) {
    data = _data;
    below = null;
  }
}

public class Stack {
  Item head;
  int size;

  public Stack() {
    head = null;
    size = 0;
  }

  public void add(int data) {
    Item added_item = new Item(data);
    added_item.below = head;
    head = added_item;
    size += 1;
  }

  public int peek() throws Exception {
    if (empty()) {
      throw new Exception("Stack is empty");
    }
    return head.data;
  }

  public int pop() throws Exception {
    int data = head.data;
    head = head.below;
    size -= 1;
    return data;
  }

  public boolean empty() {
    return (head == null);
  }

  public int size() {
    return size;
  }

  public static void main(String[] args) {
    System.out.println("Testing the Stack");
    Stack s = new Stack();
    int n = 1000000;
    for (int i=0; i<n; i++) {
      s.add(i);
    }
    System.out.println("Stack size after adding " + n + " items: " + s.size());
    try {
      for (int i=0; i<n; i++) {
        int data = s.pop();
        // System.out.println("Stack pop(): " + data);
      }
    } catch (Exception e)
    {

    }
    System.out.println("Stack size: " + s.size());
    System.out.println("Stack size after removing " + n + " items: " + s.size());
  }
}
