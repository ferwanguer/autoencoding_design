import os
import re
from random import random
import numpy as np


class PolarData:
    """Data extraction class"""

    def __init__(self, folder_path):
        self.path = folder_path
        self.directed_paths = []
        self.names = []
        self.alphas = []
        self.c_ls = []
        for name in os.listdir(self.path):
            self.directed_paths.append(os.path.join(self.path, name))

        for d_name in self.directed_paths:
            # print(d_name)
            with open(d_name) as input_file:
                alpha = []
                c_l = []

                for mu, line in enumerate(input_file):

                    if mu == 0:
                        airfoil_name = line

                    else:

                        coordinate = [item.strip() for item in re.split('   |  | ', line)]
                        # print(coordinate)
                        while ("" in coordinate):
                            coordinate.remove("")

                        coordinate = list(map(float, coordinate[0:2]))
                        # print(coordinate)
                        alpha.append(coordinate[0])
                        c_l.append(coordinate[1])

            self.names.append(airfoil_name)
            self.alphas.append(alpha)
            self.c_ls.append(c_l)

    def point_uniformation(self, desired_points=66):
        for i in range(len(self.alphas)):

            while len(self.alphas[
                          i]) > desired_points:  # The +1 and -1 is to avoid eliminating the first or the last point (kutta point)
                n = len(self.alphas[i]) - 1
                victim = int(random() * n) + 1
                self.alphas[i].pop(victim)
                self.c_ls[i].pop(victim)

            while len(self.alphas[i]) < desired_points:
                n = len(self.alphas[i]) - 1
                new_father = int(random() * n)
                new_x = 0.5 * (self.alphas[i][new_father] + self.alphas[i][new_father + 1])
                new_y = 0.5 * (self.c_ls[i][new_father] + self.c_ls[i][new_father + 1])
                self.alphas[i].insert(new_father + 1, new_x)
                self.c_ls[i].insert(new_father + 1, new_y)

            # if i == 7:
            #     Data.alphas[i][0:33] = Data.alphas[i][32::-1]
            #     Data.c_ls[i][0:33] = Data.c_ls[i][32::-1]
            # Closing opened loops
            # self.alphas[i][-1] = self.alphas[i][0]
            # self.c_ls[i][-1] = self.c_ls[i][0]

    def training_data_generation(self):
        arrayed_alpha = np.array(self.alphas)
        arrayed_cl = np.array(self.c_ls)

        x_training_set = 1 * arrayed_alpha  # This multiplication is to facilitate training and representation// not here for the moment
        y_training_set = 1 * arrayed_cl

        return np.hstack((x_training_set, y_training_set))


Data = PolarData('Polars')
Data.point_uniformation()
a = Data.training_data_generation()
print("---")
