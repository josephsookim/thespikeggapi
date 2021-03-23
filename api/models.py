class Match:
    def __init__(self, team1: str, team2: str, score1: str, score2: str, event: str, url_path: str):
        self._team1 = team1
        self._team2 = team2
        self._score1 = score1
        self._score2 = score2
        self._event = event
        self._url_path = url_path

    def get_info_dict(self) -> {str: str}:
        return {
            'team1': self._team1,
            'team2': self._team2,
            'score1': self._score1,
            'score2': self._score2,
            'event': self._event,
            'url_path': self._url_path
        }