#This program webscrapes race data from the official Formula1 website and converts the pandas dataframe to a csv file that is saved to the local repository.

import pandas as pd

#/////OVERALL F1 2022 SEASON STANDINGS/////

#Saves the website url into a global variable
url_1 = 'https://www.formula1.com/en/results.html/2022/races.html'
url_2 = 'https://www.formula1.com/en/results.html/2022/drivers.html'
url_3 = 'https://www.formula1.com/en/results.html/2022/team.html'

#Reads the website's html and saves it to a global variable
races_extract = pd.read_html(url_1)
drivers_extract = pd.read_html(url_2)
teams_extract = pd.read_html(url_3)

#Extracts the data table from the website's html file
races_df = races_extract[0]
drivers_df = drivers_extract[0]
teams_df = teams_extract[0]

#Updates the table to include only our desired data columns
races_finaltable = races_df[['Grand Prix', 'Date', 'Winner', 'Car', 'Laps', 'Time']]
drivers_finaltable = drivers_df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]
teams_finaltable = teams_df[['Pos', 'Team', 'PTS']]


#////F1 2022 INDIVIDUAL RACE STATISTICS////

#Creates a function that takes the dataframe from every race result page from the 2022 season and concatenates it all into one csv file.
def racedata_to_csv(race_urls):
    final_dfs = []
    for url in race_urls:
        url_extract = pd.read_html(url)
        df = url_extract[0]
        df_finaltable = df[['Pos', 'Driver', 'Car', 'Laps', 'Time/Retired', 'PTS']]
        final_dfs.append(df_finaltable)
    pd.concat(final_dfs).to_csv('F1 CSV Folder/GrandPrix_RaceData.csv', index=False)

#List of Grand Prix results
race_urls = ['https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html','https://www.formula1.com/en/results.html/2022/races/1125/saudi-arabia/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1108/australia/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1109/italy/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1110/miami/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1111/spain/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1112/monaco/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1126/azerbaijan/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1113/canada/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1114/great-britain/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1115/austria/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1116/france/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1117/hungary/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1118/belgium/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1119/netherlands/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1120/italy/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1133/singapore/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1134/japan/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1135/united-states/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1136/mexico/race-result.html',
             'https://www.formula1.com/en/results.html/2022/races/1137/brazil/race-result.html', 'https://www.formula1.com/en/results.html/2022/races/1138/abu-dhabi/race-result.html']

#Loop that takes all race results urls and changes them to fastest lap urls.
fastestLap_urls = []
for url in race_urls:
    url = url.replace('race-result', 'fastest-laps')
    fastestLap_urls.append(url)

#Creates a function that takes the dataframe from every fastest laps page from the 2022 season and concatenates it all into one csv file.
def fastestLap_to_csv(fastestLap_urls):
    final_dfs = []
    for url in fastestLap_urls:
        url_extract = pd.read_html(url)
        df = url_extract[0]
        df_finaltable = df[['Pos', 'Driver', 'Car', 'Lap', 'Time', 'Avg Speed']]
        final_dfs.append(df_finaltable)
    pd.concat(final_dfs).to_csv('F1 CSV Folder/GrandPrix_FastestLaps.csv', index=False)

#Loop that takes all race results urls and changes them to qualifying urls.
qual_urls = []
for url in race_urls:
    url = url.replace('race-result', 'qualifying')
    qual_urls.append(url)

# #Creates a function that takes the dataframe from every qualifying page from the 2022 season and concatenates it all into one csv file.
def qualifying_to_csv(qual_urls):
    final_dfs = []
    for url in qual_urls:
        url_extract = pd.read_html(url)
        df = url_extract[0]
        df_finaltable = df[['Pos', 'Driver', 'Car', 'Q1', 'Q2', 'Q3']]
        final_dfs.append(df_finaltable)
    pd.concat(final_dfs).to_csv('F1 CSV Folder/GrandPrix_Qualifying.csv', index=False)


#Creates overall season standings csv files.
races_finaltable.to_csv('F1 CSV Folder/races.csv', index=False)
drivers_finaltable.to_csv('F1 CSV Folder/drivers.csv', index=False)
teams_finaltable.to_csv('F1 CSV Folder/teams.csv', index=False)

#Calls the function that creates the Grand Prix csv file.
racedata_to_csv(race_urls)
fastestLap_to_csv(fastestLap_urls)
qualifying_to_csv(qual_urls)
