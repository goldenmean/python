from multiprocessing import Process
from matplotlib.pyplot import plot, show

def plot_graph(*args):
    for data in args:
        plot(data)
    show()

p = Process(target=plot_graph, args=([1, 2, 3],))
p.start()

print 'yay'
print 'computation continues...'
print 'that rocks.'

print 'Now lets wait for the graph be closed to continue...:'
p.join()