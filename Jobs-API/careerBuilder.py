#This script gets job posting from github
import urllib2
import json
import csv
from time import sleep
from lxml import etree
from xml.etree import ElementTree as ET


def get_jobposting():
    # tell computer where to put CSV
    outfile_path='/home/hamyna/Documents/Git/BullFrogIT/Jobs-WebsScrapping/Results/Github/jobPosting_careerBuilder-IT.csv'
    # open it up, the w means we will write to it
    writer = csv.writer(open(outfile_path, 'wb'))
    #create a list with headings for our columns
    headers = ['Company', 'CompanyDetailsURL', 'CompanyDID', 'DescriptionTeaser', 'EmploymentType', 'EducationRequired', 'ExperienceRequired', 'Location', 'JobTitle', 'CanBulkApply', 'Skills']
    url = urllib2.Request('http://api.careerbuilder.com/v1/jobsearch?DeveloperKey=WDHL7MB628RRNH2V6WJQ&Keywords=IT')
    #it,technology,developer,software, programmer.
    root = ET.parse(urllib2.urlopen(url)).getroot()
    print root
    #run through each item in results, and jump to an item in that dictionary, ex: the text of the tweet
    items = root.findall('Results/JobSearchResult')
    for item in items:
         row = []
         row.append(str(item['Company'].encode('utf-8')))
         row.append(str(item['CompanyDetailsURL'].encode('utf-8')))
         row.append(str(item['CompanyDID'].encode('utf-8')))

if __name__ == "__main__":
    get_jobposting()