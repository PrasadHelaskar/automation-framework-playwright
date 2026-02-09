import json
from utils.logger import Logger

log=Logger().get_logger(__name__)

class APIRecorder():
    def __init__(self,page):
        self.page=page
        self.call=[]

    def _capture(self,response):
        if "saucedemo" in response.url:
            self.call.append({
                "url": response.url,
                "status": response.status,
                # "body": self.get_response_body(response)
            })

    def start_recorder(self):
        self.page.on("response",self._capture)

    def stop_recorder(self):
        self.page.on("response",self._capture)

    def get_records(self):
        return self.call

    def get_response_body(self,response):
        try:
            return response.json()
        except ValueError:
            return response.text()