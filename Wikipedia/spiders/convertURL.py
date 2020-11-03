i = 0
d = open("wikiurl.txt").readlines()
for line in d:
    d[i] = 'https://en.wikipedia.org/wiki/' + d[i]
    i += 1
print(d)