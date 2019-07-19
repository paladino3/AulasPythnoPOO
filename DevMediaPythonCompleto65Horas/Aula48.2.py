"""
Buscas e substituição de strings
"""

string1 = "Wesley Rolim Simoes is a excellent developer and will be the one the most want in the companys around world"

print(' "developer" occurs %d times in \n\t%s' % (string1.count("developer"), string1))

string2 = "My dog is angry "
print('"%s"contains "dog" starting at index %d' % (string2, string2.find("dog")))


try:
    print(' "angry" index is ',string2.index("angry"))
except ValueError:
    print(' "angry" does occur in "%s" ' % string2)

if string2.startswith("My"):
    print(' "%s" começa com "my" '%string2)
if string2.endswith("My"):
    print("não termina com 'my' ")
print()

print('Index from end of "developer" in "%s" is %d' % (string1,string1.rfind("devoloper")))
print()

string3= "Never say never"
print("Original: ",string3)
print('Replace "never" with "forever" ',string3.replace("Never","forever"))
print('Replaced 1 maximum: ',string3.replace("Never","forever" ,1))

