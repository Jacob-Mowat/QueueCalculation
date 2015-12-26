
class Stack: ## Stack Class
  sType = ""
  
  MONO = 111 ## MONO[singular] base type declararion
  RELATIONAL = 113 ## RELATIONAL type declaration
  CONDITIONAL = 133 ## CONDITIONAL type declaration
  
  _listNode = [] ## initial list for the Stack::stack
  
  def new():
    self._listNode = []
    
  def add(a, b):
  	 self._listNode.append(a)
    
  def remove(a):
    self._listNode.remove(a)
    
  def shift(a): ## shift index by 'a' <+ve OR -ve>
    indexCarry = [] ## create the carry queue
    indexCarry[0] = a ## create the 
    for i in range(len(self._listNode)):
      if a > 0:
      	carryIndex[i+1] = self.listNode[i] ## shift forward
      else if a < 0:
        	carryIndex[i-1] = self.listNode[i] ## shift back
      
    self._listNode = indexCarry 

class Queue:
  
  _x = 0
  _y = 0
  _SIZE = [self._x, self._y] ## queue[STACK] size'
  
  stack = Stack.new() ## initalize new stack
  
  def Queue(r):
    switch(r):
      case "r":
        self.stack.sType = Stack.RELATIONAL; ## declare stack type [mono, relational, conditional]
      default:
        return False
      
  def queue(a):
    self.stack.add(a)
    
  def getTop(): 
    return self.stack[0] ## return the stack index <0>
  
  def putTop(a, b):
  	 self.stack.shift(1).add(a, 0)
    	
      
  
      
  
      	
       
    