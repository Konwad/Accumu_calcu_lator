import matplotlib.pyplot as plt


C=[0,0.083,0.125,0.166,0.25,0.375,0.5,0.625,0.75,0.875,1,1.125,1.25,1.375,1.5,1.625,1.75,1.875,2,2.125,2.23]
V=[3.83,3.7,3.67,3.65,3.62,3.58,3.54,3.49,3.45,3.4,3.36,3.33,3.28,3.25,3.22,3.17,3.13,3.06,2.98,2.89,2.8]

plt.plot(C,V)
plt.grid(True)
plt.xlabel ('Ah')
plt.ylabel('Volt')
plt.title('Discharge 22 A: PanasonicUR18650NSX')

plt.show()