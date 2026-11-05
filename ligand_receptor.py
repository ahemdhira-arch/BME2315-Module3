
import numpy as np
import matplotlib.pyplot as plt

def Fact(GLP1, sema):
    return (GLP1/0.17 + sema/0.38) / (1 + GLP1/0.17 + sema/0.38)

sema = np.logspace(-2, 2, 500)

fasting = Fact(0.015, sema)
fed = Fact(0.040, sema)

plt.figure()
plt.semilogx(sema, fasting, label="Fasting GLP1")
plt.semilogx(sema, fed, label="Fed GLP1")

plt.xlabel("Semaglutide concentration (nM)")
plt.ylabel("Fraction active (Fact)")
plt.title("GLP1R Activation")
plt.ylim(0, 1)
plt.legend()
plt.show()
