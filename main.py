import numpy as np 
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

@app.route("/calculate", methods = ['GET', 'POST'])
def calculate():
    
    x = float(request.json['valor'])
    y = float(request.json['valor_2'])
    # print(request.json)

    xx = np.linspace(0,10,150)
    yy = np.sin(xx*x)*(y)
    # print(yy)

    result = {"x_coordinate":list(xx), "y_coordinate": list(yy), "x": x, "y": y}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)