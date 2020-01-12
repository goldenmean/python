#https://docs.python.org/2/glossary.html#term-global-interpreter-lock
#https://pymotw.com/2/multiprocessing/basics.html
#https://docs.python.org/2/library/multiprocessing.html

import multiprocessing
import time
import sys
"""
def daemon():
    p = multiprocessing.current_process()
    print ('Starting:', p.name, p.pid)
    sys.stdout.flush()
    #time.sleep(7)
    print ('Exiting :', p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print ('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print ('Exiting :', p.name, p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
"""

import multiprocessing
import time
import sys

def daemon():
    print ('Starting:', multiprocessing.current_process().name)
    time.sleep(2)
    print ('Exiting :', multiprocessing.current_process().name)

def non_daemon():
    print ('Starting:', multiprocessing.current_process().name)
    print ('Exiting :', multiprocessing.current_process().name)

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    n.start()

    d.join(1)
    print ('d.is_alive()', d.is_alive())
    n.join()    