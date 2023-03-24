'''
Top batsman for Royal Challengers Bangalore
'''

import csv
from itertools import islice
import matplotlib.pyplot as plt


def runs_scored_by_rcb_batsmen(file):
    '''
    This function will loop through data and
    add rcb batsmen name with their runs in dictionary
    '''

    with open(file, 'r', encoding='utf8') as opened_file:
        deliveries = csv.DictReader(opened_file)
        runs_scored_by_batsmen = {}
        for delivery in deliveries:
            if delivery['batting_team'] == 'Royal Challengers Bangalore':
                batsmen = delivery['batsman']
                runs = delivery['batsman_runs']
                runs_scored_by_batsmen[batsmen] = runs_scored_by_batsmen.get(
                    batsmen, 0) + int(runs)
    return runs_scored_by_batsmen


def top_10_batsman_with_runs(runs_scored_by_batsman):
    '''
    This function will sort the dictionary and then slice to find top
    10 batsman
    '''
    sorted_runs_scored_by_batsman = dict(
        sorted(runs_scored_by_batsman.items(),
               key=lambda x: x[1],
               reverse=True))
    top_10_batsmans_with_runs = dict(
        islice(sorted_runs_scored_by_batsman.items(), 10))

    return top_10_batsmans_with_runs


def plot_line_graph(top_10_batsmans_with_runs):
    '''
    This function is used to plot line graph
    '''
    players = top_10_batsmans_with_runs.keys()
    runs = top_10_batsmans_with_runs.values()

    plt.plot(players, runs, marker='o')
    plt.xlabel('Runs')
    plt.ylabel('Runs Scored')
    plt.title('Top 10 RCB Batsman')
    plt.show()


def run():
    '''
    Execute all the code in order to plot the graph
    '''
    file = 'deliveries.csv'
    runs_scored_by_batsmen = runs_scored_by_rcb_batsmen(file)
    top_10_batsmans_with_runs = top_10_batsman_with_runs(
        runs_scored_by_batsmen)
    plot_line_graph(top_10_batsmans_with_runs)


run()
