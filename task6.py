'''
 Number of matches won per team per year in IPL
'''

import csv
import matplotlib.pyplot as plt


def find_no_of_wins_by_team_by_season(file):
    '''
    This function will go through file and create a dictionary for team as key and for value 
    it will use another dictiontion where key is year and value is no of games won
    '''

    no_of_wins_by_team_by_season = {}
    with open(file, 'r', encoding='utf8') as open_file:
        matches = csv.DictReader(open_file)
        for match in matches:
            team = match['winner']
            season = match['season']
            if team not in no_of_wins_by_team_by_season:
                no_of_wins_by_team_by_season[team] = {}
            if season not in no_of_wins_by_team_by_season[team]:
                no_of_wins_by_team_by_season[team][season] = 1
            else:
                no_of_wins_by_team_by_season[team][season] += 1

    return no_of_wins_by_team_by_season


def create_list_of_team_and_match_won(no_of_wins_by_team_by_season):
    '''
    This Function will generate list of team and it will also generate
    a nested list containing no of game won by each team 
    '''

    #Fixing the error in data removing unnecessary data
    del no_of_wins_by_team_by_season['']

    list_of_teams = list(no_of_wins_by_team_by_season.keys())
    list_of_wins_by_each_team_each_season = []

    for team in no_of_wins_by_team_by_season:
        list_of_win_by_one_team = []
        for year in range(2008, 2018):
            if str(year) in no_of_wins_by_team_by_season[team]:
                list_of_win_by_one_team.append(
                    no_of_wins_by_team_by_season[team][str(year)])
            else:
                list_of_win_by_one_team.append(0)
        list_of_wins_by_each_team_each_season.append(list_of_win_by_one_team)
    return (list_of_teams, list_of_wins_by_each_team_each_season)


def plotting_a_stack_bar(list_of_teams, list_of_wins_by_each_team_each_season):
    '''
    This function will generate the stack bar graph
    '''
    bottom_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i, team in enumerate(list_of_teams):
        (plt.bar([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
                 list_of_wins_by_each_team_each_season[i],
                 bottom=bottom_values,
                 label=f'{i}:{team}'))

        #change bottom values
        for j in range(10):
            bottom_values[j] = bottom_values[
                j] + list_of_wins_by_each_team_each_season[i][j]

    plt.xlabel('Seasons')
    plt.ylabel('Number of wins')
    plt.title('Number of matches won by each team each year')
    plt.legend()
    plt.show()


def run():
    '''
    This function will runn all the function
    '''
    file = 'matches.csv'
    no_of_wins_by_team_by_season = find_no_of_wins_by_team_by_season(file)
    list_of_teams, list_of_wins_by_each_team_each_season = (
        create_list_of_team_and_match_won(no_of_wins_by_team_by_season))
    plotting_a_stack_bar(list_of_teams, list_of_wins_by_each_team_each_season)


run()
