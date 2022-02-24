#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests
import json

def getWinnerTotalGoals(competition, year):
    # Write your code here
    URL = "https://jsonmock.hackerrank.com/api/football_competitions?name=" + competition + "&year=" + str(year)
    getData = requests.get(URL)
    getJson = json.loads(getData.content)
    team = ""
    for i in getJson['data']:
        team = i["winner"]
        break
    # re-trace
    url1 = "https://jsonmock.hackerrank.com/api/football_matches?competition=" + competition + "&year=" + str(
        year) + "&team1=" + team
    url2 = "https://jsonmock.hackerrank.com/api/football_matches?competition=" + competition + "&year=" + str(
        year) + "&team2=" + team

    # first team
    res1 = requests.get(url1)
    res1Json = json.loads(res1.content)

    # second team
    res2 = requests.get(url2)
    res2Json = json.loads(res2.content)

    # getting the total pages from the JSON
    itr1 = 1
    itr2 = 1

    page1 = res1Json['total_pages']
    page2 = res2Json['total_pages']

    # counting how many goals
    total = 0
    while itr1 <= page1:
        url1Update = "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team1={2}&page={3}".format(
            competition, year, team, itr1)
        res1Update = requests.get(url1Update)
        res1JsonUpdate = json.loads(res1Update.content)
        for i in res1JsonUpdate['data']:
            if i['team1'].upper() == team.upper():
                total += int(i['team1goals'])
        itr1 += 1

    while itr2 <= page2:
        url2Update = "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team2={2}&page={3}".format(
            competition, year, team, itr2)
        res2Update = requests.get(url2Update)
        res2JsonUpdate = json.loads(res2Update.content)
        for i in res2JsonUpdate['data']:
            if i['team2'].upper() == team.upper():
                total += int(i['team2goals'])
        itr2 += 1

    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
