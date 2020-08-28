import requests
import random
import time


class SNCreater:
    def __init__(self):
        self.url = r"http://127.0.0.1:8000/location/info"

    def create_SN(self):
        letter_list = [chr(item) for item in range(65, 91)]
        num_list = [str(i) for i in range(10)]
        temp = letter_list + num_list
        result = "".join(random.choices(temp, k=8))
        return result

    def create_model(self):
        temp = ["AAA1", "BBB2"]
        return random.choice(temp)

    def create_MAC(self):
        temp = ["ec8eb570c316", "ec8eb570c317"]
        return random.choice(temp).upper()

    def create_data(self):
        sn = self.create_SN()
        model = self.create_model()
        mac = self.create_MAC()
        result = {
            "Flag": "0",
            "SN": sn,
            "Model": model,
            "MAC": mac,
        }
        return result

    def send_data(self, data):
        resp = requests.post(url=self.url, data=data)
        print(resp.text)

    def run(self):
        while True:
            time.sleep(5)
            data = self.create_data()
            resp = self.send_data(data)


if __name__ == '__main__':
    sc = SNCreater()
    sc.run()

