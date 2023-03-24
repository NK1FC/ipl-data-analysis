'''
Foreign umpire analysis
'''

import csv
import matplotlib.pyplot as plt


def no_umpires_from_different_country(file):
    '''
    This function will go through file and count number of umpires from
    different country
    '''
    umpires_from_different_country = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        umpires = csv.DictReader(opened_file)
        for umpire in umpires:
            country = umpire[' country']
            if country != ' India':
                umpires_from_different_country[country] = (
                    umpires_from_different_country.get(country, 0)) + 1
    return umpires_from_different_country


def plot_bar_graph(umpires_from_different_country):
    '''
    This function will plot the required bar graph
    '''
    country = umpires_from_different_country.keys()
    number_of_umpires = umpires_from_different_country.values()

    plt.bar(country, number_of_umpires)
    plt.xlabel('Country')
    plt.ylabel('Number of Umpires')
    plt.title('Number of Umpires per Country')
    plt.show()


def run():
    '''
    Execute all the code in order to obtain required bar chart
    '''
    file = 'umpires.csv'
    umpires_from_different_country = no_umpires_from_different_country(file)
    plot_bar_graph(umpires_from_different_country)


run()
