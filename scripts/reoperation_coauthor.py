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
    coauthors = {}
    line_No = 0
    length = len(content_list)
    print(length)
    while line_No < length:
        if line_No % 100000 == 0:
            print(line_No)
        line = content_list[line_No][1:]
        colaboration_info = line.split("\t")
        author_A = colaboration_info[0]
        author_B = colaboration_info[1]
        if author_A == author_B:
            print("error")
            continue
        times = colaboration_info[2]
        if author_A not in coauthors:
            coauthors[author_A] = [{'index': author_B, 'times': times}]
        else:
            co_list = coauthors[author_A]
            No = 0
            while No < len(co_list):
                if co_list[No]["index"] == author_B:
                    co_list[No]["times"] += times
                    break
                No += 1
            if No == len(co_list):
                co_list.append({'index': author_B, 'times': times})
            while No > 0 and co_list[No]["times"] > co_list[No - 1]["times"]:
                co_list[No], co_list[No - 1] = co_list[No - 1], co_list[No]
                No -= 1

        if author_B not in coauthors:
            coauthors[author_B] = [{'index': author_A, 'times': times}]
        else:
            co_list = coauthors[author_B]
            No = 0
            while No < len(co_list):
                if co_list[No]["index"] == author_A:
                    co_list[No]["times"] += times
                    break
                No += 1
            if No == len(co_list):
                co_list.append({'index': author_A, 'times': times})
            while No > 0 and co_list[No]["times"] > co_list[No - 1]["times"]:
                co_list[No], co_list[No - 1] = co_list[No - 1], co_list[No]
                No -= 1
        line_No += 1
    new_coauthors = {}
    for author_index, coauthor_info in coauthors.items():
        new_coauthors[author_index] = json.dumps(coauthor_info)

    return new_coauthors


parser = argparse.ArgumentParser()
parser.add_argument('author_file', type=str)
# parser.add_argument('co_file', type=str)
args = parser.parse_args()
author_file = args.author_file
content_list = reader(author_file)
coauthors = operate_content(content_list)
with open('./coauthors.json', 'w') as file_handle:
    file_handle.write(json.dumps(coauthors))

