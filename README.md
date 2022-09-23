# Variational autoencoder applied to Generative design
> This repo contains my work on variational autoencoders applied to generative design. For a thorough documentation on the mathematical principles of the work, it would be adequate to read : https://arxiv.org/abs/2205.02102

![Design_evol_AdobeExpress](https://user-images.githubusercontent.com/57362874/191919403-a8eb1994-0ee3-49e7-9845-553f9ba82755.gif)



The study case for the application of this technique has been the design extrapolation of 11 NACA Airfoils. This data has been extracted from: http://airfoiltools.com/airfoil/naca4digit. Imported as .txt files in the ***Airfoils*** folder. The same operation was performed by the polars of each of these Airfoils, folder ***Polars***. 

The functioning of this example is as follows: The design of each Airfoil and its lift polar (C_l vs α, being α each Airfoil's angle of attack) is mapped to a 2 Dimensional latent space. We will be able to move through the latent space in real time with two ranges embedded in an HTML file.

For this purpose, 3 Neural networks are constructed in the code. 2 Variational autoencoders (One for the Airfoil designs and another for their polars) and one feed forward neural network that maps the latent spaces between the two. The figure below shows the probabilistic distributions of each Airfoil in the latent space. This 2D space is mapped into the corresponding polar 2D space via the mapper (the distributions of the Airfoil polars will not be located on the same points). 

![Capture](https://user-images.githubusercontent.com/57362874/191486351-6c859f63-e314-4c5d-bb66-4e830c0f8f2c.PNG)

The results obtained after training:

https://user-images.githubusercontent.com/57362874/191912806-e3a2cf30-6684-42a1-bbb0-6aff70338ecf.mp4




Main concepts of VAEs clearly explained: https://www.youtube.com/watch?v=9zKuYvjFFS8&t=604s&ab_channel=ArxivInsights

For information about the VAE implementation: https://keras.io/examples/generative/vae/

For information about Polars, Airfoils and basic aerodynamic concepts: https://en.wikipedia.org/wiki/Drag_curve, http://airfoiltools.com/polar/index
