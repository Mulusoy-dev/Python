import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("C:/Users/melih/Desktop/sensorler.xlsx")
var_rpm = pd.read_excel("C:/Users/melih/Desktop/encoder111.xlsx")


rpm = var_rpm['rpm']
#print(len(rpm))
#print(var)

time2 = list(var_rpm['time'])

time = list(var['time'])
a= len(time)
#print(time)

vibration = list(var['vibration'])
#print(vibration)

temp1 = list(var['0-3V Temp1'])
#print(temp1)

temp2 = list(var['0-3V Temp2'])
#print(temp2)

temp3 = list(var['0-3V Temp3'])
#print(temp3)

oil_temp = list(var['Oil Temp [C]'])
#print(oil_temp)



#plt.grid()






fig = plt.figure()
ax2 = fig.add_subplot()

# fig,ax2 =plt.subplot()
ax1=ax2.twinx()
plt.xlim(0, a+500)





#plt.plot(time, vibration, 'y', time, temp1,'r', time, temp2, 'r', time, temp3, 'r', time, oil_temp,'r--')
ln22 = ax2.plot(time2, rpm, color='black', label='rpm', linewidth=1)
ln11 = ax1.plot(time, vibration, color='gray', label='vibration', linewidth=0.3)
ln12 = ax1.plot(time, temp1, color='red', label='temp1', linewidth=0.3)
ln13 = ax1.plot(time, temp2, color='green', label='temp2',linewidth=0.3)
ln14 = ax1.plot(time, temp3, color='blue', label='temp3',linewidth=0.3)
ln15 = ax1.plot(time, oil_temp, color='magenta',label='oil temp', linewidth=0.3)


lns = ln22 + ln11 + ln12 + ln13 + ln14 + ln15

labs = [l.get_label() for l in lns]
ax2.legend(lns, labs, loc=0)

# ax1.legend(loc="upper right")
# ax2.legend(loc="best")
plt.show()
plt.close()