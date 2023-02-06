import requests

API_KEY = ''
SPORT = 'americanfootball_nfl'
REGIONS = 'us'
MARKETS = 'h2h,spreads'
ODDS_FORMAT = 'american'
DATE_FORMAT = 'iso'
BOOKMAKERS = 'fanduel'

odds_response = requests.get(
    f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
        'bookmakers': BOOKMAKERS,
    }
)

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json), '\n')
    for i in range(len(odds_json)):
        line = odds_json[i]['bookmakers'][0]['markets'][0]['outcomes']
        time = odds_json[i]['commence_time']
        odds1 = line[0]['price']
        odds2 = line[1]['price']
        name1 = line[0]['name']
        name2 = line[1]['name']
        if odds1 > 0:
            odds1 = '+' + str(odds1)
        if odds2 > 0:
            odds2 = '+' + str(odds2)

        odds1 = str(odds1)
        odds2 = str(odds2)

        print('Time:', time)
        print(name1 + ' (' + odds1 + ')' + '\n' + name2 + ' (' + odds2 + ')\n')
