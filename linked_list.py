class Node:
   def __init__(self, data, next):
      self.data = data
      self.next = next
   
   
class Linked_list:
   def __init__(self):
      self.head = None
      
      
   def insert_at_begining(self, data):
      node = Node(data, self.head)
      self.head = node
      
      
   def insert_at_end(self, data):
      if self.head is None:
         self.head = Node(data, None)
         return

      itr = self.head
      while itr.next:
         itr = itr.next     
      itr.next = Node(data, None)
      
      
   def insert_at(self, index, data):
      if index < 0 or index >= self.get_length():
         raise Exception('INVALID INDEX')
         
      if index == 0:
         self.insert_at_begining(data)
         return
         
      count = 0
      itr = self.head
      while itr:
         if count == index - 1:
            node = Node(data, itr.next)
            itr.next = node
            break
            
         itr = itr.next
         count += 1
      
   	
   def insert_values(self, data_list):
      self.head = None
      for data in data_list:
         self.insert_at_end(data)
         
         
   def remove_at(self, index):
      if index < 0 or index >= self.get_length():
         raise Exception('INVALID INDEX')
          
      if index == 0:
         self.head = self.head.next
         return
          
      count = 0
      itr = self.head
      while itr:
         if count == index -1:
            itr.next = itr.next.next
            break
             
         itr = itr.next
         count += 1
          
         
   def get_length(self):
       count = 0
       itr = self.head
       while itr:
          count += 1
          itr = itr.next
       
       return count
    
   	
   def printLL(self):
      if self.head is None:
         print("Linked List is empty ")
         return
       
      itr = self.head
      llstr = ''
      while itr:
         llstr += str(itr.data) + ' --> '
         itr = itr.next
   	
      print(llstr)


if __name__ == "__main__":

   myList = [2*i for i in range(1, 11)]
   ll = Linked_list()
   ll.insert_values(myList)
   ll.printLL()
   print('Length: ',ll.get_length())
   ll.insert_at(0, 100)
   ll.printLL()
   ll.remove_at(0)
   ll.printLL()
   print('Length: ',ll.get_length())
   
   
   
