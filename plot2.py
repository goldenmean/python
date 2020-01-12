import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#matplotlib.interactive(True)
""""
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Sine Wave')
plt.grid(True)
#plt.savefig("test.png")
plt.show()
"""

"""
import matplotlib.cm as cm
import matplotlib.colors as colors

fig, ax = plt.subplots()
Ntotal = 1000
N, bins, patches = ax.hist(np.random.rand(Ntotal), 20)
plt.show()

#http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html#scatter-plots
import numpy as np
import matplotlib.pyplot as plt
"""

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())

plt.show()

n = 20
Z = np.ones(n)
Z[-7] *= 6

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.axis('equal')
plt.xticks(())
plt.yticks()

plt.show()

#https://stackoverflow.com/questions/8920436/matplotlib-how-to-start-ticks-leaving-space-from-the-axis-origin

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xticks=['Jan','Feb','Mar','April','May']
x=[1,2,3,4,5]
yticks = ['Windy', 'Sunny', 'Rainy', 'Cloudy', 'Snowy']
y=[2,1,3,5,4]

plt.plot(x,y,'b-', marker = 'o') #.2,.1,.7,.8
plt.subplots_adjust(left =0.2)

plt.xticks(x,xticks)
plt.yticks(y,yticks)
ax.set_ylim(0.5,max(y))
plt.show()