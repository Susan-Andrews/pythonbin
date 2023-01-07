
#You can split your code into cells using # %% as in this example. 
# Running code this way, Visual Studio Code opens an Interactive pane that displays the plots inline.
#Basically, install Python Extension Pack, it includes Jupyter extension, put your code in the editor, put #%% at the top of your code,
#  you'll get Run cell clickable, click it, and you'll get result in the other window
# %%
'''
import matplotlib.pylab as plt
import numpy as np 
plt.figure()
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x, y,'g^')     #'ro' to see line as dots ,'r--' to see in dash ,'bs' to see as blue sqrs 

plt.show()
plt.ylabel("some label")
plt.xlabel("some label")

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
x.sort()
plt.plot(x, y,'r--')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

import statistics
import numpy as np
import matplotlib.pyplot as plt
estimates=[1000,1010,1786,2000,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
y=[] # create constant vakue for y axis

estimates.sort()
tv=int(0.1*len(estimates))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(5) # any ct value
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([375],[5],'g^')
plt.show()

'''
