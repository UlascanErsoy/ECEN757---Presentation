import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    T = np.arange(0, 1000000)
    for c in [10, 100, 1000]:

        rbound = c * ((T / (c+1)) - 1)
        plt.plot(T, rbound, label=f"C={c}")

    plt.legend()
    plt.show()


