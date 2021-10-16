import numpy as np
import matplotlib.pyplot as plt
import random
 
 
ver = [(1,0),
       (np.cos(np.pi*2/5),np.sin(np.pi*2/5)),
       (np.cos(np.pi*4/5),np.sin(np.pi*4/5)),
       ((np.cos(np.pi*6/5),np.sin(np.pi*6/5))),
       (np.cos(np.pi*8/5),np.sin(np.pi*8/5))]
 
p1 = 0
p2 = 1
now1=4
now2=4
colors = ['red', 'blue']
for color in colors:
    for _ in range(100000):
        p3,p4=random.choice(ver)
        while(True):
            if (now1 == p3 and now2==p4):
                p3,p4=random.choice(ver)
            else:
                break
        x_vals.append(p1)
        y_vals.append(p2)
        now1=p3
        now2=p4
        p1=(p1+p3)/2
        p2=(p2+p4)/2
 
        plt.plot(p1,p2,marker = 'o', markersize = 0.03,color = color)
