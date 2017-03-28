import json
import os

from pro2.settings import BASE_DIR


class Data_model(object):
    __AUTHORS = json.loads(open(os.path.join(BASE_DIR, 'data/new_authors.json'), 'r').read())
    __DOMAINS = json.loads(open(os.path.join(BASE_DIR, 'data/new_domains.json'), 'r').read())
    __CO_AUTHORS = json.loads(open(os.path.join(BASE_DIR, 'data/coauthors.json'), 'r').read())

    def __str__(self):
        return repr(self)

    @staticmethod
    def get_authors_with_domain(domain):
        authors_info_list = []
        if domain in Data_model.__DOMAINS:
            authors_index_list = json.loads(Data_model.__DOMAINS[domain])
            for index in authors_index_list:
                author_dict = {"index": index, "info": json.loads(Data_model.__AUTHORS[str(index)])}
                authors_info_list.append(author_dict)
        return authors_info_list

    @staticmethod
    def get_coauthors(author_index):
        authors_info_list = []
        if author_index in Data_model.__CO_AUTHORS:
            coauthors_list = json.loads(Data_model.__CO_AUTHORS[author_index])
            for coauthor in coauthors_list:
                index = coauthor["index"]
                times = coauthor["times"]
                author_dict = {"index": index, "times": times, "info": json.loads(Data_model.__AUTHORS[str(index)])}
                authors_info_list.append(author_dict)
        return authors_info_list


def __getattr__(self, name):
    return getattr(self.instance, name)
