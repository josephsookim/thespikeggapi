import requests
from bs4 import BeautifulSoup
import re

from .models import Match


class Spike:
    base_url = 'https://www.thespike.gg'

    @staticmethod
    def get_match_results() -> [dict]:
        response = requests.get(
            f'{Spike.base_url}/matches/results')

        soup = BeautifulSoup(response.content, 'html.parser')
        matches = soup.findAll(
            'li', {'class': 'single-match element-trim-button main-colour-background'})

        match_list = [
            Match(
                *[team for team in ' '.join(re.split('\s+', match.find('div', {'class': 'match-info-match'}).text)).strip().split(' vs ')],
                *[match.find('span', {'class': f'team-{num}'}).text.strip() for num in (1, 2)],
                match.find('div', {'class': 'match-info-event'}).text.strip(),
                match.find('a')['href']
            )
            for match in matches
        ]

        return [match.get_info_dict() for match in match_list]

    @ staticmethod
    def get_rankings():
        pass

    @ staticmethod
    def get_news():
        pass
