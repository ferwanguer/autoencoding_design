# Variational autoencoder applied to Generative design
> This repo contains my work on variational autoencoders applied to generative design. For a thorough documentation on the mathematical principles of the work, it would be adequate to read : https://arxiv.org/abs/2205.02102

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/57362874/191920898-3d46f06b-efa5-417c-a067-95afac28df97.gif)



The objective of this project has been to live-compute some measure of an Airfoil's performance with respecto to it's design. In this case, the perfomance indicator selected was the lift polar. 

 
The study case for the application of this technique has been the design extrapolation of 11 NACA Airfoils. This data has been extracted from: http://airfoiltools.com/airfoil/naca4digit. Imported as .txt files in the ***Airfoils*** folder. The same operation was performed by the polars of each of these Airfoils, folder ***Polars***. 

The functioning of this example is as follows: The design of each Airfoil and its lift polar (C_l vs α, being α each Airfoil's angle of attack) are mapped to two 2-Dimensional latent spaces (One for the Airfoil and one for it's polar function). We will be able to move through the latent space in real time with two ranges embedded in an HTML file.

For this purpose, 3 Neural networks are constructed in the code. Two Variational autoencoders (One for the Airfoil designs and another for their polars) and one feed forward neural network that maps the latent spaces between the two. The figure below shows the probabilistic distributions of each Airfoil in the latent space. This is, each of the 11 normal distributions below corresponds to one of the Airfoils the networks were trained with. This 2D space is mapped into the corresponding polar 2D space via the mapper (the distributions of the Airfoil polars will not be located on the same points).


![Capture](https://user-images.githubusercontent.com/57362874/191486351-6c859f63-e314-4c5d-bb66-4e830c0f8f2c.PNG)

Essentially, the VAEs allow us to simplify a 2n dimensional space (Being n the number of points of each airfoil in 2D space) into a 2D space, being the design optimization much more manageable. VAEs are able to ``generate" the corresponding design from a point in the latent space, hence the name ***Generative Design***.
The results obtained after training are shown below:

![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/57362874/191941005-4bbfee82-825f-4c60-a13a-2167663e570b.gif)





Main concepts of VAEs clearly explained: https://www.youtube.com/watch?v=9zKuYvjFFS8&t=604s&ab_channel=ArxivInsights

For information about the VAE implementation: https://keras.io/examples/generative/vae/

For information about Polars, Airfoils and basic aerodynamic concepts: https://en.wikipedia.org/wiki/Drag_curve, http://airfoiltools.com/polar/index

Contact information: f.wguerra@outlook.com
