import requests
from bs4 import BeautifulSoup
from bs4 import PageElement


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Could not get a valid response from the server.")
    return BeautifulSoup(response.content, 'html.parser')


def get_ulist(soup: BeautifulSoup, element_id: str) -> PageElement:
    return soup.find(id=element_id).find_next("ul")


def count_list_items(element: PageElement) -> int:
    items = element.find_all_next(name="li")
    return len(items)
