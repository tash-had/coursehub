import requests
import json
import copy
from html.parser import HTMLParser
from bs4 import BeautifulSoup

inside_eval = False
list_courses = []
course_dict = {}
list_dict_courses = []


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        global inside_eval, course_dict

        if tag == 'tr':
            for attr in attrs:
                if (attr[0] == 'id') and ('wsGridRowID' in attr[1]):
                    course_dict.clear()
                    course_dict['courseInfo'] = []
                    inside_eval = True

                if inside_eval is True:
                    if attr[0] == 'pk':
                        course_dict['pk'] = attr[1]
                    elif attr[0] == 'sk':
                        course_dict['sk'] = attr[1]

    def handle_endtag(self, tag):

        global inside_eval, course_dict, list_courses
        if tag == 'tr' and inside_eval is True:
            savedDict = copy.deepcopy(course_dict)
            list_courses.append(savedDict)
            inside_eval = False

    def handle_data(self, data):
        global inside_eval, course_dict
        if inside_eval == True:
            data = data.strip()
            if len(data) != 0:
                course_dict['courseInfo'].append(data)

    def find_course_code(self, course_code, courseTitle):
        startInd = courseTitle.find(course_code)
        return courseTitle[startInd:startInd + 8]

    def calculate_rating(self, list_of_course_evals):
        list_all_ratings = []
        total_students = 0
        for evals in list_of_course_evals:
            # put into dict with the key as the course code
            num_students = int(evals[len(evals) - 1])
            total_students += num_students

            reccommended_rating = float(evals[len(evals) - 3]) * num_students
            difficulty_rating = float(evals[len(evals) - 4]) * num_students

            temp_ratings = [difficulty_rating, reccommended_rating]
            list_all_ratings.append(copy.deepcopy(temp_ratings))

        difficulty_rating_total = 0
        reccommended_rating_total = 0

        list_of_course_evals.clear()
        for rating in list_all_ratings:
            difficulty_rating_total += rating[0]
            reccommended_rating_total += rating[1]
        if total_students == 0:
            list_of_course_evals = [0, 0, 0]
            return list_of_course_evals
        list_of_course_evals = [round(difficulty_rating_total / total_students, 1), round(reccommended_rating_total / total_students, 1), total_students]
        return list_of_course_evals

    def printList(self, course_code):
        global list_courses
        global list_dict_courses
        dict_for_courses_list = {}
        # print(len(list_courses))
        for l in list_courses:
            course_info_list = l['courseInfo']
            if ('2018' in course_info_list) or ('2017' in course_info_list):
                course_code_full = self.find_course_code(course_code, course_info_list[2])
                course_info_list[2] = course_code_full
                if dict_for_courses_list.get(course_code_full) is None:
                    dict_for_courses_list[course_code_full] = []
                dict_for_courses_list[course_code_full].append(course_info_list)

        for course in dict_for_courses_list:
            dict_for_courses_list[course] = self.calculate_rating(dict_for_courses_list[course])
        return dict_for_courses_list


