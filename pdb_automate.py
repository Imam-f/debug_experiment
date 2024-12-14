i = 21
a = 33

def fun(i):
    a = 10 + i
    c = fun2(a)
    d = 40
    return c+d
def fun2(a):
    xyz ='str'
    return a+10

import pdb
import io
output = io.StringIO()
# this contains the pdb commands we want to execute:
# pdb_script = io.StringIO("list;; n;; p i;; p a;; i = 100;; n;; p a;; pp locals();; c;; q;;")
pdb_script = io.StringIO("list;; s;; s;; s;; list;; p i;; p a;; pp locals();; c;; q;;")
# mypdb = pdb.Pdb(stdin=pdb_script)
mypdb = pdb.Pdb(stdin=pdb_script, stdout=output)
mypdb.set_trace()

fun(i)

print("===============")
print(output.getvalue())
print("===============")
print(fun(1))


mypdb = pdb.Pdb()
mypdb.runcall(fun2, i)