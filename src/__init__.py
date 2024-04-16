# Python
from .purePython.purePython import fibonacci_pure_python as pure_python

# Compiled python (with and without static typing)
from .compiledPython import compiledPython_wo_staticTyping as compiled_notTyped
from .compiledPython import compiledPython_w_staticTyping as compiled_Typed

# Cython
from .pureCython.pureCython import fibonacci_pure_cython as pure_cython
