'''
Top 10 economical bowlers in the year 2015
'''

import csv
from itertools import islice
import matplotlib.pyplot as plt


def listing_matchid_in_2015(file):
    '''
    This will create a dictionary of all the match id for
    year 2015
    '''
    matchid = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        matches = csv.DictReader(opened_file)

        for match in matches:
            if match['season'] == '2015':
                matchid[match['id']] = 0
    return matchid


def number_of_balls_each_bowler(file, matchid):
    '''
    Returns Number of balls bowled by each bowler in form of dictionary
    '''
    numbers_of_balls_each_bowlers = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        deliveries = csv.DictReader(opened_file)
        for delivery in deliveries:
            if delivery['match_id'] in matchid:
                if int(delivery['noball_runs']) == 0 and int(
                        delivery['wide_runs']) == 0:
                    bowler = delivery['bowler']
                    numbers_of_balls_each_bowlers[bowler] = (
                        numbers_of_balls_each_bowlers.get(bowler, 0) + 1)
    return numbers_of_balls_each_bowlers


def runs_concieded_by_bowler(file, matchid):
    '''
    Returns Number of runs concieded by each bowler in form of dictionary
    '''
    runs_concieded_by_each_bowlers = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        deliveries = csv.DictReader(opened_file)
        for delivery in deliveries:
            if delivery['match_id'] in matchid:
                bowler = delivery['bowler']
                total_runs = int(delivery['total_runs'])
                leg_by = int(delivery['legbye_runs'])
                bye_runs = int(delivery['bye_runs'])
                penalty_run = int(delivery['penalty_runs'])
                runs = total_runs - leg_by - bye_runs - penalty_run
                runs_concieded_by_each_bowlers[bowler] = (
                    runs_concieded_by_each_bowlers.get(bowler, 0) + runs)
    return runs_concieded_by_each_bowlers


def economy_of_bowler(numbers_of_balls_each_bowlers,
                      runs_concieded_by_each_bowler):
    '''
    Return the economy of each bowler
    '''
    economy_of_each_bowler = {}
    for bowler in numbers_of_balls_each_bowlers:
        economy_of_each_bowler[bowler] = round(
            (runs_concieded_by_each_bowler[bowler] /
             numbers_of_balls_each_bowlers[bowler]) * 6, 2)
    return economy_of_each_bowler


def get_top_10_economy(economy_of_each_bowler):
    '''
    Find the top 10 economy bowler
    '''
    sorted_economy_of_each_bowler = dict(
        sorted(economy_of_each_bowler.items(), key=lambda x: x[1]))
    top_10_economy_bowler = dict(
        islice(sorted_economy_of_each_bowler.items(), 10))
    return top_10_economy_bowler


def plot_bar_graph(top_10_economy_bowler):
    '''
    Plot the bar graph
    '''
    bowler = top_10_economy_bowler.keys()
    economy = top_10_economy_bowler.values()

    plt.bar(bowler, economy)
    plt.title('Top 10 economy bowlers')
    plt.xlabel('Bowler Name')
    plt.ylabel('Economy')
    plt.gcf().autofmt_xdate()
    plt.show()


def run():
    '''
    This function will run all the functions
    '''
    file1 = 'matches.csv'
    file2 = 'deliveries.csv'
    matchid = listing_matchid_in_2015(file1)
    numbers_of_balls_each_bowlers = number_of_balls_each_bowler(file2, matchid)
    runs_concieded_by_each_bowler = runs_concieded_by_bowler(file2, matchid)
    economy_of_each_bowler = economy_of_bowler(numbers_of_balls_each_bowlers,
                                               runs_concieded_by_each_bowler)
    top_10_economy_bowler = get_top_10_economy(economy_of_each_bowler)
    plot_bar_graph(top_10_economy_bowler)


run()
