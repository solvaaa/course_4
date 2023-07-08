import requests
import json

#API_URL = 'https://hh.ru/search/vacancy?text=Machine+learning&from=suggest_post&area=1'
#info = { text: 'Machine Learning' or 'Data Scientist', lang: 'eng=', speed: 2, voice: 'filipp', emotion: 'good' }
#json_str = json.dumps(info)
#answer = requests.post(API_URL, json_str)

class Description:
    def __init__(self, vacancy_name, vacancy_link, vacancy_salary, vacancy_description, working_condition, job_requirements):
        self.vacancy_name = vacancy_name
        self.vacancy_link = vacancy_link
        self.vacancy_salary = vacancy_salary
        self.vacancy_description = vacancy_description
        self.working_condition = working_condition
        self.job_requirements = job_requirements



