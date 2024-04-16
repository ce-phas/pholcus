import sys

import fetcher


if __name__ == '__main__':
    soup = fetcher.get_soup(sys.argv[1])
    ulist = fetcher.get_ulist(soup, sys.argv[2])
    # TODO trigger notification if len(ulist) > os.getenv('TOTAL_ITEMS')
