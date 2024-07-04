import os

import dotenv

from page_parser import PageParser
from change_watcher import ChangeWatcher

if __name__ == '__main__':
    parser = PageParser()
    cw = ChangeWatcher()
    element = parser.get_child_element("ul")
    count = cw.count_items(element, "li")

    if count > int(os.environ["TOTAL_ITEMS"]):
        print(count)
        # dotenv.set_key(env_file, "TOTAL_ITEMS", str(count))
