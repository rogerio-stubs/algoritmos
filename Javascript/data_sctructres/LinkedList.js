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
    console.log(rep)
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
    console.log(this.size)
  }

  returnHead() {
    console.log(this.head)
  }

  returnTail() {
    console.log(this.tail)
  }

}


const list = new LinkedList()

list.insertToHead(02)
list.insertToHead(12)
list.insertToHead(22)
// list.insertToTail(44)
list.show()
list.linkedSize()
list.returnTail()
