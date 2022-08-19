'''
The outfielder problem

pip install matplotlib
pip install ipykernel
'''
#%%
import matplotlib.pyplot as plt

def ball_trajectory(x):
    location = 10 * x - 5 * (x**2)
    return location

xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]

plt.plot(xs, ys)
plt.title('The outfielder problem')
plt.xlabel('Horizontal position')
plt.ylabel('Vertical position')
plt.axhline(y = 0)
plt.show()
# %%
