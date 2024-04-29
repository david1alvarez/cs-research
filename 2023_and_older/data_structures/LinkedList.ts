class ListNode {
    constructor(data: any) {
        this.data = data;
    }
    data: any;
    next: ListNode;
}

export class LinkedList {
    head: ListNode;
    constructor(data: any) {
        // initialize a head element
        this.head.data = data;
    }

    append(data): void {
        // start at the beginning
        let element = this.head;
        // iterate to the last element of the list
        while(element.next) {
            // move to the next element in the list
            element = element.next
        }
        // create a new last element
        element.next = new ListNode(data)
    }

    prepend(data): void {
        // create the new element
        let element = new ListNode(data);
        // point the new element to the head element of the list
        element.next = this.head;
        // redefine the head element to be the new element
        this.head = element;
    }

    delete(data): void {
        // start at the beginning
        let element = this.head;
        // iterate through until the next element is the one you want to delete
        while(element.next.data != data) {
            // error prevention
            if(!element.next) return;
            // move to the next element
            element = element.next;
        }
        // connect your current element to the element after the one you want to delete
        // removing any reference to the deleted element, which will be garbage collected
        element.next = element.next.next;
    }
}
