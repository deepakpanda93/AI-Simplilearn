#!/usr/bin/python

import sys
import getopt
import csv

def predictDropOffProb(base, user):
    prob = 0
    count = 0
    for i in range(len(base)-1, -1, -1):
        print '.....'
        if user[i] != -1:
            count = count + 1
            if float(user[i])-float(base[i]) < 0.25 :
                prob = prob + 1

    prob = prob/float(count)
    return prob

dataPath = 'C:/Users/basis/Desktop/Data/'
cloudData = 'CloudData/'
acadData = 'AcadPoolData/'
compData = 'CompanyPoolData/'
dataExt = '.csv'

def main(argv):
   username = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print 'test.py -i <username>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         username = arg
   print 'User: ', username
   print ''

   with open('{}{}/profile{}'.format(dataPath,username,dataExt), 'r') as f:
    reader = csv.reader(f)
    profile_params = list(reader)

    print 'Predicting content for user: {}'.format(username)
    print ''

    with open('{}{}/courses{}'.format(dataPath,username,dataExt)) as f:
        reader = csv.reader(f)
        courseList = list(reader)

    with open('{}{}{}{}{}'.format(dataPath,cloudData,acadData,profile_params[0][2],dataExt)) as f:
        reader = csv.reader(f)
        acadCircleCourses = list(reader)

    with open('{}{}{}{}{}'.format(dataPath,cloudData,compData,profile_params[0][3],dataExt)) as f:
        reader = csv.reader(f)
        compCircleCourses = list(reader)

    print 'Enrolled Courses: '
    for i in range(0,len(courseList[1])):
           print '{}'.format(courseList[1][i])
    print ''

    print 'Popular courses in Acadmeic Circles'
    for i in range(0, len(acadCircleCourses[0])):
        print '{}'.format(acadCircleCourses[0][i])
    print ''


    print 'Popular courses with your Colleagues'
    for i in range(0, len(compCircleCourses[0])):
        print '{}'.format(compCircleCourses[0][i])
    print ''



if __name__ == "__main__":
   main(sys.argv[1:])