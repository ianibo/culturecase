# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import time
import requests
import lxml.html


# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

html = scraperwiki.scrape("http://www.culturecase.org/contents/")

root = lxml.html.fromstring(html)

for el in root.cssselect("div.post-content p a"):
    print el.text
    content_url = el.attrib['href']
    print "Scrape..."+content_url
    contentpage = scraperwiki.scrape(content_url);
    content_root = lxml.html.fromstring(contentpage);
    for metadata_el in content_root.cssselect("table.research-meta tr"):
      print "element"
      print metadata_el.cssselect("th")[0].text
      print metadata_el.cssselect("td")[0].text


# Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

# for i in range(1, 6):
#     print "%i..." % i
#     time.sleep(1)
