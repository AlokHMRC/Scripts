#!/usr/bin/python
import os

repository = ["government-gateway-registration-frontend",
              "multi-factor-authentication-frontend",
              "reauthentication-frontend",
              "company-auth-frontend",
              "bas-gateway-frontend"]

englishArr = []
welshArr = []


def delete_repo(file_name):
    os.system("rm -rf %s" % file_name)  


def clone_and_switch(file_name):
    os.system("git clone git@github.com:hmrc/%s.git" % file_name)
    os.chdir(file_name)


def get_welsh_translation(file_name):
    welsh_translation = file_name.read().split("\n")
    for line in welsh_translation:
        if not line.startswith("#"):
            clear_translation = line.split("=")
            welshArr.append(clear_translation)
    return welshArr


def get_english_translation(file_name):
    eng_translation = file_name.read().split("\n")
    for line in eng_translation:
        if not line.startswith("#"):
            clear_translation = line.split("=")
            englishArr.append(clear_translation)
    return englishArr


def compare_length(welsh_array, english_array):
    if len(english_array) == len(welsh_array):
        return True
    else:
        return False

    
def compare_keys(arr_one, arr_two):
    for i in range(len(arr_one)):
        if arr_one[i][0] == arr_two[i][0]:
            return True
        else:
            print(arr_one[i][0] + "not the same as " + arr_two[i][0])


def compare_values(arr_one, arr_two):
    for i in range(len(arr_one)):
        if arr_one[i][1] != arr_two[i][1]:
            return True
        else:
            print(arr_one[i][1] + " SAME AS " + arr_two[i][1])


def compare(arr_one, arr_two):
    if compare_length(arr_one, arr_two):
        compare_key_and_value(arr_one, arr_two)
    else:
        print("-----Number of keys or Values dont match up-----")


def compare_key_and_value(arr_one, arr_two):
    try:
        compare_values(arr_one, arr_two)
        compare_keys(arr_one, arr_two)
        print("---Number of keys are the same on both files the values of each key are different.-----")
        print("Its safe to assume that each english key value has welsh translation")
    except IndexError:
        print("----------Missing or Extra key Values-----------")


def open_english_messages():
    try:
        opened_file = open("conf/messages", "r")
        return opened_file
    except IOError:
        print("ERROR: Couldn't find messages file")


def open_welsh_messages():
    try:
        opened_file = open("conf/messages.cy", "r")
        return opened_file
    except IOError:
        print("ERROR: Couldn't find messages.cy file")


for repos in repository:
    delete_repo(repos)
    clone_and_switch(repos)
    english = open_english_messages()
    welsh = open_welsh_messages()
    print("Checking %s" % repos + "\n")
    compare(get_english_translation(english), get_welsh_translation(welsh))
    print("----Check complete---- \n")
    englishArr.clear()
    welshArr.clear()
    delete_repo(repos)
