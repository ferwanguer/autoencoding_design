# Variational autoencoder applied to Generative design
> This repo contains my work on variational autoencoders applied to generative design. For a thorough documentation on the mathematical principles of the work, it would be adequate to read : https://arxiv.org/abs/2205.02102

The study case for the application of this technique has been the design extrapolation of 11 NACA Airfoils. This data has been extracted from: http://airfoiltools.com/airfoil/naca4digit . Imported as .txt files in the ***Airfoils*** folder. The same operation was performed by the polars of each of these Airfoils, folder ***Polars***. 

The functioning of this example is as follows: The design of each Airfoil and its lift polar ($$C_l$$ vs α) being α each Airfoil's angle of attack.  
With this data, 3 Neural networks are constructed in the code. 2 Variational autoencoders (One for the Airfoil designs and another for their polars) and one feed forward neural network that maps the latent spaces between the two. In the example that is represented, 

![Capture](https://user-images.githubusercontent.com/57362874/191486351-6c859f63-e314-4c5d-bb66-4e830c0f8f2c.PNG)






For information about the VAE implementation: https://keras.io/examples/generative/vae/

For information about Polars, Airfoils and basic aerodynamic concepts: https://en.wikipedia.org/wiki/Drag_curve, http://airfoiltools.com/polar/index
