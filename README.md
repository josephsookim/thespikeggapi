# thespikeggapi

An Unofficial REST API for [TheSpike.GG](https://www.thespike.gg/), a site for Valorant Esports match and news coverage.

Built by [Joseph Kim](https://github.com/josephsookim/)

## Current Endpoints

All endpoints are relative to https://thespikeggapi.herokuapp.com.

### `/matches/results`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  [
    {
      'event': str,
      'score1': str,
      'score2': str,
      'team1': str,
      'team2': str,
      'url_path': str
    },
    # list of matches (dictionaries)
  ]
  ```
  
### `/rankings`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
    'region_name': [
      {
        'name': str,
        'points': str,
        'rank': str,
        'roster': [
          {
            'ign': str,
            'name': str,
            'url_path': str
          },
          # list of players within team (dictionaries)
        ]
      },
      # list of teams within region (dictionaries)
    ],
    # dictionary of regions
  }
  ```
  
### `/news`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
    'time': [
      {
        'comment_count': str,
        'date': str,
        'title': str,
        'url_path': str
      },
      # list of articles (dictionaries)
    ],
    # dictionary of times (past, today, yesterday)
  }
  ```
  
## Installation
### Source
```
$ git clone https://github.com/josephsookim/thespikeggapi/
$ cd thespikeggapi
$ pip3 install -r requirements.txt
```

### Usage
```
python3 main.py
```

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Contributing

Feel free to submit a [pull request](https://github.com/josephsookim/thespikeggapi/pull/new/master) or an [issue](https://github.com/josephsookim/thespikeggapi/issues/new)!

## License
The MIT License (MIT)
