import matplotlib.pyplot as plt
#https://matplotlib.org/users/pyplot_tutorial.html


plt.plot([1,2,3,4], [1,4,9,16],'k')
plt.axis([0, 6, 0, 20])
plt.show(block=False) #block=False , returns the control to the next instruction. non-blocking.

print("Hello ")
#But when this is executed as python plot1.py , it displays the plot shows temporarily and window exits, on which, the plot is also closed
plt.show() #This blocks , but when run as python plot1.py, the plot window stays on
print("Matplotlib ")