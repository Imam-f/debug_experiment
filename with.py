class marker:
    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, traceback):
        print('exit')

with marker():
    print('hello')

if True:
    print('hello2')
