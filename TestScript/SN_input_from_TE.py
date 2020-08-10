import requests
import random
import time
import pymysql


class MACreater:
    def __init__(self):
        self.url = r"http://127.0.0.1:8000/location/info"
        self.db = pymysql.connect(
            host="127.0.0.1",
            user="guest_q",
            password="123",
            db="EWS"
        )

    def query_data(self):
        cur = self.db.cursor()
        sql = r"SELECT SN,modelName,MAC FROM EWS"
        cur.execute(sql)
        result = cur.fetchone()
        return result

    def create_location(self):
        area_list = ["FA", "DT"]
        row_temp = chr(random.randint(65, 69)) + str(random.randint(1, 9))
        result = {
            "line": random.randint(1, 6),
            "area": random.choice(area_list),
            "row": row_temp,
            "number": random.randint(1, 42)
        }
        return result

    def create_data(self):
        machine_info = self.query_data()
        location_info = self.create_location()
        result = {
            "Flag": "1",
            "SN": machine_info[0],
            "Model": machine_info[1],
            "MAC": machine_info[2],
            "line": location_info["line"],
            "area": location_info["area"],
            "row": location_info["row"],
            "number": location_info["number"]
        }
        return result

    def send_data(self, data):
        resp = requests.post(url=self.url, data=data)
        print(resp.text)

    def run(self):
        data = self.create_data()
        self.send_data(data)


if __name__ == '__main__':
    mc = MACreater()
    mc.run()
