import traceback
import pdb

listitems = [i for i in range(10)]
def foo():
    x = 10
    x = x + 2
    print(x)
    print(listitems[x])


try:
    foo()
except Exception as e:
    pdb.post_mortem()
    