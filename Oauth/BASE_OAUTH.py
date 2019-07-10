import json
import urllib.request
from urllib import parse
import requests


class OAuth_Base():
    def __init__(self, client_id, client_key, redirect_url):
        '''
         #初始化
        :param client_id:  应用id
        :param client_key: 秘钥
        :param redirect_url:  回调地址
        '''
        self.client_id = client_id
        self.client_key = client_key
        self.redirect_url = redirect_url

    def _get(self, url, data):
        request_url = '%s?%s' % (url, urllib.parse.urlencode(data))
        response = urllib.request.urlopen(request_url)
        return response.read()

    def _post(self, url, data):
        request = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(encoding='UTF8'))  # 1
        response = urllib.request.urlopen(request)
        return response.read()

    def get_auth_url(self):
        '''
        获取code
        :return:
        '''
        pass

    def get_access_token(self, code):
        '''
        获取access token
        :param code:
        :return:
        '''
        pass

    def get_open_id(self):
        '''
        获取openid
        :return:
        '''
        pass

    def get_email(self):
        pass


# github
class OAuth_github(OAuth_Base):

    def github_login(self):
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_url': self.redirect_url,
            'scope': 'user:email',
            'state': 1

        }
        url = 'https://github.com/login/oauth/authorize?%s' % urllib.parse.urlencode(params)
        return url

    def get_access_token(self, code):
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_key,
            'code': code,
            'redirect_uri': self.redirect_url
        }

        response = self._post('https://github.com/login/oauth/access_token', params)  # 此处为post方法
        result = urllib.parse.parse_qs(response, True)
        self.access_token = result[b'access_token'][0]
        return self.access_token

    def get_user_info(self):
        params = {
            'access_token': self.access_token,
        }
        response = self._get('https://api.github.com/user', params)
        res = json.loads(response.decode('utf-8'))
        self.openid = res.get('id', '')
        return res

    def get_auth_url(self):
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_url,
            'scope': 'user:email',
            'state': 1
        }
        url = 'https://github.com/login/oauth/authorize?%s' % urllib.parse.urlencode(params)
        return url

    def get_email(self):
        params = {'access_token': self.access_token}
        response = self._get('https://api.github.com/user/emails', params)
        result = json.loads(response.decode('utf-8'))
        return result[0]['email']


# wb
class OAuth_WB(OAuth_Base):

    def get_access_token(self, code):
        url = 'https://api.weibo.com/oauth2/access_token'

        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_key,
            'code': code,
            'redirect_uri': self.redirect_url
        }
        response = requests.request('POST', url, params=params)
        return json.loads(response.text)

    def get_user_info(self, access_token_uid):
        url = 'https://api.weibo.com/2/users/show.json'
        params = {
            'access_token': access_token_uid['uid'],
            'uid': access_token_uid['access_uid']
        }

        response = requests.request('GET', url, params=params)

        return json.loads(response.text)

    # def get_email(self):
    #     params = {'access_token': self.access_token}
    #     response = self._get('https://api.weibo.com/2/account/profile/email.json', params)
    #     res = json.loads(response.decode('utf-8'))
    #     return res[0]['email']
