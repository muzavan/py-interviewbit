#!/usr/bin/python3

# pip install beautifulsoup4
from bs4 import BeautifulSoup

# pip install requests
import requests

class InterviewBit:
    def __init__(self, cookie):
        self.headers = {
            'Connection': 'keep-alive', 
            'Cache-Control': 'max-age=0', 
            'Upgrade-Insecure-Requests': '1', 
            'DNT': '1', 
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36', 
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
            'Sec-Fetch-Site': 'same-origin', 
            'Sec-Fetch-Mode': 'navigate', 
            'Sec-Fetch-User': '?1', 
            'Sec-Fetch-Dest': 'document', 
            'Referer': 'https://www.interviewbit.com/courses/programming/topics/arrays/', 
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6',
            'Cookie': cookie,
        }

    def get_programming_topics(self):
        r = requests.get('https://www.interviewbit.com/courses/programming/', headers=self.headers)

        soup = BeautifulSoup(r.text, 'html.parser')

        progs = soup.find_all('a', {
            'href': lambda x: x and x.startswith('/courses/programming/topics')
        })

        topic_hrefs = [p.get('href') for p in progs]
        topic_names = list(set(map(lambda x: x.split('/')[-2], topic_hrefs)))

        return topic_names

    def get_problems(self, topic):
        topic_url = f"https://www.interviewbit.com/courses/programming/topics/{topic}/"
        r = requests.get(topic_url, headers=self.headers)

        soup = BeautifulSoup(r.text, 'html.parser')

        problems = soup.find_all('tr', {
            'id': lambda x: x and x.startswith('problem_')
        })

        def get_problem_name(tr):
            tds = tr.find_all('td')
            if len(tds) < 1:
                return None

            problem_href = tds[0].a.get('href')
            problem_name = problem_href.split('/')[-2]

            return problem_name

        problem_names = map(get_problem_name, problems)
        problem_names = [s for s in problem_names if s] # remove None
        return problem_names
    
    def get_solved_code(self, problem):
        problem_url = f"https://www.interviewbit.com/problems/{problem}/"
        r = requests.get(problem_url, headers=self.headers)

        # parse result
        soup = BeautifulSoup(r.text, 'html.parser')

        # checked if it's solved or not
        # based on whether the complete solution already unlocked or not!
        hint_ul = soup.find('ul', {'class': 'hint-list'})
        if not hint_ul:
            return None
        
        lock_i_list = hint_ul.find_all('i')
        if len(lock_i_list) < 1:
            return None

        complete_lock = lock_i_list[-1]

        if 'fa-unlock-alt' not in complete_lock.get('class', []):
            return None

        # get the actual code
        editor_wrapper = soup.find('div', {'id': 'editor_wrapper'})
        
        code = None
        if editor_wrapper.textarea:
            code = editor_wrapper.textarea.get_text()

        return code


