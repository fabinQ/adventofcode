from dotenv import load_dotenv
import os
import requests

def getData():
    with open ("./data.txt", mode="r") as dataFromFile:
        data = dataFromFile.read()
    return data

def get_data_from_link(url, session_cookie):
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to get data from link: {url}")

def stringRaportToInt(data):
    raports = []
    for i in data:
        raport = []
        for j in i:
            raport.append(int(j))
        raports.append(raport)
    return raports

def splitToSingleRaport(data):
    data = data.split("\n")
    data = list(map(lambda x: x.split(" ") if " " in x else None, data))
    data = [x for x in data if x is not None]
    raports = stringRaportToInt(data)
    return raports

def sortMultipleLists(*lists):
    sorted_lists = []
    for lst in lists:
        sorted_lists.append(sorted(lst))
    return sorted_lists

def diffrenceOfNumbers(firstNumber, secondNumber):
    if abs(secondNumber - firstNumber) <=3:
        return True
    else:
        return False

def isAscending(raport):
    for i in range(len(raport) - 1):
        if raport[i]< raport[i + 1]:
            if diffrenceOfNumbers(raport[i], raport[i + 1]):
                continue
            else:
                return False, False
        elif i == 0:
            return False, True
        else: 
            return False, False
    return True, True

def isDescending(raport):
    for i in range(len(raport)-1):
        if raport[i] > raport[i+1]:
            if diffrenceOfNumbers(raport[i], raport[i+1]):
                continue
            else:
                return False
        else:
            return False
    return True

def CalculateValueRaport(raports):
    valueRaports = []
    for raport in raports:
        isAscendingCondition, maybeDescedingCondition =  isAscending(raport)
        if isAscendingCondition:
            valueRaports.append(raport)
        elif maybeDescedingCondition:
            if isDescending(raport):
                valueRaports.append(raport)
    return valueRaports

url = "https://adventofcode.com/2024/day/2/input"
load_dotenv()
session_cookie = os.getenv("SESSION_COOKIE")
data = get_data_from_link(url, session_cookie)
# data = getData()
if data:
    raports = splitToSingleRaport(data)
    valueRaports = CalculateValueRaport(raports)
    for index, value in enumerate(valueRaports):
        print(f"{index+1}: Value: {value}")
    print(f"Count of raports: {len(valueRaports)}")