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

                        coordinate = [item.strip() for item in re.split('   |  | ', line)]
                        while ("" in coordinate):
                            coordinate.remove("")

                        coordinate = list(map(float, coordinate[-2:]))
                        # print(coordinate)
                        x_coordinate.append(coordinate[0])
                        y_coordinate.append(coordinate[1])

            self.names.append(airfoil_name)
            self.x_coordinates.append(x_coordinate)
            self.y_coordinates.append(y_coordinate)

    def point_uniformation(self, desired_points=66):
        for i in range(len(self.x_coordinates)):

            while len(self.x_coordinates[
                          i]) > desired_points:  # The +1 and -1 is to avoid eliminating the first or the last point (kutta point)
                n = len(self.x_coordinates[i]) - 1
                victim = int(random() * n) + 1
                self.x_coordinates[i].pop(victim)
                self.y_coordinates[i].pop(victim)

            while len(self.x_coordinates[i]) < desired_points:
                n = len(self.x_coordinates[i]) - 1
                new_father = int(random() * n)
                new_x = 0.5 * (self.x_coordinates[i][new_father] + self.x_coordinates[i][new_father + 1])
                new_y = 0.5 * (self.y_coordinates[i][new_father] + self.y_coordinates[i][new_father + 1])
                self.x_coordinates[i].insert(new_father + 1, new_x)
                self.y_coordinates[i].insert(new_father + 1, new_y)

            # if i == 7:
            #     Data.x_coordinates[i][0:33] = Data.x_coordinates[i][32::-1]
            #     Data.y_coordinates[i][0:33] = Data.y_coordinates[i][32::-1]
            # Closing opened loops
            # self.x_coordinates[i][-1] = self.x_coordinates[i][0]
            # self.y_coordinates[i][-1] = self.y_coordinates[i][0]

    def training_data_generation(self):
        arrayed_x = np.array(self.x_coordinates)
        arrayed_y = np.array(self.y_coordinates)

        x_training_set = 10 * arrayed_x #This multiplication is to facilitate training and representation.
        y_training_set = 10 * arrayed_y

        return np.hstack((x_training_set, y_training_set))

if __name__ == "__main__":

    Data = FoilData('Airfoils')
    Data.point_uniformation()
    a = Data.training_data_generation()

#
    from matplotlib import pyplot as plt

# # for i in range(len(Data.x_coordinates)):
#     # print(i)
#     plt.plot(a[4,:], b[4,:])
#     # plt.scatter(x_new,y_new)
#     plt.show()
#     # print(f'{Data.x_coordinates[5]} \n {Data.y_coordinates[5]}')