def find_course_ratings(course_code):

    url = "https://course-evals.utoronto.ca/BPI/fbview-WebService.asmx/getFbvGrid"

    payload_str = '\"strUiCultureIn\":\"en-US\",\"datasourceId\":\"7160\",\"blockId\":\"2330\",\"subjectColId\":\"1\",\"subjectValue\":\"____[-1]____\",\"detailValue\":\"____[-1]____\",\"gridId\":\"fbvGrid\",\"pageActuelle\":1,\"strOrderBy\":[\"col_1\",\"asc\"],\"strFilter\":[\"\",\"{}\",\"ddlFbvColumnSelectorLvl1\",\"\"],\"sortCallbackFunc\":\"__getFbvGrid\",\"userid\":\"4R7rrxj8fgXOTDE_LF_ka3QKFm_bqQF0Qj_3\",\"pageSize\":\"2000\"'.format(course_code)

    payload = "{" + payload_str + "}"
    headers = {
        'origin': "https://course-evals.utoronto.ca",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'content-type': "application/json; charset=UTF-8",
        'accept': "*/*",
        'referer': "https://course-evals.utoronto.ca/BPI/fbview.aspx?blockid=4odZr4oKMguTMDb3lu&userid=4R7rrxj8fgXOTDE_LF_ka3QKFm_bqQF0Qj_3&lng=en",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'cookie': 's_serial=%7B%22FTASBA%22%3A%5B%2210.1002%2Fwcs.32%22%5D%2C%22FTASBP%22%3A%5B%2210.1002%2F%28ISSN%291939-5086%22%5D%7D; s_fid=600EB21D59319DFE-1A0F3EE83BFB8BB8; AMCV_774C31DD5342CAF40A490D44%40AdobeOrg=793872103%7CMCIDTS%7C17242%7CMCMID%7C64357226451117272466250146897599312126%7CMCAAMLH-1490292715%7C7%7CMCAAMB-1490292715%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; __csess=1489991819228.5DAKKR.; _4c_=fVJdaxs7EP0rF0H3yZX1udIalmLSxATSNlD6HLSS1ha1LSPJ9jXG%2Fz0jE0PTlu7Lzpxz5mg0ozM6rvwWzajoCGGdZky0coJ%2B%2BlNGszNKwdXfAc2Q0h2jdnSUdIPtHBmZ5QNlAxl1R7wZ0QT9f%2FVRSkoueEv5ZYLs7q3%2BjB5i8tl7sLpFE%2FQj%2B7RIcQ8qtC8xxW2JLxsTtsA9p%2Bj2tjxCB2j%2B7es9QPu0hmRVym42nS4jXpq1X9ZybOMGb07GWp8zXochmXTCN0dszXSXpwG7%2BGnXV68mH%2Ftjs%2B%2FfndkceoZpE0qfmuD6xfzp%2FoO6mwspBZFC8sZkgKVrFXd21MQaorwig%2FCEjJ4TTiHQ0KYL2caDT6fvPh2C9Y%2BfoWvAi08bGGsNhxSPcHdI7lYpbvx%2FUgEaK%2FvFWAiTH31KVwVkOZQ6uHf3BdhGV2HaYY7ZxwNmgI11lpS2QiraUoWp0C2XHdX1gF3dZFWtowUvSGD5E7SYv1x7%2FHsZrPHXzQqmGUAuuKe4fHi%2BvQ%2F62wN4k9UTrwL2B90CHbZjLMnYf8h0dYG9X2l6owkRRGtJWgJzLUBTIUj9LpfLKw%3D%3D; optimizelyEndUserId=oeu1497898989151r0.7239100040982731; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=2096510701%7CMCIDTS%7C17337%7CMCMID%7C87801646313437230121681507781644206750%7CMCAAMLH-1498503790%7C7%7CMCAAMB-1498503790%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497906190s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.0.0; AMCVS_242B6472541199F70A4C98A6%40AdobeOrg=1; AMCV_242B6472541199F70A4C98A6%40AdobeOrg=1099438348%7CMCIDTS%7C17337%7CMCMID%7C87818175454228393671680911223479938781%7CMCAAMLH-1498508582%7C7%7CMCAAMB-1498508582%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497910982s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.1.0; ist_usr_page=1; adblock=blocked; _sdsat_DMC_or_CCODE=null; _sdsat_utm_source=; _sdsat_utm_medium=; _sdsat_utm_term=; _sdsat_utm_content=; sat_ppv=77; optimizelySegments=%7B%22204658328%22%3A%22false%22%2C%22204728159%22%3A%22none%22%2C%22204736122%22%3A%22referral%22%2C%22204775011%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; s_sess=%20v31%3D1497898989698%3B%20e41%3D1%3B%20s_cpc%3D0%3B; s_cc=true; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1497906081240%3B%20v68%3D1497904280679%7C1497906081246%3B%20v8%3D1497904605143%7C1592512605143%3B%20v8_s%3DLess%2520than%25201%2520day%7C1497906405143%3B; _vis_opt_test_cookie=1; _ga=GA1.2.1164571617.1486359187; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C17726%7CMCMID%7C87196995694785983511697324701033975381%7CMCAAMLH-1532053063%7C7%7CMCAAMB-1532053063%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1531455463s%7CNONE%7CMCAID%7C2DA4056F0507DF00-6000010BC000080B%7CMCSYNCSOP%7C411-17733%7CvVersion%7C3.0.0; s_sq=ithakajstorprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Darticle%252520view%2526link%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526region%253DloadingBody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Darticle%252520view%2526pidt%253D1%2526oid%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526oidt%253D3%2526ot%253DSUBMIT; utag_main=v_id:0164916e005000123a206443789b03078004a07000838$_sn:1$_ss:0$_st:1531450074411$ses_id:1531448262739%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:utoronto.ca; __utmc=229443032; __utma=229443032.1164571617.1486359187.1532630007.1533750013.2; __utmz=229443032.1533750013.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); s_serial=%7B%22FTASBA%22%3A%5B%2210.1002%2Fwcs.32%22%5D%2C%22FTASBP%22%3A%5B%2210.1002%2F%28ISSN%291939-5086%22%5D%7D; s_fid=600EB21D59319DFE-1A0F3EE83BFB8BB8; AMCV_774C31DD5342CAF40A490D44%40AdobeOrg=793872103%7CMCIDTS%7C17242%7CMCMID%7C64357226451117272466250146897599312126%7CMCAAMLH-1490292715%7C7%7CMCAAMB-1490292715%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; __csess=1489991819228.5DAKKR.; _4c_=fVJdaxs7EP0rF0H3yZX1udIalmLSxATSNlD6HLSS1ha1LSPJ9jXG%2Fz0jE0PTlu7Lzpxz5mg0ozM6rvwWzajoCGGdZky0coJ%2B%2BlNGszNKwdXfAc2Q0h2jdnSUdIPtHBmZ5QNlAxl1R7wZ0QT9f%2FVRSkoueEv5ZYLs7q3%2BjB5i8tl7sLpFE%2FQj%2B7RIcQ8qtC8xxW2JLxsTtsA9p%2Bj2tjxCB2j%2B7es9QPu0hmRVym42nS4jXpq1X9ZybOMGb07GWp8zXochmXTCN0dszXSXpwG7%2BGnXV68mH%2Ftjs%2B%2FfndkceoZpE0qfmuD6xfzp%2FoO6mwspBZFC8sZkgKVrFXd21MQaorwig%2FCEjJ4TTiHQ0KYL2caDT6fvPh2C9Y%2BfoWvAi08bGGsNhxSPcHdI7lYpbvx%2FUgEaK%2FvFWAiTH31KVwVkOZQ6uHf3BdhGV2HaYY7ZxwNmgI11lpS2QiraUoWp0C2XHdX1gF3dZFWtowUvSGD5E7SYv1x7%2FHsZrPHXzQqmGUAuuKe4fHi%2BvQ%2F62wN4k9UTrwL2B90CHbZjLMnYf8h0dYG9X2l6owkRRGtJWgJzLUBTIUj9LpfLKw%3D%3D; optimizelyEndUserId=oeu1497898989151r0.7239100040982731; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=2096510701%7CMCIDTS%7C17337%7CMCMID%7C87801646313437230121681507781644206750%7CMCAAMLH-1498503790%7C7%7CMCAAMB-1498503790%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497906190s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.0.0; AMCVS_242B6472541199F70A4C98A6%40AdobeOrg=1; AMCV_242B6472541199F70A4C98A6%40AdobeOrg=1099438348%7CMCIDTS%7C17337%7CMCMID%7C87818175454228393671680911223479938781%7CMCAAMLH-1498508582%7C7%7CMCAAMB-1498508582%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497910982s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.1.0; ist_usr_page=1; adblock=blocked; _sdsat_DMC_or_CCODE=null; _sdsat_utm_source=; _sdsat_utm_medium=; _sdsat_utm_term=; _sdsat_utm_content=; sat_ppv=77; optimizelySegments=%7B%22204658328%22%3A%22false%22%2C%22204728159%22%3A%22none%22%2C%22204736122%22%3A%22referral%22%2C%22204775011%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; s_sess=%20v31%3D1497898989698%3B%20e41%3D1%3B%20s_cpc%3D0%3B; s_cc=true; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1497906081240%3B%20v68%3D1497904280679%7C1497906081246%3B%20v8%3D1497904605143%7C1592512605143%3B%20v8_s%3DLess%2520than%25201%2520day%7C1497906405143%3B; _vis_opt_test_cookie=1; _ga=GA1.2.1164571617.1486359187; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C17726%7CMCMID%7C87196995694785983511697324701033975381%7CMCAAMLH-1532053063%7C7%7CMCAAMB-1532053063%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1531455463s%7CNONE%7CMCAID%7C2DA4056F0507DF00-6000010BC000080B%7CMCSYNCSOP%7C411-17733%7CvVersion%7C3.0.0; s_sq=ithakajstorprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Darticle%252520view%2526link%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526region%253DloadingBody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Darticle%252520view%2526pidt%253D1%2526oid%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526oidt%253D3%2526ot%253DSUBMIT; utag_main=v_id:0164916e005000123a206443789b03078004a07000838$_sn:1$_ss:0$_st:1531450074411$ses_id:1531448262739%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:utoronto.ca; __utmc=229443032; __utma=229443032.1164571617.1486359187.1532630007.1533750013.2; __utmz=229443032.1533750013.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); s_serial=%7B%22FTASBA%22%3A%5B%2210.1002%2Fwcs.32%22%5D%2C%22FTASBP%22%3A%5B%2210.1002%2F%28ISSN%291939-5086%22%5D%7D; s_fid=600EB21D59319DFE-1A0F3EE83BFB8BB8; AMCV_774C31DD5342CAF40A490D44%40AdobeOrg=793872103%7CMCIDTS%7C17242%7CMCMID%7C64357226451117272466250146897599312126%7CMCAAMLH-1490292715%7C7%7CMCAAMB-1490292715%7CNRX38WO0n5BH8Th-nqAG_A%7CMCAID%7CNONE; __csess=1489991819228.5DAKKR.; _4c_=fVJdaxs7EP0rF0H3yZX1udIalmLSxATSNlD6HLSS1ha1LSPJ9jXG%2Fz0jE0PTlu7Lzpxz5mg0ozM6rvwWzajoCGGdZky0coJ%2B%2BlNGszNKwdXfAc2Q0h2jdnSUdIPtHBmZ5QNlAxl1R7wZ0QT9f%2FVRSkoueEv5ZYLs7q3%2BjB5i8tl7sLpFE%2FQj%2B7RIcQ8qtC8xxW2JLxsTtsA9p%2Bj2tjxCB2j%2B7es9QPu0hmRVym42nS4jXpq1X9ZybOMGb07GWp8zXochmXTCN0dszXSXpwG7%2BGnXV68mH%2Ftjs%2B%2FfndkceoZpE0qfmuD6xfzp%2FoO6mwspBZFC8sZkgKVrFXd21MQaorwig%2FCEjJ4TTiHQ0KYL2caDT6fvPh2C9Y%2BfoWvAi08bGGsNhxSPcHdI7lYpbvx%2FUgEaK%2FvFWAiTH31KVwVkOZQ6uHf3BdhGV2HaYY7ZxwNmgI11lpS2QiraUoWp0C2XHdX1gF3dZFWtowUvSGD5E7SYv1x7%2FHsZrPHXzQqmGUAuuKe4fHi%2BvQ%2F62wN4k9UTrwL2B90CHbZjLMnYf8h0dYG9X2l6owkRRGtJWgJzLUBTIUj9LpfLKw%3D%3D; optimizelyEndUserId=oeu1497898989151r0.7239100040982731; AMCVS_4D6368F454EC41940A4C98A6%40AdobeOrg=1; AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=2096510701%7CMCIDTS%7C17337%7CMCMID%7C87801646313437230121681507781644206750%7CMCAAMLH-1498503790%7C7%7CMCAAMB-1498503790%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497906190s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.0.0; AMCVS_242B6472541199F70A4C98A6%40AdobeOrg=1; AMCV_242B6472541199F70A4C98A6%40AdobeOrg=1099438348%7CMCIDTS%7C17337%7CMCMID%7C87818175454228393671680911223479938781%7CMCAAMLH-1498508582%7C7%7CMCAAMB-1498508582%7CNRX38WO0n5BH8Th-nqAG_A%7CMCOPTOUT-1497910982s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17344%7CvVersion%7C2.1.0; ist_usr_page=1; adblock=blocked; _sdsat_DMC_or_CCODE=null; _sdsat_utm_source=; _sdsat_utm_medium=; _sdsat_utm_term=; _sdsat_utm_content=; sat_ppv=77; optimizelySegments=%7B%22204658328%22%3A%22false%22%2C%22204728159%22%3A%22none%22%2C%22204736122%22%3A%22referral%22%2C%22204775011%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; s_sess=%20v31%3D1497898989698%3B%20e41%3D1%3B%20s_cpc%3D0%3B; s_cc=true; s_pers=%20c19%3Dsd%253Aproduct%253Ajournal%253Aarticle%7C1497906081240%3B%20v68%3D1497904280679%7C1497906081246%3B%20v8%3D1497904605143%7C1592512605143%3B%20v8_s%3DLess%2520than%25201%2520day%7C1497906405143%3B; _vis_opt_test_cookie=1; _ga=GA1.2.1164571617.1486359187; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C17726%7CMCMID%7C87196995694785983511697324701033975381%7CMCAAMLH-1532053063%7C7%7CMCAAMB-1532053063%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1531455463s%7CNONE%7CMCAID%7C2DA4056F0507DF00-6000010BC000080B%7CMCSYNCSOP%7C411-17733%7CvVersion%7C3.0.0; s_sq=ithakajstorprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Darticle%252520view%2526link%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526region%253DloadingBody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Darticle%252520view%2526pidt%253D1%2526oid%253DI%252520accept%25252C%252520proceed%252520to%252520PDF%2526oidt%253D3%2526ot%253DSUBMIT; utag_main=v_id:0164916e005000123a206443789b03078004a07000838$_sn:1$_ss:0$_st:1531450074411$ses_id:1531448262739%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:utoronto.ca; __utmc=229443032; __utma=229443032.1164571617.1486359187.1532630007.1533750013.2; __utmz=229443032.1533750013.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        'cache-control': "no-cache",
        'postman-token': "eb912eea-3be0-4c42-a3ae-df30b64f91cb"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    json_dict = response.json()
    json_str = str(json_dict)
    json_str = json_str[8:len(json_str)-3]
    json_str = json_str.replace('\\n', '').replace('\\', '')

    soup = BeautifulSoup(json_str, 'html.parser')
    soup_str = soup.prettify()

    parser = MyHTMLParser()
    parser.feed(soup_str)

    ret_val = parser.printList(course_code)
    return ret_val