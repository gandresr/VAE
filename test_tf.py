import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

fig = plt.figure()

with open('/home/griano/Documents/Github/VAE/dataset/train/0/0.pkl', 'rb') as f:
    data = pickle.load(f)
print(data.shape)
ims = []
for d in data:
    im = plt.imshow(d, cmap='gray', animated=True)
    ims.append([im])

ims = np.array(ims)
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=False,
                                repeat_delay=0)

# ani.save('dynamic_images.mp4')

plt.show()