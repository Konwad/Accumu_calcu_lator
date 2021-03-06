import matplotlib.pyplot as plt


C=[0,0.03125,0.09375,0.125,0.208,0.25,0.375,0.5,0.625,0.75,0.875,1,1.125,1.25,1.375,1.5,1.625,1.75,1.875,2,2.125,2.25,2.375,2.5,2.625,2.75,2.875,3,3.125,3.23]
V=[3.95,3.85,3.8,3.78,3.75,3.74,3.7,3.65,3.62,3.59,3.55,3.51,3.48,3.45,3.41,3.38,3.35,3.31,3.28,3.25,3.22,3.2,3.16,3.14,3.1,3.08,3.04,3,2.9,2.8,]

plt.plot(C,V)
plt.grid(True)
plt.xlabel ('Ah')
plt.ylabel('Volt')
plt.title('Discharge 8.0 A: SamsungINR18650-35E')

plt.show()