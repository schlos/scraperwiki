###############################################################################
# START HERE: Tutorial 1: Getting used to the ScraperWiki editing interface.
# Based on tutorial 1
###############################################################################

##
#import scraperwiki
#html = scraperwiki.scrape('http://data.gov')
#print html
##

import scraperwiki
import csv

url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'

data = scraperwiki.scrape(url)
data = data.splitlines()
#reader = csv.DictReader(data)

csv_reader = csv.DictReader(data, delimiter=';')

for record in csv_reader:
    #record['Name'] = record['Name'].decode("cp1252")
    print record 
    #for scraperwiki only:
    scraperwiki.sqlite.save(['OIB'], record) 
