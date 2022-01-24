import requests
import json
import pandas as pd


def parse_response(response):
    """
    Parses response from api server
    and loads json file
    :param response: api request
    :return: list of dictionaries
    """

    if response.status_code == 200:
        data = json.loads(response.content)
    else:
        raise Exception("Unexpected response (%s: %s)." % (response.status_code, response.reason))

    return data


def api_r(artist):
    """
    Shows year of formation and country of origin of artist
    :param artist: artist name
    :return: dataframe
    """
    r = pd.DataFrame({'artist_name': [], 'formed_year': [], 'country': []})

    for i in artist:
        response = requests.get("http://theaudiodb.com/api/v1/json/2/search.php?s={}".format(i))
        data = parse_response(response)
        if data:
            art = data.get('artists')
            r = r.append({'artist_name': "".join([a.get('strArtist') for a in art]),
                          'formed_year': "".join([a.get('intFormedYear') for a in art]),
                          'country': "".join([a.get('strCountry') for a in art])}, ignore_index=True)
        else:
            raise Exception("Couldn't get data.")

    return r
