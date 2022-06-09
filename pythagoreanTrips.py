# Pythagorean Triples

#
num = 200
for a in range( 2, num ) :
    for b in range( 2, num ) :
        for c in range( 2, num) :
            if a * a + b * b == c * c :
                print (a, b, c)
