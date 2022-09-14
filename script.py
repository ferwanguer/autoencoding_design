from ae import VAE, ForwardMapper
import ae
import numpy as np
from matplotlib import pyplot as plt
from Data_preprocess import FoilData
from Polar_preprocess import PolarData
from flask import Flask, render_template, url_for, request, jsonify
import tensorflow as tf


Data = FoilData('Airfoils')

Data.point_uniformation()
x_train = Data.training_data_generation()
real_dim = x_train.shape[-1]
N = int(real_dim /2)
vae = VAE(real_dim=real_dim)

Polar_Data = PolarData('Polars')
Polar_Data.point_uniformation()
x_train_polar = Polar_Data.training_data_generation()
vae_polar = VAE(real_dim = real_dim)

# repetitions = 499
# frequency = np.linspace(1, 2, repetitions)[:, None]
# amplitude = np.linspace(1, 3, repetitions)[:, None]
#
# x = np.linspace(0,1,N)[None]
# x = np.repeat(x,repetitions, axis = 0)
# y = amplitude * np.sin(frequency * 2 * np.pi * x)
#
# x_data = np.hstack((x,y))
# idx = np.random.choice(x_data.shape[0], repetitions, replace=False)
# x_train = x_data[idx[:int(repetitions/2 -1)],:]
# x_test = x_data[idx[int(repetitions/2 +1):],:]


vae.train(x_train, N_iterations=51)
vae_polar.train(x_train_polar, N_iterations=51)
n_samples = 50
for i in range(n_samples):
    _,_,z = vae.encoder(x_train)
    _,_,z_polar = vae_polar.encoder(x_train_polar)

    if i == 0:
        Z = z
        Z_polar = z_polar
    else:
        Z = tf.concat([Z, z], axis = 0)
        Z_polar = tf.concat([Z_polar, z_polar], axis=0)


mapper = ForwardMapper()
mapper.train(training_data=Z.numpy(), labels=Z_polar.numpy())

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

@app.route("/calculate", methods = ['GET', 'POST'])
def calculate():
    
    x = float(request.json['valor'])
    y = float(request.json['valor_2'])
    # print(request.json)
    inputs = np.array([x,y])[None]

    prediction = vae.decoder(inputs)
    xx = prediction[0,0:N].numpy()
    xxx = xx.astype(float)
    xxx = np.append(xxx,np.array([-1,13]))
    # print(xxx[-1])
    yy = prediction[0,N:].numpy()

    yyy = yy.astype(float)
    yyy = np.append(yyy,np.array([0,0]))

    #Polar part:
    mapped_inputs = mapper.model(inputs)
    polar_prediction = vae_polar.decoder(mapped_inputs)

    xx_polar = polar_prediction[0,0:N].numpy()
    xxx_polar = xx_polar.astype(float)
    # xxx_polar = np.append(xxx,np.array([-1,13]))
    # print(xxx[-1])
    yy_polar = polar_prediction[0,N:].numpy()

    yyy_polar = yy_polar.astype(float)
    # yyy_polar = np.append(yyy_polar,np.array([0,0]))




    result = {"x_coordinate":list(xxx), "y_coordinate": list(yyy), "x": x, "y": y, "x_polar": list(xxx_polar), "y_polar": list(yyy_polar)}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False)
