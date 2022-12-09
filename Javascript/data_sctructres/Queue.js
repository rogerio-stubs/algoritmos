class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.size = 0; 
  }  

  queue(data) {
    if(this.head === null) {
      this.head = new Node(data);
    } else{
      let pointer = this.head
      while(pointer.next != null) {
        pointer = pointer.next;
      }
      pointer.next = new Node(data);
    }
    this.size += 1;
  } 
  
  dequeue() {
    this.head = this.head.next;
  }

  sizeQueue() {
    return this.size;
  }

  showQueue() {
    if(this.size === 0) return console.log('EMPTY')
    let pointer = this.head;
    var rep = []
    while(pointer.next) {
      rep.push(pointer.data)  
      pointer = pointer.next
    }
    rep.push(pointer.data)
    console.log(rep)
    }
  }



fila = new Queue()
fila.queue(1)
fila.queue(2)
fila.queue(3)
fila.queue(4)
fila.showQueue()
fila.dequeue()
fila.showQueue() 