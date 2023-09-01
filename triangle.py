"""
for i in range(1):
    print("*", end=" ")
print()

for i in range(2):
    print("*", end=" ")
print()


for i in range(3):
    print("*", end=" ")
print()


for i in range(4):
    print("*", end=" ")
print()
"""

for k in range(4):
    for i in range(k+1):
        print("*", end=" ")
    print()
    
for i in range(5):
    print("*", end=" ")
print()
    
for k in range(5,1,-1):
    for i in range(k-1):
        print("*", end=" ")
    print()