import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    x = np.linspace(-5, 5, 200)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.title("waveform")
    plt.savefig("img.png")
