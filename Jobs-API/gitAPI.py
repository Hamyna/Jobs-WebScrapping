#This script gets job posting from github
# IMPORTS
#Make Python understand how to read things on the Internet
import urllib2
#Make Python understand the stuff in a page on the Internet is JSON
import json
# Make Python understand csv
import csv
# Make Python know how to take a break so we don't hammer API and exceed rate limit
from time import sleep

def get_jobposting():
    # tell computer where to put CSV
    outfile_path='/home/hamyna/Documents/Git/BullFrogIT/Jobs-WebScrapping/Results/Github/jobPosting_gitHub-.csv'
    # open it up, the w means we will write to it
    writer = csv.writer(open(outfile_path, 'w'))
    #create a list with headings for our columns
    headers = ['id', 'title', 'created_at', 'location', 'type', 'description', 'company', 'how_to_apply', 'url']
    location = ['Atlanta', 'boston', 'bristol', 'brooklyn', 'CA', 'chicago', 'DC', 'LA', 'london', 'MA', 'Maryland', 'NC', 'NY', 'TORONTO', 'WATERLOO', 'Washington']
    #write the row of headings to our CSV file
    writer.writerow(headers)
    i=1 #iteration count
    #loop through pages of JSON returned, 5 (ce), note that iteration can be increased or decreased
    while i<6:
        #print out what number loop we are on, which will make it easier to track down problems when they appear
        print "Currently downloading job postings from github"
        print i
        #create the URL for the json data, location is north america and page number is iteration i
        #and set the number of tweets per JSON file to the max of 5, so we have to do as little looping as possible
        url = urllib2.Request('https://jobs.github.com/positions.json?description&location=TORONTO&page=' + str(i))
        #use the JSON library to turn this file into a Pythonic data structure
        parsed_json = json.load(urllib2.urlopen(url))

        print parsed_json

        #run through each item in results, and jump to an item in that dictionary, ex: the text of the tweet
        for posting in parsed_json:
         #initialize the row
         row = []
         #add every 'cell' to the row list, identifying the item just like an index in a list
         row.append(str(posting['id'].encode('utf-8')))
         row.append(str(posting['title'].encode('utf-8')))
         row.append(str(posting['created_at'].encode('utf-8')))
         row.append(str(posting['location'].encode('utf-8')))
         row.append(str(posting['type'].encode('utf-8')))
         row.append(str(posting['description'].encode('utf-8')))
         row.append(str(posting['company'].encode('utf-8')))
         row.append(str(posting['how_to_apply'].encode('utf-8')))
         row.append(str(posting['url'].encode('utf-8')))
         #once you have all the cells in there, write the row to your csv
         writer.writerow(row)
        #increment our loop counter, now we're on the next time through the loop
        i = i +1
        #tell Python to rest for 5 secs, so we don't exceed our rate limit
        sleep(5)

if __name__ == "__main__":
    get_jobposting()