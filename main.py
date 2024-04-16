import os

import fetcher

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    soup = fetcher.get_soup(os.getenv('TARGET_URL'))
    ulist = fetcher.get_ulist(soup, os.getenv('ELEMENT_ID'))
    count = fetcher.count_list_items(ulist)

    # if count > int(os.getenv('TOTAL_ITEMS')):
    # TODO trigger notification
