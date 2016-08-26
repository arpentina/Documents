orig = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
targ = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't',' u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', ' ', '.', '!', '?']


def cesar(text):
    cypher = []
    for i in range(len(text)):
        #print (text[i])
        if text[i] in orig:
            #print (targ[i])
            cypher.append(targ[i])
    return (''.join(cypher))   
                      
def look(text):
    result = []
    for i in range(len(text)):
        if text[i] in orig:
            result.append(text[i])
    return(''.join(result))

def main():
    #read the text from a file
    f = open('test.txt', 'r+')
    #cy = open('criptat.txt', 'w')
    text = f.read()
    print(look(text))
    print("End!")

main()
            
