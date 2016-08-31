import re
from urllib.request import urlopen

#define page url
url = 'http://www.pythonchallenge.com/pc/def/'
sli = 'linkedlist.php?nothing='
random = '12345'

#define pattern
pattern = re.compile('and the next nothing is (\d+)')


while random:
#open page
    page = urlopen(url+sli+random)

#read page content
    pageContent = page.read()
    pageContent = pageContent.decode('UTF-8')
    print(pageContent)

#look for numeric string in page
    
    try: 
        random = re.search(pattern, pageContent).group(1)
        #print(random)
    except AttributeError:
        if ('html'in pageContent) or ('php' in pageContent):
            print('we found the url!')
            print(url+pageContent)
            break
        else:
            random = int(random)    #make it int to divide by 2
            random = int(random/2)       #divide by 2
            random = str(random)    #make it string back to be able to add it to the url
            print(random)
