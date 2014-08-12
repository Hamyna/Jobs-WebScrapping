# import library
import urllib2
import json
import csv
from time import sleep
from lxml import etree
from xml.etree import ElementTree as ET
from optparse import OptionParser
from xml.dom.minidom import parseString

def get_jobPosting():
    headers = ['Company', 'CompanyDID', 'CompanyDetailsURL', 'DID', 'OnetCode', 'ONetFriendlyTitle',
               'DescriptionTeaser', 'Distance', 'EmploymentType', 'EducationRequired',
               'ExperienceRequired', 'JobDetailsURL', 'JobServiceURL', 'Location', 'LocationLatitude',
               'LocationLongitude', 'PostedTime', 'Pay', 'SimilarJobsURL', 'JobTitle', 'ApplyRequirement',
               'Skills']
    # create a list with headings for our columns
    outfile_path = '/home/hamyna/Documents/Git/BullFrogIT/Jobs-WebScrapping/Results/CareerBuilder/jobpostings-careerBuild.csv'
    # open it up, the w means we will write to it
    writer = csv.writer(open(outfile_path, 'wb'))
    writer.writerow(headers)
    #'developer', 'Programmer', 'IT', 'Technology', 'Application', 'Computer', 'Systems', 'tester', 'front-end', 'programming', 'software-test', 'Software', 'Data', 'hardware', 'mysql', 'engineer'
    #'object-oriented-design', 'architect', 'object-oriented-design', 'architect', 'database', 'web', 'technician', 'analyst', 'mobile'
    keywords = ['Java', '.NET', 'Python', 'CSS', 'mysql', 'network', 'html', 'security', 'iOS', 'developer', 'Programmer', 'IT', 'Technology',
                'Application', 'Computer', 'Systems', 'tester', 'front-end', 'programming', 'software-test', 'Software', 'Data', 'hardware', 'mysql',
                'engineer', 'object-oriented-design', 'architect', 'object-oriented-design', 'architect', 'database', 'web', 'technician', 'analyst', 'mobile']
    #loop through the keyword and call the API then download the file:
    for keyword in keywords:
        print 'Downloading job post with keyword ' + keyword
        pg = 1
        while pg < 3:
            print "Downloading page number" + str(pg)
            #download data from API call to file.
            file = urllib2.urlopen(
                'http://api.careerbuilder.com/v1/jobsearch?DeveloperKey=WDHL7MB628RRNH2V6WJQ&Keywords=' + keyword + '&pg=' + str(
                    pg))
            #convert data in file to string:
            data = file.read()
            #close file because we don't need it anymore:
            file.close()
            i = 1
            while i <= 24:
                row = []
                print 'downloading jop post number ' + str(i)
                for column in headers:
                    try:
                        print 'downloading row ' + column
                        dom = parseString(data)
                        row.append(str(
                            dom.getElementsByTagName(column)[i].toxml().replace(column, '').replace(
                                column, '')))
                    except UnicodeEncodeError as detail:
                        print str(
                            Exception) + "occured at row " + column + "with the keyword " + keyword + "page number " + str(pg)
                        print detail
                writer.writerow(row)
                i = i + 1
            pg = pg + 1
            sleep(5)


if __name__ == "__main__":
    get_jobPosting()