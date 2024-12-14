import prettyprinter as pp
import traceback

listitems = [i for i in range(10)]
def foo():
    x = 10
    x = x + 2
    print(x)
    print(listitems[x])


try:
    foo()
except Exception as e:
    print(e)
    print(e.__traceback__)
    pp.pprint(e.__traceback__.tb_frame.f_locals)
    pp.pprint(e.__traceback__.tb_frame.f_globals)

def bar():
    try:
        foo()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        pp.pprint(traceback.extract_tb(e.__traceback__))
        for i in traceback.extract_tb(e.__traceback__):
            pp.pprint(i)
            pp.pprint(i.lineno)
            pp.pprint(i.locals)

        print("=======================")
        
        pp.pprint(e.__traceback__.tb_frame.f_locals)
        pp.pprint(e.__traceback__.tb_frame.f_globals)
        print(e.__traceback__.tb_next.tb_frame.f_back.f_locals)
        pp.pprint(e.__traceback__.tb_next.tb_frame.f_locals)

        print("=======================")
        tb = e.__traceback__
        while tb:
            frame = tb.tb_frame
            lineno = tb.tb_lineno
            co = frame.f_code
            filename = co.co_filename
            func_name = co.co_name
            print(f"  File \"{filename}\", line {lineno}, in {func_name}")
            print("    Locals:")
            for var_name, var_value in frame.f_locals.items():
                print(f"      {var_name} = {var_value}")
            tb = tb.tb_next

bar()