import os

import dotenv
import requests
from bs4 import BeautifulSoup


class PageParser:

    def __init__(self):
        self.env_file = dotenv.find_dotenv()

        dotenv.load_dotenv(self.env_file)

        self.url = os.environ["TARGET_URL"]
        self.element_id = os.environ["ELEMENT_ID"]

    def get_soup(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Could not get a valid response from the server.")
        return BeautifulSoup(response.content, 'html.parser')

    def get_child_element(self, child_element_name):
        soup = self.get_soup()
        return soup.find(id=self.element_id).find_next(child_element_name)
