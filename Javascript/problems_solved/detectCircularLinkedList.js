class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0
  }

  show() {
    if(this.isEmpty()) return console.log('EMPTY')
    let pointer = this.head;
    var rep = []
    while(pointer.next) {
      rep.push(pointer.data)  
      pointer = pointer.next
    }
    rep.push(pointer.data)
    return rep
  }

  insertToTail(data) {
    if (this.head) {
      let pointer = this.head;
      while (pointer.next) {
        pointer = pointer.next;
      }
      pointer.next = new Node(data)
      this.tail = pointer.next.data
    } else {
      this.head = new Node(data)
      this.tail = this.head.data
    }
    this.size++;
  }

  insertToHead(data) {
    if (this.head) {
      const oldHead = this.head;
      this.head = new Node(data)
      this.head.next = oldHead;
      this.tail =  oldHead.next
    } else {
      this.head = new Node(data)
    }
    this.size++;
  }

  isEmpty() {
    if (this.size === 0) return true;
    return false;
  }

  linkedSize() {
    return this.size
  }

  returnHead() {
    return this.head
  }

  returnTail() {
    return this.tail
  }

}

class DetectCircularLinkedList {
  constructor() {
    const linkedList = new LinkedList()
    this.list = linkedList;
  }

  detect() {
    if(this.list.isEmpty() == 0 || this.list.returnTail() === this.list.returnHead()) return true
    return false
  }
}

const list = new DetectCircularLinkedList()
console.log(list.detect())

