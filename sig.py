import signal
import sys

def signal_handler(signum, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGWINCH, signal_handler)
signal.pause()
