import requests
import unittest
from library_function import create_yadiskfolder




class Test_API(unittest.TestCase):

    def yandex_upload(self):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        respose = requests.get(url)
        print(respose.status_code)
        self.assertEqual(401, respose.status_code)


















