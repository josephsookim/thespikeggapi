# thespikeggapi

An Unofficial REST API for [TheSpike.GG](https://www.thespike.gg/).

Built by [Joseph Kim](https://github.com/josephsookim/)

## Current Endpoints

### `/matches/results`

- Method: `GET`
- Cached Time: 300 seconds(5 Minutes)
- Response:
  ```python
  [
    {
      'event': str,
      'score1': str
      'score2': str,
      'team1': str,
      'team2': str,
      'url_path': str,
    },
    # list of matches
  ]
  ```

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
