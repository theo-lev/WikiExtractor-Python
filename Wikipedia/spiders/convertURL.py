i = 0
d = open("Wikipedia/spiders/wikiurl.txt").readlines()
for line in d:
    d[i] = 'https://en.wikipedia.org/wiki/' + d[i]
    d[i] = d[i].rstrip("\n")
    i += 1
print(d)
