import json

import requests


def autocomplete(base_path, api_key, params: dict):
    try:
        headers = {
            'Accept-Encoding': 'gzip',
        }
        autocomplete_params = {'api_key': api_key,
                               'field': params['field']
                               }
        if 'text' in params:
            autocomplete_params['text'] = params['text'] or ''
        if 'size' in params:
            autocomplete_params['size'] = params['size'] or 10
        if 'pretty' in params:
            autocomplete_params['pretty'] = params['pretty'] or False

        data = requests.get(url=f"{base_path}/autocomplete",
                            params=autocomplete_params, headers=headers)
        try:
            if data.status_code == 200:
                return json.loads(data.content.decode('utf-8'))
        except Exception as err:
            raise err
    except Exception as err:
        raise err
