from urllib import request
from urllib.parse import urlencode
import json

BASE_URL = "http://smfu.in/api"


class Shortener:
    """
    Provides an API wrapper for http://smfu.in/api - a URL shortening service.
    """
    def __init__(self, url=None, key=None):
        self.post_data = dict(url=url)
        self._setkey(key)

    def __repr__(self):
        return 'URL shortener for {}'.format(self.post_data['url'])

    def _setkey(self, key):
        self.post_data['key'] = key

    @property
    def _get_time(self):
        self._time_response = request.urlopen(BASE_URL + '/getTime')
        self._time_content = self._time_response.read()
        return json.loads(self._time_content.decode('utf-8'))

    @property
    def _get_marker(self):
        self._mark_response = request.urlopen(BASE_URL + '/genMarker')
        self._mark_content = self._mark_response.read()
        return json.loads(self._mark_content.decode('utf-8'))

    @property
    def _dock_request(self):
        self.dock_post = {'key': self.post_data['key'],
                          'marker': self.post_data['userMarker'],
                          'time': self.post_data['time']}
        self._dock_response = request.urlopen(BASE_URL + '/dockRequestReady',
                                bytes(urlencode(self.dock_post), encoding='utf-8'))
        self._dock_content = self._dock_response.read()
        return json.loads(self._dock_content.decode('utf-8'))

    @property
    def _prepare_request(self):

        if not self.post_data['key']:
            raise Exception('Must specify API key')

        self.post_data.update(**self._get_time)
        self.post_data.update(**self._get_marker)
        self.post_data.update(**self._dock_request)

    def shorten(self, full_url_only=True):
        self._prepare_request
        self._shorten_request = request.urlopen(BASE_URL + '/shorten',
                                    bytes(urlencode(self.post_data), encoding='utf-8'))
        self._shorten_content = self._shorten_request.read()
        self.return_json = json.loads(self._shorten_content.decode('utf-8'))
        if full_url_only:
            self.return_json[0]['urlkey'] = 'http://smfu.in/' + self.return_json[0]['urlkey']
        return self.return_json
