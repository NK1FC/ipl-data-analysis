'''
Stacked chart of matches played by team by season
'''

import csv
import matplotlib.pyplot as plt


def no_matches_of_teams_each_season(file):
    '''
    This function will go through file and create a dictionary for team as key and for value 
    it will use another dictiontion where key is year and value is no of games won 
    '''
    no_matches_of_teams_each_seasons = {}

    with open(file, 'r', encoding='utf8') as open_file:
        matches = csv.DictReader(open_file)

        for match in matches:
            team1 = match['team1']
            team2 = match['team2']
            season = match['season']
            if team1 not in no_matches_of_teams_each_seasons:
                no_matches_of_teams_each_seasons[team1] = {}
            if team2 not in no_matches_of_teams_each_seasons:
                no_matches_of_teams_each_seasons[team2] = {}
            no_matches_of_teams_each_seasons[team1][season] = (
                no_matches_of_teams_each_seasons[team1].get(season, 0) + 1)
            no_matches_of_teams_each_seasons[team2][season] = (
                no_matches_of_teams_each_seasons[team2].get(season, 0) + 1)
    return no_matches_of_teams_each_seasons


def list_of_team_and_no_of_game_play(no_matches_of_teams_each_seasons):
    '''
    This function will take the nested dictionary then it will
    got through each item of dictionary then returns a  tuple list of team 
    and list of matches played by each team in each season
    '''
    list_of_team = list(no_matches_of_teams_each_seasons.keys())
    list_of_match_played_by_team_each_season = []
    for team in no_matches_of_teams_each_seasons:
        matches_played_by_team = []
        for year in range(2008, 2018):
            year = str(year)
            if year in no_matches_of_teams_each_seasons[team]:
                matches_played_by_team.append(
                    no_matches_of_teams_each_seasons[team][year])
            else:
                matches_played_by_team.append(0)
        list_of_match_played_by_team_each_season.append(matches_played_by_team)
    return (list_of_team, list_of_match_played_by_team_each_season)


def plot_stack_bar(list_of_team, list_of_match_played_by_team_each_season):
    '''
    This function will plot the stack graph
    '''

    bottom_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, team in enumerate(list_of_team):
        (plt.bar(range(2008, 2018),
                 list_of_match_played_by_team_each_season[i],
                 bottom=bottom_value,
                 label=f"{i}:{team}"))

        for j in range(10):
            bottom_value[j] = bottom_value[
                j] + list_of_match_played_by_team_each_season[i][j]
    plt.xlabel('Seasons')
    plt.ylabel('Number of games')
    plt.legend()
    plt.title('Stacked chart of matches played by team by season')
    plt.show()


def run():
    '''
    This funnction will execute all the function
    '''
    file = 'matches.csv'
    no_matches_of_teams_each_seasons = no_matches_of_teams_each_season(file)
    list_of_team, list_of_match_played_by_team_each_season = (
        list_of_team_and_no_of_game_play(no_matches_of_teams_each_seasons))
    plot_stack_bar(list_of_team, list_of_match_played_by_team_each_season)


run()
