import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(URL)
        return response.content

    def load_json(self):
        people_list = []
        people = json.loads(self.get_response_body())
        for person in people:
            people_list.append(person)
        return people_list
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()

# for person in set(name_and_job):
#     print(person)