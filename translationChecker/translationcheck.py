#!/usr/bin/python
import os

repository = ["government-gateway-registration-frontend","multi-factor-authentication-frontend","reauthentication-frontend","company-auth-frontend","bas-gateway-frontend"]

englishArr = []
welshArr = []

def deleteRepo(fileName):
	os.system("rm -rf %s" % fileName)	

def cloneAndSwitch(fileName):
	os.system("git clone git@github.com:hmrc/%s.git" % fileName)
	os.chdir(fileName)


def getWelshTranslation(fileName):
  welshTranslation = fileName.read().split("\n")
  for line in welshTranslation:
    if not line.startswith("#"):    
        clearTranslation = line.split("=")
        welshArr.append(clearTranslation)
  return welshArr

def getEnglishTranslation(fileName):
  engTranslation = fileName.read().split("\n")
  for line in engTranslation:
    if not line.startswith("#"):
        clearTranslation = line.split("=")
        englishArr.append(clearTranslation)
  return englishArr


def compare_length(welshArray, englishArray):
  if(len(englishArray) == len(welshArray)):
    return True
  else:
    return False

    
def compare_keys(arrOne, arrTwo): 
  for i in range (len(arrOne)):
    if(arrOne[i][0] == arrTwo[i][0]):
      return True
    else:
      print arrOne[i][0] + "not the same as " + arrTwo[i][0]
      


def compare_values(arrOne, arrTwo):
  for i in range (len(arrOne)):
    if(arrOne[i][1] != arrTwo[i][1]):
      return True
    else:
      print arrOne[i][1] + " SAME AS " + arrTwo[i][1]
      

def compare(arrOne, arrTwo):
  if(compare_length(arrOne,arrTwo)):
    compare_key_and_value(arrOne,arrTwo)
  else:
    print("-----Number of keys or Values dont match up-----")


def compare_key_and_value(arrOne, arrTwo):
  try:
    compare_values(arrOne,arrTwo)
    compare_keys(arrOne,arrTwo)
    print "---Number of Keys and Values are the same on both files.-----"
    print"Its safe to assume that each english key value has welsh translation"
  except IndexError:
    print "----------Missing or Extra key Values-----------"


def openEnglishMessages():
    try:
        openedFile = open("conf/messages", "r")
	return openedFile
    except IOError:
        print("ERROR: Couldnt find messages file")

def openWelshMessages():
    try:
        openedFile = open("conf/messages.cy", "r")
	return openedFile
    except IOError:
	print("ERROR: Couldnt find messages.cy file")


for repos in repository:
	deleteRepo(repos)
        cloneAndSwitch(repos)
	english = openEnglishMessages()
	welsh = openWelshMessages()
	print("Checking %s" % repos + "\n")
        compare(getEnglishTranslation(english),getWelshTranslation(welsh))
	print("----Check complete---- \n")
	welshArr = []
	englishArr = []
	deleteRepo(repos)
