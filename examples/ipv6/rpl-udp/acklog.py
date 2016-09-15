import re

nodes = {}
f = open('COOJA.testlog','r')
atre = re.compile('(.*) (.*) #A (.*)')
prr = re.compile('r=(.*)/(.*),c')
while True:
    text = f.readline()
    if not text: break
    ma =re.search(atre, text) 
    if ma:
        #print ma.group(2), ma.group(3)
        s = re.search(prr, ma.group(3))
        #print float(s.group(1)) / float(s.group(2))
        nodes[ma.group(2)] = float(s.group(1)) / float(s.group(2))

ctr = 0
tot = 0
for node in nodes:
    print node,nodes[node]
    tot = tot + nodes[node]
    ctr = ctr + 1

print "Total PRR:", tot / ctr

