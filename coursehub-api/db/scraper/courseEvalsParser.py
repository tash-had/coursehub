import requests
import json
import copy
from html.parser import HTMLParser
from bs4 import BeautifulSoup

insideEval = False
listCourses = []
courseDict = {}


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        global insideEval, courseDict

        if tag == 'tr':
            for attr in attrs:
                if (attr[0] == 'id') and ('wsGridRowID' in attr[1]):
                    courseDict.clear()
                    courseDict['courseInfo'] = []
                    insideEval = True

                if insideEval is True:
                    if attr[0] == 'pk':
                        courseDict['pk'] = attr[1]
                    elif attr[0] == 'sk':
                        courseDict['sk'] = attr[1]

    def handle_endtag(self, tag):

        global insideEval, courseDict, listCourses
        if tag == 'tr' and insideEval is True:
            savedDict = copy.deepcopy(courseDict)
            listCourses.append(savedDict)
            insideEval = False

    def handle_data(self, data):
        # print("Data     :", data
        global insideEval, courseDict
        if insideEval == True:
            data = data.strip()
            if len(data) != 0:
                courseDict['courseInfo'].append(data)

    def printList(self):
        global listCourses
        tempYearCourses = []
        for l in listCourses:
            courseInfoList = l['courseInfo']
            if ('2018' in courseInfoList) or ('2017' in courseInfoList):
                tempYearCourses.append(courseInfoList)

        listAllRatings = []
        totalStudents = 0
        for course in tempYearCourses:
            numStudents = int(course[len(course) - 1])
            totalStudents += numStudents

            recRating = float(course[len(course) - 3]) * numStudents
            difficultyRating = float(course[len(course) - 4]) * numStudents

            tempRatings = [difficultyRating, recRating]
            listAllRatings.append(copy.deepcopy(tempRatings))

        difficultyTotal = 0
        recTotal = 0
        for rating in listAllRatings:
            difficultyTotal += rating[0]
            recTotal += rating[1]

        return [round(difficultyTotal / totalStudents, 1), round(recTotal / totalStudents, 1), totalStudents]


def findCourseRatings(courseCode):
    with open ('cookieSpecificCourse.txt') as f:
        read_data = f.read()

    url = "https://course-evals.utoronto.ca/BPI/fbview-WebService.asmx/getFbvGrid"

    payloadSTR = '\"strUiCultureIn\":\"en-US\",\"datasourceId\":\"7160\",\"blockId\":\"2330\",\"subjectColId\":\"1\",\"subjectValue\":\"____[-1]____\",\"detailValue\":\"____[-1]____\",\"gridId\":\"fbvGrid\",\"pageActuelle\":1,\"strOrderBy\":[\"col_1\",\"asc\"],\"strFilter\":[\"\",\"{}\",\"ddlFbvColumnSelectorLvl1\",\"\"],\"sortCallbackFunc\":\"__getFbvGrid\",\"userid\":\"4R7rrxj8fgXOTDE_LF_ka3QKFm_bqQF0Qj_3\",\"pageSize\":\"100\"'.format(courseCode)

    payload = "{" + payloadSTR + "}"
    headers = {
        'origin': "https://course-evals.utoronto.ca",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'content-type': "application/json; charset=UTF-8",
        'accept': "*/*",
        'referer': "https://course-evals.utoronto.ca/BPI/fbview.aspx?blockid=4odZr4oKMguTMDb3lu&userid=4R7rrxj8fgXOTDE_LF_ka3QKFm_bqQF0Qj_3&lng=en",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'cookie': read_data,
        'cache-control': "no-cache",
        'postman-token': "eb912eea-3be0-4c42-a3ae-df30b64f91cb"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    jsonDict = response.json()
    jsonStr = str(jsonDict)
    jsonStr = jsonStr[8:len(jsonStr)-3]
    jsonStr = jsonStr.replace('\\n', '').replace('\\', '')

    soup = BeautifulSoup(jsonStr, 'html.parser')
    soupstr = soup.prettify()

    parser = MyHTMLParser()
    parser.feed(soupstr)

    retVal = parser.printList()
    retVal.append(courseCode)
    return retVal
