import re


value = "Developers are developers!"


mySearch = re.search("(lope.*)(deve.*)",value,re.I)

if mySearch:
    print("Result for search (group 1): ", mySearch.group(1))
    print("Result for search (group 2): ", mySearch.group(2))

print()


myMatch = re.match("(devolopers.*)", value, re.I)

if myMatch:
    print("Result: ", myMatch.group(1))