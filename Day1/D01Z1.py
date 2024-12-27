from dotenv import load_dotenv
import os
import requests

def get_data_from_link(url, session_cookie):
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get data from link: {url}")

def splitToList(data):
    data = data.split("\n")
    leftList = []
    rightList = []
    for i in data:
        valuesOfTwoList = i.split("   ")
        
        try:
            leftValue = int(valuesOfTwoList[0])
            rightValue = int(valuesOfTwoList[1])
            leftList.append(leftValue)
            rightList.append(rightValue)
        except:
            continue
    return leftList, rightList

def sortMultipleLists(*lists):
    sorted_lists = []
    for lst in lists:
        sorted_lists.append(sorted(lst))
    return sorted_lists


url = "https://adventofcode.com/2024/day/1/input"
load_dotenv()
session_cookie = os.getenv("SESSION_COOKIE")
data = get_data_from_link(url, session_cookie)
if data:
    leftSortedList, rightSortedList = splitToList(data)
    leftSortedList, rightSortedList = sortMultipleLists(leftSortedList, rightSortedList)
    measureDistanceBetweenTwoLists = sum([abs(leftSortedList[i] - rightSortedList[i]) for i in range(len(leftSortedList))])
    print(measureDistanceBetweenTwoLists)