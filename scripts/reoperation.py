import argparse
import json
import re

def reader(author_file):
    file_handle = open(author_file, 'r')
    content_list = []
    No = -1
    while True:
        No += 1
        if No % 1000000 == 0:
            print(No)
        line = file_handle.readline()
        if line == "":
            break
        if line[0] == "#":
            content_list.append(line[:-1])
        elif line == "\n":
            continue
        else:
            print("------------------")
            print(line)
            content_list[len(content_list) - 1] += line[:-1]
    file_handle.close()
    return content_list





def operate_content(content_list):
    domains_dict = {}
    authors = {}
    No = -1
    length = len(content_list)
    print(length)
    while No < length:
        No += 1
        if No >= length:
            break
        author_index_line = content_list[No]
        # while author_index_line == '\n':
        #     continue
        No += 1
        author_name_line = content_list[No]
        No += 1
        author_place_line = content_list[No]
        No += 1
        pc_line = content_list[No]
        No += 1
        cn_line = content_list[No]
        No += 1
        hi_line = content_list[No]
        No += 1
        pi_line = content_list[No]
        No += 1
        upi_line = content_list[No]
        No += 1
        domains_line = content_list[No]
        try:
            author_index = int(author_index_line[7:])
            if author_index % 10000 == 0:
                print(author_index)
            author_name = author_name_line[3:]
            author_place = author_place_line[3:]
            pc = int(pc_line[4:])
            cn = int(cn_line[4:])
            hi = int(hi_line[4:])
            pi = float(pi_line[4:])
            upi = float(upi_line[5:])
            domains_str = domains_line[3:]
            domains = re.split(";", domains_str)
        except Exception as e:
            print(e)
            print(author_index_line)
            print(No)
            break
        authors[author_index] = {'name': author_name, 'place': author_place, 'pc': pc, 'cn': cn, 'hi': hi, 'pi': pi,
                                 'upi': upi}
        for domain in domains:
            if domain == "":
                continue
            if domain not in domains_dict:
                domains_dict[domain] = [author_index]
            else:
                author_list = domains_dict[domain]
                author_list.append(author_index)
                j = len(author_list) - 2
                while j >= 0 and authors[author_list[j]]['hi'] < authors[author_list[j + 1]]['hi']:
                    author_list[j], author_list[j + 1] = author_list[j + 1], author_list[j]
                    j -= 1
    return authors, domains_dict


parser = argparse.ArgumentParser()
parser.add_argument('author_file', type=str)
# parser.add_argument('co_file', type=str)
args = parser.parse_args()
author_file = args.author_file
content_list = reader(author_file)
authors, domains = operate_content(content_list)
with open('./authors.json', 'w') as file_handle:
    file_handle.write(json.dumps(authors))
with open('./domains.json', 'w') as file_handle:
    file_handle.write(json.dumps(domains))
