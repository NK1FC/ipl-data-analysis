'''
Number of matches played per year for all the years in IPL
'''

import csv
import matplotlib.pyplot as plt


def no_of_matches_per_season(file):
    '''
    This function will return a dictionary containning number of matches per seasons
    '''
    no_of_matches_per_seasons = {}

    with open(file, 'r', encoding='utf8') as opened_file:
        allmatches = csv.DictReader(opened_file)

        for match in allmatches:
            year = match['season']
            no_of_matches_per_seasons[year] = no_of_matches_per_seasons.get(
                year, 0) + 1
    return no_of_matches_per_seasons


def sort_no_of_matches_per_seasons(no_of_matches_per_seasons):
    ''''
    Sorting the dictionary using keys
    '''
    no_of_matches_per_seasons = dict(
        sorted(no_of_matches_per_seasons.items(), key=lambda x: x[0]))
    return no_of_matches_per_seasons


def plot_bar_graph(no_of_matches_per_seasons):
    '''
    This function will plot the bar graph
    '''
    years = no_of_matches_per_seasons.keys()
    matches = no_of_matches_per_seasons.values()

    plt.bar(years, matches)
    plt.xlabel('Season')
    plt.ylabel('Number of matches')
    plt.title('Number of Matches per Season')
    plt.show()


def run():
    '''
    This funnction will execute all the functions
    '''
    file = 'matches.csv'
    no_of_matches_per_seasons = no_of_matches_per_season(file)
    no_of_matches_per_seasons = sort_no_of_matches_per_seasons(
        no_of_matches_per_seasons)
    plot_bar_graph(no_of_matches_per_seasons)


run()
