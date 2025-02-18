class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

      class CircularLinkedList:
         def  __init__(sefl):
            self.head = None

            def insert(self, data):
               new_node = Node(data)
               if not self.head:
                  self.head = new_node
                  self.head.next = self.head
               else:
                  temp = self.head
                  while temp.next != self.head:
                     temp.next = new_node
                     new_node.next = self.head
                     
               def display(self):
                  if not self.head:
                     return
                  temp = self.head
                  while True:
                     print(temp.data, end="->")
                     temp = temp.next
                     if temp == self.head:
                        break
                     print("Back to Head)")

         #Example Usage
      ll = CircularLinkedList()
      ll.insert(10)
      ll.insert(20)
      ll.insert(30)
      ll.display()
         