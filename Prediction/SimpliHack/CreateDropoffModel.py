__author__ = 'basis'
#!/usr/bin/python

import sys
import getopt
import csv

thresh = 0.25
uppderCutoff = 0.7
lowerCutoff = 0.3

def createDropOffModel(base, user):
    for i in range(0, len(base[0])):
        if user[0][i] != '-1':
            base[0][i] = base[0][i]+float(user[0][i])
    return

dataPath = 'C:/Users/basis/Desktop/Data/'
dropoffDataPath = 'CloudData/DropoffData/'
coursePath = 'CloudData/AnnUserData/'
annUser = 'AnnUser'
dataExt = '.csv'

def main(argv):
   coursename = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print 'test.py -i <coursename>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         coursename = arg
   print 'Creating Dropoff Model for : ', coursename

   model = 0
   numUsers = 21;

   for i in range(1,numUsers):
       with open('{}{}{}/{}'.format(dataPath,coursePath,coursename,annUser) + '{0:04}'.format(i) + '{}'.format(dataExt), 'r') as f:
        reader = csv.reader(f)
        course_list = list(reader)
        if i == 1:
            model = course_list
            for j in range(0,len(model[0])):
                model[0][j] = float(0)
        createDropOffModel(model,course_list)

        print 'Processing : AnnUser {0:04}'.format(i)

   for i in range(0,len(model[0])):
       model[0][i] = model[0][i]/numUsers

   print '\n'
   print('Model Created')
   for i in range(0, len(model)):
       print model[i]

   with open('{}{}{}{}'.format(dataPath,dropoffDataPath,coursename,dataExt), 'w') as f:
       for i in range(0,len(model)):
           for j in range(0,len(model[i])):
               if j == len(model[i])-1:
                   f.write('{}\n'.format(model[i][j]))
               else:
                   f.write('{},'.format(model[i][j]))

if __name__ == "__main__":
   main(sys.argv[1:])
