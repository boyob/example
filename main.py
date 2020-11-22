import numpy as np

a = np.array([[0,0,0,0],[0.1,0,0,0]])
if (a[:, :4] > 0).any():
    print('-- Yes')
else:
    print('-- No')