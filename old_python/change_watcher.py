class ChangeWatcher:
    def count_items(self, parent_el, child_name):
        items = parent_el.find_all_next(name=child_name)
        return len(items)
