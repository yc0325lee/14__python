#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import types

class Node:
    pass

import types
class NodeVisitor:
    def visit(self, node):
        stack = [ node ]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    
    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
 
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


# In[ ]:


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

# A sample visitor class that evaluates expressions
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)
    
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
 
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)
 
    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)
 
    def visit_Negate(self, node):
        return -self.visit(node.operand)

    
if __name__ == '__main__':
    # 1 + 2*(3-4) / 5
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)
 
    # Evaluate it
    e = Evaluator()
    print(e.visit(t4)) # Outputs 0.6


# In[ ]:


a = Number(0)
for n in range(1, 100000):
    a = Add(a, Number(n))

e = Evaluator()
e.visit(a)


# In[ ]:


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
 
    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)
 
    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)
        
    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)
 
    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)
 
    def visit_Negate(self, node):
        yield -(yield node.operand)


# In[ ]:


a = Number(0)
for n in range(1,100000):
    a = Add(a, Number(n))

e = Evaluator()
e.visit(a)


# In[ ]:


class Evaluator(NodeVisitor):
 
    def visit_Add(self, node):
        print('Add:', node)
        lhs = yield node.left
        print('left=', lhs)
        rhs = yield node.right
        print('right=', rhs)
        yield lhs + rhs


# In[ ]:


e = Evaluator()
e.visit(t4)


# In[ ]:


value = self.visit(node.left)


# In[ ]:


value = yield node.left


# In[ ]:


value = yield node.left


# In[ ]:


try:
    last = stack[-1]
    if isinstance(last, types.GeneratorType):
        stack.append(last.send(last_result))
        last_result = None
    elif isinstance(last, Node):
        stack.append(self._visit(stack.pop()))
    else:
        last_result = stack.pop()

except StopIteration:
    stack.pop()


# In[ ]:


class Visit:
    def __init__(self, node):
        self.node = node


class NodeVisitor:
    def visit(self, node):
        stack = [ Visit(node) ]
        last_result = None
    while stack:
        try:
            last = stack[-1]
            if isinstance(last, types.GeneratorType):
                stack.append(last.send(last_result))
                last_result = None
            elif isinstance(last, Visit):
                stack.append(self._visit(stack.pop().node))
            else:
                last_result = stack.pop()
        except StopIteration:
            stack.pop()
        return last_result
 
    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
 
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


# In[ ]:


class Evaluator(NodeVisitor):
    def visit_Add(self, node):
        yield (yield Visit(node.left)) + (yield Visit(node.right))
    
    def visit_Sub(self, node):
        yield (yield Visit(node.left)) - (yield Visit(node.right))


# In[ ]:




