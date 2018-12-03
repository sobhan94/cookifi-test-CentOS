import unittest
import requests
import json


class Large_Order_Api(unittest.TestCase):
    def add_dish(self, item):
        headers = {
            'Host': "cookifi.com",
            'Connection': "keep-alive",
            'Content-Length': "0",
            'Accept': "application/json, text/plain, */*",
            'Origin': "https://cookifi.com",
            'X-CSRFToken': "5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            'Referer': "https://cookifi.com/menu/240885/cookifi-value-non-veg/web/view",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "en-US,en;q=0.9",
            'Cookie': "DeviceId1801=d2bbbf0d-8ad5-4bf1-85f3-5d3fd3040cc4; _ga=GA1.2.536402851.1540906574; __tawkuuid=e::cookifi.com::w3U9YcDQgpAT19Ky5jUARCs36uX8sAcnn3NFj9oBaOLaGV9Hn9xXR/xRyctqVdXY::2; _gid=GA1.2.1493513947.1543231702; _fbp=fb.1.1543231702490.2145733689; csrftoken=5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR; sessionid=qdvolncv99selk7em4thslqn9rzs7q7k; TawkConnectionTime=0",
        }
        url = "https://cookifi.com/rest/menu/add_dish/"
        querystring = {"menu_id": "240885", "dish_id": item}
        response = requests.request("POST", url, headers=headers, params=querystring)
        print(response.text)
        url1 = "https://cookifi.com/rest/menu/menu_order_summary/240252/"
        response = requests.request("GET", url1, headers=headers)
        data = response.text
        decoded_string = json.loads(data)
        print(decoded_string["total_cost"])

    def delete_dish(self, item):
        headers = {
            'Host': "cookifi.com",
            'Connection': "keep-alive",
            'Content-Length': "0",
            'Accept': "application/json, text/plain, */*",
            'Origin': "https://cookifi.com",
            'X-CSRFToken': "5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            'Referer': "https://cookifi.com/menu/240885/cookifi-value-non-veg/web/view",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "en-US,en;q=0.9",
            'Cookie': "DeviceId1801=d2bbbf0d-8ad5-4bf1-85f3-5d3fd3040cc4; _ga=GA1.2.536402851.1540906574; __tawkuuid=e::cookifi.com::w3U9YcDQgpAT19Ky5jUARCs36uX8sAcnn3NFj9oBaOLaGV9Hn9xXR/xRyctqVdXY::2; _gid=GA1.2.1493513947.1543231702; _fbp=fb.1.1543231702490.2145733689; csrftoken=5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR; sessionid=qdvolncv99selk7em4thslqn9rzs7q7k; TawkConnectionTime=0",
        }
        url = "https://cookifi.com/rest/menu/delete_dish/"
        querystring = {"menu_id": "240885", "dish_id": item}
        requests.request("DELETE", url, headers=headers, params=querystring)
        print("Deleted " + item)

    def check(self, price):
        headers = {
            'Host': "cookifi.com",
            'Connection': "keep-alive",
            'Content-Length': "0",
            'Accept': "application/json, text/plain, */*",
            'Origin': "https://cookifi.com",
            'X-CSRFToken': "5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            'Referer': "https://cookifi.com/menu/240885/cookifi-value-non-veg/web/view",
            'Accept-Encoding': "gzip, deflate, br",
            'Accept-Language': "en-US,en;q=0.9",
            'Cookie': "DeviceId1801=d2bbbf0d-8ad5-4bf1-85f3-5d3fd3040cc4; _ga=GA1.2.536402851.1540906574; __tawkuuid=e::cookifi.com::w3U9YcDQgpAT19Ky5jUARCs36uX8sAcnn3NFj9oBaOLaGV9Hn9xXR/xRyctqVdXY::2; _gid=GA1.2.1493513947.1543231702; _fbp=fb.1.1543231702490.2145733689; csrftoken=5ey8NtcRr04QkZBHebEQzoT0cVpjRibS0WqEML54yUBFIBIAFOtiEfzfMWh1IadR; sessionid=qdvolncv99selk7em4thslqn9rzs7q7k; TawkConnectionTime=0",
        }
        url1 = "https://cookifi.com/rest/menu/menu_order_summary/240252/"
        response = requests.request("GET", url1, headers=headers)
        data = response.text
        decoded_string = json.loads(data)
        assert (decoded_string["total_cost"] == price), "price mismatch"

    def test_api_large_order(self):
        # add disk and check if price correct or not
        # starters
        self.add_dish("288")
        self.check("25700.00")
        self.add_dish("327")
        self.check("25700.00")
        self.add_dish("275")
        self.check("28100.00")
        # dal
        self.add_dish("43")
        self.check("28100.00")
        # gravy
        self.add_dish("12666")
        self.check("28100.00")
        self.add_dish("198")
        self.check("28100.00")
        # Rice
        self.add_dish("181")
        self.check("28100.00")
        self.add_dish("78")
        self.check("29300.00")
        # bread
        self.add_dish("12392")
        self.check("29300.00")
        self.add_dish("280")
        self.check("30500.00")
        # Desert
        self.add_dish("95")
        self.check("30500.00")
        self.add_dish("12670")
        self.check("31700.00")
        # live counters
        self.add_dish("260")
        self.check("35300.00")
        self.add_dish("12407")
        self.check("37700.00")
        # Welcome Drink
        self.add_dish("56")
        self.check("37700.00")

        # deleting the entries
        # Starter
        self.delete_dish("288")
        self.delete_dish("327")
        self.delete_dish("275")
        # dal
        self.delete_dish("43")
        # Gravy
        self.delete_dish("12666")
        self.delete_dish("198")
        # Rice
        self.delete_dish("181")
        self.delete_dish("78")
        # Bread
        self.delete_dish("12392")
        self.delete_dish("280")
        # Desert
        self.delete_dish("95")
        self.delete_dish("12670")
        # Live Counter
        self.delete_dish("260")
        self.delete_dish("12407")
        # Welcome Drink
        self.delete_dish("56")


if __name__ == '__main__':
    unittest.main()