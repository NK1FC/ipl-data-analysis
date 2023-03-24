'''
# Total runs scored by team
'''
import csv
import matplotlib.pyplot as plt


def run_scored_by_team(file):
    ''''
    Creating a dictionary with team as key and run as value
    '''

    with open(file, 'r', encoding='utf8') as opened_file:
        deliveries = csv.DictReader(opened_file)

        run_per_team = dict()

        for delivery in deliveries:
            team = delivery["batting_team"]
            runs = delivery["total_runs"]
            run_per_team[team] = run_per_team.get(team, 0) + int(runs)

    return run_per_team


def plot_bar_graph(run_per_team):
    '''
    This function is used to plot bar graph
    '''

    team = run_per_team.keys()
    runs = run_per_team.values()

    plt.bar(team, runs)
    plt.xlabel('Teams')
    plt.ylabel('Runs')
    plt.title('Total runs scored by team')
    plt.gcf().autofmt_xdate()
    plt.show()


def run():
    '''
    Execute all the code in order to obtain required bar chart
    '''
    file = 'deliveries.csv'
    run_per_team = run_scored_by_team(file)
    plot_bar_graph(run_per_team)


run()
