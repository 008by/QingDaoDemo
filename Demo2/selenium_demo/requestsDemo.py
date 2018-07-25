import requests
import unittest


class ITest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8080/Supermarket/analysis/lookupprice?goodsCode="

    def test_lookupprice(self):
        gc = {"pId": "123456"}
        r = requests.get(self.url,params=gc)
        requests.post(self.url,data="")
        result = r.json();
        print(result)
        self.assertEqual(result['good']['res'], 'ok')



if __name__ == '__main__':
        unittest.main()
