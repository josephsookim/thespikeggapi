class Match:
    def __init__(self, team1: str, team2: str, score1: str, score2: str, event: str, url_path: str):
        self._team1 = team1
        self._team2 = team2
        self._score1 = score1
        self._score2 = score2
        self._event = event
        self._url_path = url_path

    def get_dict(self) -> {str: str}:
        return {
            'team1': self._team1,
            'team2': self._team2,
            'score1': self._score1,
            'score2': self._score2,
            'event': self._event,
            'url_path': self._url_path
        }


class Player:
    def __init__(self, ign: str, name: str, url_path: str):
        self._ign = ign
        self._name = name
        self._url_path = url_path

    def get_dict(self) -> {str: str}:
        return {
            'ign': self._ign,
            'name': self._name,
            'url_path': self._url_path
        }


class Team:
    def __init__(self, name: str, roster: [Player], rank: str, points: str):
        self._name = name
        self._roster = roster
        self._rank = rank
        self._points = points

    def get_dict(self) -> {str: str or dict}:
        return {
            'name': self._name,
            'roster': [player.get_dict() for player in self._roster],
            'rank': self._rank,
            'points': self._points
        }


class Article:
    def __init__(self, title: str, date: str, comment_count: str, url_path: str):
        self._title = title
        self._date = date
        self._comment_count = comment_count
        self._url_path = url_path

    def get_dict(self) -> {str: str}:
        return {
            'title': self._title,
            'date': self._date,
            'comment_count': self._comment_count,
            'url_path': self._url_path
        }
