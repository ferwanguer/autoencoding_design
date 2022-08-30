import os
import re

class FoilData:
    """Data extraction class"""

    def __init__(self, folder_path):
        self.path = folder_path
        self.directed_paths = []
        self.names = []
        self.x_coordinates = []
        self.y_coordinates = []
        for name in os.listdir(self.path):
            self.directed_paths.append(os.path.join(self.path, name))
            # print(name)
        for d_name in self.directed_paths:
            # print(d_name)
            with open(d_name) as input_file:
                x_coordinate = []
                y_coordinate = []

                for mu, line in enumerate(input_file):

                    if mu == 0:
                        airfoil_name = line

                    else:

                        coordinate = [item.strip()for item in re.split('   |  | ', line)]
                        while ("" in coordinate):
                            coordinate.remove("")

                        coordinate = list(map(float, coordinate[-2:]))
                        # print(coordinate)
                        x_coordinate.append(coordinate[0])
                        y_coordinate.append(coordinate[1])

            self.names.append(airfoil_name)
            self.x_coordinates.append(x_coordinate)
            self.y_coordinates.append(y_coordinate)


Data = FoilData('Airfoils')

from matplotlib import pyplot as plt

plt.scatter(Data.x_coordinates[0], Data.y_coordinates[0])
plt.show()

