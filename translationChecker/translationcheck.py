#!/usr/bin/python
import os

repositories = ["government-gateway-registration-frontend",
              "multi-factor-authentication-frontend",
              "reauthentication-frontend",
              "company-auth-frontend",
              "bas-gateway-frontend"]

englishArr = {}
welshArr = {}
base_dir = os.getcwd()


def delete_repo(file_name):
    os.chdir(base_dir)
    os.system("rm -rf %s" % file_name)


def clone_and_switch(file_name):
    print(base_dir)
    os.chdir(base_dir)
    os.system("git clone git@github.com:hmrc/%s.git" % file_name)
    os.chdir(file_name)


def get_translation(file_name, array):
    for line in file_name:
        if not line.startswith("#") and line not in ['\n', '\r\n']:
            key_value_pair = line.split("=")
            array[key_value_pair[0].rstrip(' ')] = key_value_pair[1].lstrip(' ')
    return array


def compare_length(welsh_array, english_array):
    print("Number of Keys In English File = " + str(len(english_array)))
    print("Number of Keys In Welsh File = " + str(len(welsh_array)))

    if len(english_array) == len(welsh_array):
        return True
    else:
        return False


def compare_keys(arr_one, arr_two):
    for key in arr_one:
        if key in arr_two:
            return True
        else:
            print(arr_one[key] + "not in other file")


def compare_values(arr_one, arr_two):
    for key in arr_one:
        if arr_one[key] != arr_two[key]:
            return True
        else:
            print(arr_one[key] + " SAME AS " + arr_two[key])


def compare(arr_one, arr_two):
    if compare_length(arr_one, arr_two):
        compare_key_and_value(arr_one, arr_two)
    else:
        print("ERROR: Mismatch in the number of keys in each file")


def compare_key_and_value(arr_one, arr_two):
    try:
        compare_keys(arr_one, arr_two)
        compare_values(arr_one, arr_two)
        print("Number of keys are the same on both files the values of each key are different.")
        print("Its safe to assume that each english key value has welsh translation")
    except IndexError:
        print("ERROR: Missing or Extra key Values")


def open_english_messages():
    try:
        opened_file = open("conf/messages", "r")
        return opened_file
    except IOError:
        print("ERROR: Couldn't find messages file")
        return None


def open_welsh_messages():
    try:
        opened_file = open("conf/messages.cy", "r")
        return opened_file
    except IOError:
        print("ERROR: Couldn't find messages.cy file")
        return None


for repo in repositories:
    print("Check starting for " + repo)
    delete_repo(repo)
    clone_and_switch(repo)
    english = open_english_messages()
    welsh = open_welsh_messages()

    if english is not None and welsh is not None:
        print("Comparing key and values for " + repo)
        compare(get_translation(english, englishArr), get_translation(welsh, welshArr))
    else:
        if english is None:
            print("English file was not found")
        if welsh is None:
            print("Welsh file was not found")

    print("Check complete for " + repo)

    englishArr.clear()
    welshArr.clear()
    delete_repo(repo)
