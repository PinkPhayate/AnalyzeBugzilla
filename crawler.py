import requests
import urllib2
from bs4 import BeautifulSoup
import lxml

COLUMNS = ['Status','Product','Component','Version','Hardware','Importance','Target_Milestone','Assigned_To','QA_Contact','URL','Whiteboard','Keywords','Depends_on','Blocks','Reported','Modified','CC_List']
def scrape_page(url, comment):
    # read page source code
    soup = BeautifulSoup(urllib2.urlopen(url), "lxml")
    # Extract status
    list = []
    for table in  soup.findAll(class_='bz_show_bug_column'):
        for td in table.findAll('td',''):
            list.append( " ".join(td.text.rsplit()) )

    # create dictionary
    dict = {}
    for (a, b) in zip(COLUMNS, list):
        dict[a] = b
    return dict

    if not comment :
        return list

    # Extract comment
    for comment in  soup.findAll(class_='bz_comment_text'):
            list.append( " ".join(comment.text.rsplit()) )
    return list


if __name__ == '__main__':
    url = "https://bugs.eclipse.org/bugs/show_bug.cgi?id=1789"
    res = scrape_page(url,True)

    print res
