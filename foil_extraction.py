#This file extracts the data into an array
import os

airfoil_folder = 'Airfoils'


airfoil_names = os.listdir(airfoil_folder)


directed_names = []

for name in airfoil_names:

    directed_names.append(os.path.join(airfoil_folder,name))



with open(directed_names[0]) as input_file:
    x_coordinate = []
    y_coordinate = []

    for mu, line in enumerate(input_file):

        if mu == 0:
            airfoil_name = line

        else:
            
            coordinate = [item.strip() for item in line.split('   ', 2)] # List comprehension. strip "eliminates" the shit at the beginning and end of each split.
            coordinate = list(map(float,coordinate[1:]))
            x_coordinate.append(coordinate[0])
            y_coordinate.append(coordinate[1])
            
    

        # stats = dict(zip(('kills', 'deaths', 'assists'),

        #                   map(int, stats.split('/'))))
        # date = tuple(map(int, date.split('-')))
        # info[player] = dict(zip(('stats', 'outcome', 'date'),

        #                         (stats, outcome, date)))



