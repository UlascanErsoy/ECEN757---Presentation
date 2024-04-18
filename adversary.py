import matplotlib
font = {'size'   : 22}

matplotlib.rc('font', **font)
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 

def skew_norm_pdf(x,e=0,w=1,a=0):
    # adapated from:
    # http://stackoverflow.com/questions/5884768/skew-normal-distribution-in-scipy
    t = (x-e) / w
    return 2.0 * w * stats.norm.pdf(t) * stats.norm.cdf(a*t)

if __name__ == "__main__":

    w = np.array([0.2,0.5,1.2,1.1,0.8,0.4,0.3,0.1])
    x = np.arange(100)
    w = skew_norm_pdf(x, 20, 20) / 35 
    w = w[20:70]
    x = x[20:70]
    
    prob = (1 / w) / (1 / w).sum()

    plt.figure(figsize=(8,4.5))
    ax = plt.subplot()
    plt.bar(x,w, color='grey', label="Utility Coeff. ($w^n$)")
    plt.plot(x,prob, label="$x_t$ PMF")
    ax.fill_between(x, prob, color="b", alpha=0.2) 
    plt.yticks([],[])
    plt.xticks(np.arange(0,50,10) + 20, np.arange(0,50,10))
    plt.xlabel("Files")
    plt.legend()
    plt.tight_layout()
    ax.set_xlim([19.5,69.5])
    plt.show()

