import numpy as np
import matplotlib.pyplot as plt
X = np.arange(1,21)
Y = np.sin(X)
X = np.random.randn(50)
print(X)
plt.hist(X,50)
plt.show()
#big o complexity notaions graph