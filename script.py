from ae import VAE
import ae
import numpy as np
from matplotlib import pyplot as plt

real_dim = 100
N = int(real_dim /2)
vae = VAE(real_dim=real_dim)
repetitions = 499
frequency = np.linspace(1, 2, repetitions)[:, None]
amplitude = np.linspace(1, 3, repetitions)[:, None]

x = np.linspace(0,1,N)[None]
x = np.repeat(x,repetitions, axis = 0)
y = amplitude * np.sin(frequency * 2 * np.pi * x)

x_data = np.hstack((x,y))
idx = np.random.choice(x_data.shape[0], repetitions, replace=False)
x_train = x_data[idx[:int(repetitions/2 -1)],:]
x_test = x_data[idx[int(repetitions/2 +1):],:]


vae.train(x_train, N_iterations=20001)
# a = 0.5*np.ones((1,2))
# b = vae.decoder(a)
# _,_,sample = vae.encoder(x_test)
# sample = 0*sample.numpy()
# sample[:,1] = sample[:,1] + np.linspace(-2,2, sample.shape[0])
# testing = vae.decoder(sample)

# plt.figure(1)
# plt.scatter(sample[:,0], sample[:,1])
# plt.show()

# plt.figure(2)
# axis = plt.subplot(1, 1, 1, xlim = [0, 1], ylim=[-3, 3])
# for i in range(100):
#     axis.plot(testing[i, 0:50], testing[i, 50:], label =f'{i}')

# axis.set_title("Reconstruction")
# plt.show()
