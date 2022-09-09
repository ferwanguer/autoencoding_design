import os
import re
from scipy.interpolate import Rbf
import numpy as np
from random import random
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

    def point_uniformation(self, desired_points = 66):
        for i in range(len(self.x_coordinates)):
            while len(self.x_coordinates[i]) > desired_points: #The +1 and -1 is to avoid eliminating the first or the last point (kutta point)
                n = len(self.x_coordinates[i]) - 1
                victim = int(random()*n)+1
                self.x_coordinates[i].pop(victim)
                self.y_coordinates[i].pop(victim)
            while len(self.x_coordinates[i]) < desired_points:
                n = len(self.x_coordinates[i])-1
                new_father = int(random()*n)
                new_x = 0.5*(self.x_coordinates[i][new_father] + self.x_coordinates[i][new_father+1])
                new_y = 0.5 * (self.y_coordinates[i][new_father] + self.y_coordinates[i][new_father+1])
                self.x_coordinates[i].insert(new_father+1, new_x)
                self.y_coordinates[i].insert(new_father + 1, new_y)



Data = FoilData('Airfoils')
Data.point_uniformation()


points =np.random.choice(len(Data.x_coordinates[0])-1,40,replace=False )

x_new =0.5*( np.array(Data.x_coordinates[0])[points] + np.array(Data.x_coordinates[0])[np.array(points)+1])
y_new = 0.5*( np.array(Data.y_coordinates[0])[points] + np.array(Data.y_coordinates[0])[np.array(points)+1])

#
from matplotlib import pyplot as plt
for i in range(8):
    # print(i)
    plt.plot(Data.x_coordinates[i], Data.y_coordinates[i])
    # plt.scatter(x_new,y_new)
plt.show()
#
# #VAMOS A INTENTAR UNA MOVIDA DE INTERPOLACION QUE PUEDE SALIR MAL.
#
# n = 1

# rbf = Rbf(n*np.array(Data.x_coordinates[2]), n*np.array(Data.y_coordinates[2]), epsilon=4)
#
# def interpol(x,y):
#     return (rbf(x)- y)**2
#
# print(np.sqrt(interpol(np.array([1]),np.array([0.2]))))
# print("...")