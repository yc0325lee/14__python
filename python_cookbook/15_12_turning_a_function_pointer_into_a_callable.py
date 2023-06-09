#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ctypes
lib = ctypes.cdll.LoadLibrary(None)
# Get the address of sin() from the C math library
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
addr


# In[ ]:


# Turn the address into a callable function
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
func


# In[ ]:


# Call the resulting function
func(2)
func(0)


# In[ ]:


from llvm.core import Module, Function, Type, Builder
mod = Module.new('example')
f = Function.new(mod,Type.function(Type.double(), \

block = f.append_basic_block('entry')
builder = Builder.new(block)
x2 = builder.fmul(f.args[0],f.args[0])
y2 = builder.fmul(f.args[1],f.args[1])
r = builder.fadd(x2,y2)
builder.ret(r)

from llvm.ee import ExecutionEngine
engine = ExecutionEngine.new(mod)
ptr = engine.get_pointer_to_function(f)
ptr

foo = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(ptr)
# Call the resulting function
foo(2,3)

foo(4,5)

foo(1,2)

