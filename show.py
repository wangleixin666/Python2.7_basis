#!/usr/bin/env python    # -*- coding: utf-8 -*

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 30)
y = 0.5*x + 49

plt.plot(y)
plt.xlabel('day')
plt.ylabel('Kg')
plt.ylim(0, 100)
plt.xlim(1, 30)
plt.show()
