
class Stack: ## Stack Class
  sType = ""
  
  MONO = 111 ## MONO[singular] base type declararion
  RELATIONAL = 113 ## RELATIONAL type declaration
  CONDITIONAL = 133 ## CONDITIONAL type declaration
  
  _listNode = [] ## initial list for the Stack::stack
  
  def new(self):
    self._listNode = []
    
  def add(self, a):
  	 self._listNode.append(a)

  def add(a, b):
    return False

  def remove(self, a):
    self._listNode.remove(a)
    
  def shift(self, a): ## shift index by 'a' <+ve OR -ve>
    indexCarry = [] ## create the carry queue
    indexCarry[0] = a ## create the 
    for i in range(len(self._listNode)):
      if a > 0:
      	carryIndex[i+1] = self.listNode[i] ## shift forward
      elif a < 0:
        	carryIndex[i-1] = self.listNode[i] ## shift back
      
    self._listNode = indexCarry 

  def shift(self, a, b):
    listCarry = []
    for i in range(b): ## add all values from keys<i> into listCarry
      listCarry.append(self._listNode[i]) ## set index i of listCarry to index 

    for j in range(b+1, len(self._listNode)+1):
      indexCarry[j] = self._listNode[j-1] ## set the ceil values of the array

    listCarry[b] = a
    self._listNode = listCarry() ## replace old array with new values


class Queue:
  
  _x = 0
  _y = 0
  _SIZE = [_x, _y] ## queue[STACK] size'
  
  stack = Stack()
  stack.new() ## initalize new stack
  
  def Queue(self, r):
    return {
      'r': { self.stack.sType == Stack.RELATIONAL } ## declare stack type [mono, relational, conditional]
    }.get(r, 0)
      
  def queue(self, a):
    self.stack.add(a)
    
  def getTop(): 
    return self.stack[0] ## return the stack index <0>
  
  def putTop(a): ## work in progress
  	 self.stack.shift(1).add(a, 0)
  	 
  	 
def Main():
  q = Queue()
  q.Queue("r") ## create relational queue

  for i in range(1, 10):
    q.queue(i) ## create queue with values [1, 2, 3, ... , 10]

  print q.stack._listNode
  print len(q.stack._listNode)

  q.stack.shift(13, 3) ## add '13' at position 3 in array

  print q.stack._listNode
  
if __name__ == "__main__":
  Main()
