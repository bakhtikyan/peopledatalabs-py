from tests.util import *


def test_with_phone(enrichment_client):
    phone = {'phone': '4155688415'}
    data = enrichment_client.person().enrichment(phone)

    assert data['status'] == 200
    assert data['data']['full_name'] == 'sean thorne'
    assert data['data']['first_name'] == 'sean'
    assert data['data']['last_name'] == 'thorne'
    assert data['data']['gender'] == 'male'
    assert data['data']['birth_year'] == 1990
    assert data['data']['linkedin_url'] == 'linkedin.com/in/seanthorne'
    assert data['data']['facebook_url'] == 'facebook.com/deseanthorne'
    assert data['data']['twitter_url'] == 'twitter.com/seanthorne5'
    assert data['data']['work_email'] == 'sean@peopledatalabs.com'
    assert data['data']['mobile_phone'] == '+14155688415'
    assert data['data']['industry'] == 'computer software'


def test_with_likedin_profile(enrichment_client):
    profile = {'profile': ['linkedin.com/in/seanthorne']}
    data = enrichment_client.person().enrichment(profile)

    assert data['status'] == 200
    assert data['data']['full_name'] == 'sean thorne'
    assert data['data']['first_name'] == 'sean'
    assert data['data']['last_name'] == 'thorne'
    assert data['data']['gender'] == 'male'
    assert data['data']['birth_year'] == 1990
    assert data['data']['linkedin_url'] == 'linkedin.com/in/seanthorne'
    assert data['data']['facebook_url'] == 'facebook.com/deseanthorne'
    assert data['data']['twitter_url'] == 'twitter.com/seanthorne5'
    assert data['data']['work_email'] == 'sean@peopledatalabs.com'
    assert data['data']['mobile_phone'] == '+14155688415'
    assert data['data']['industry'] == 'computer software'


