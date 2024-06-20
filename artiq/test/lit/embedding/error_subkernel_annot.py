# RUN: %python -m artiq.compiler.testbench.embedding +diag %s 2>%t
# RUN: OutputCheck %s --file-to-check=%t

from artiq.language.core import *
from artiq.language.types import *

# CHECK-L: ${LINE:+2}: error: type annotation for argument 'x', '1', is not an ARTIQ type
@subkernel(destination=1)
def foo(x: 1) -> TNone:
    pass

@kernel
def entrypoint():
    # CHECK-L: ${LINE:+1}: note: in subkernel call here
    foo()
