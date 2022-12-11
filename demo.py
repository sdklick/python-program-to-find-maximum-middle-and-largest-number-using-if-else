#python-program-to-find-maximum-middle-and-largest-number using if else
n1 = 70
n2 = 100
n3 = 80

if n1 > n2 and n1 > n3:
    print(n1, 'bigger')
elif n2 > n1 and n2 > n3:
    print(n2, 'bigger')
else:
    print(n3, 'bigger')

if (n2 < n1 and n3 > n1) or (n3 < n1 and n2 > n1):
    print(n1, 'middle')
elif (n2 > n1 and n3 > n2) or (n1 > n2 and n3 < n2):
    print(n2, 'middle')
elif (n3 > n2 and n3 < n1) or (n3 < n2 and n3 > n1):
    print(n3, 'middle')

if n1 < n2 and n1 < n3:
    print(n1, 'smaller')
elif n2 < n1 and n2 < n3:
    print(n2, 'smaller')
else:
    print(n3, 'smaller')
