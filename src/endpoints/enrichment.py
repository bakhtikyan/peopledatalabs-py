import json

import requests


def enrichment(base_path, api_key, category, params: dict, *args):
    try:
        headers = {
            'Accept-Encoding': 'gzip',
        }

        params["api_key"] = api_key
        data = requests.get(url=f"{base_path}/{category}/enrich",
                            params=params, headers=headers)
        try:
            if data.status_code == 200:
                return json.loads(data.content.decode('utf-8'))
        except Exception as err:
            raise err
    except Exception as err:
        raise err
