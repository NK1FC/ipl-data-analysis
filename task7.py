'''
Extra runs conceded per team in the year 2016
'''

import csv
import matplotlib.pyplot as plt


def listing_matchid_in_2016(file):
    '''
    This will create a dictionary of all the match id for
    year 2016
    '''
    matchid = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        matches = csv.DictReader(opened_file)

        for match in matches:
            if match['season'] == '2016':
                matchid[match['id']] = 0
    return matchid


def extra_concieded_by_team(file, matchid):
    '''
    Extra runn concieded by team in 2016 year
    '''
    extras_concieded_by_teams = {}
    with open(file, 'r', encoding='utf8') as opened_file:
        deliveries = csv.DictReader(opened_file)

        for delivery in deliveries:
            if delivery['match_id'] in matchid:
                bowling_team = delivery['bowling_team']
                extra_runs = int(delivery['extra_runs'])
                extras_concieded_by_teams[bowling_team] = (
                    extras_concieded_by_teams.get(bowling_team, 0) +
                    extra_runs)

    return extras_concieded_by_teams


def plot_bar_graph(extras_concieded_by_teams):
    '''
    This function will plot the bar graph
    '''

    teams = extras_concieded_by_teams.keys()
    extra_runs = extras_concieded_by_teams.values()

    plt.bar(teams, extra_runs)
    plt.title('Extra runs conceded per team in the year 2016')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runns Concieded')
    plt.gcf().autofmt_xdate()
    plt.show()


def run():
    '''
    This function will execute all the functions
    '''
    file1 = 'matches.csv'
    file2 = 'deliveries.csv'
    matchid = listing_matchid_in_2016(file1)
    extras_concieded_by_teams = extra_concieded_by_team(file2, matchid)
    plot_bar_graph(extras_concieded_by_teams)


run()
