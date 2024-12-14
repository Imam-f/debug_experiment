import gdb

executable = './example'

gdb.execute(f"file {executable}")
gdb.execute("break main")
gdb.execute("run")
gdb.execute("break +3")
gdb.execute("c")
gdb.execute("print x")
x = gdb.parse_and_eval("x")
y = gdb.execute("info functions main", to_string=True)
print("VALUE IS ", x)
print("VALUE IS ", y)