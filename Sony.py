import matplotlib.pyplot as plt


C=[0,0.03125,0.0625,0.125,0.25,0.375,0.458,0.5,0.625,0.75,0.875,1,1.125,1.25,1.375,1.5,1.625,1.75,1.875]
V=[3.58,3.5,3.47,3.44,3.4,3.37,3.34,3.33,3.3,3.28,3.25,3.22,3.2,3.185,3.17,3.15,3.13,3.1,3.08]

plt.plot(C,V)
plt.grid(True)
plt.xlabel ('Ah')
plt.ylabel('Volt')
plt.title('Discharge 30.0 A: SonyUS18650_VTC6')

plt.show()

