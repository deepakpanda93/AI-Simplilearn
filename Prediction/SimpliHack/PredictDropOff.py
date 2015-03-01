#!/usr/bin/python

import sys
import getopt
import csv

thresh = 0.25
uppderCutoff = 0.7
lowerCutoff = 0.3

def predictDropOffProb(base, user):
    prob = 0
    count = 0
    for i in range(0,len(base)):
        print '.....'
        if user[i] != '-1':
            count = count + 1
            if (float(user[i])-float(base[i])) < float(thresh):
                prob = prob + 1

    prob = prob/float(count)
    return prob

dataPath = 'C:/Users/basis/Desktop/Data/'
dropoffDataPath = 'CloudData/DropoffData/'
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

   with open('{}{}/courses{}'.format(dataPath,username,dataExt), 'r') as f:
    reader = csv.reader(f)
    course_list = list(reader)

    print 'Running Drop Off Analysis for Course: {}'.format(course_list[0][0])

    with open('{}{}{}{}'.format(dataPath,dropoffDataPath,course_list[0][0],dataExt)) as f:
        reader = csv.reader(f)
        baseCourseBehaviour = list(reader)

    with open('{}{}/{}{}'.format(dataPath,username,course_list[0][0],dataExt)) as f:
        reader = csv.reader(f)
        userCourseBehaviour = list(reader)

    prob = predictDropOffProb(baseCourseBehaviour[0], userCourseBehaviour[0])
    print '\n'
    print 'DropOff probability for {} =   {}'.format(course_list[0][0], prob)
    print '\n'
    if prob > 0.7:
        print '{} is a Possible Dropoff in {} course'.format(username, course_list[0][0])
    elif prob < 0.3:
       print '{} is a Hihgly Engaged student in {} course'.format(username, course_list[0][0])
    else:
        print 'Mediocre User'

if __name__ == "__main__":
   main(sys.argv[1:])