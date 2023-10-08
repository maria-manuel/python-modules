# REMINDER: Only do one challenge at a time! Save and test after every one.

print('ready for modules')

print('Challenge 1 -------------')
# Challenge 1:
# 1. Uncomment and examine the following function code.
# 2. Modify it so that it prints the "lyrics" variable from the library module

#import library
#print()

import library
print(library.lyrics)

print('Challenge 2 -------------')
# Challenge 2:
# 1. Import the library.py file
# 2. Invoke the greeter function from library.py.
# Extra: Write an "from import" style statement to import the greeter directly.

import library
library.greeter(name='Keanu')

print('Challenge 3 -------------')
# Challenge 3:
# Time to get practice making your own module.
# 1. Create a new file called mymod.py
# 2. In mymod: Add a print statement to it which says "mymod getting imported"
# 3. In this file: Import mymod
# 3. In mymod: Create a function in the module called "myfunc". It should have a print
#    statement  saying "myfunc getting invoked".
# 4. In this file: Invoke myfunc

import mymod

mymod.myfunc()

print('Challenge 4 -------------')
# Challenge 4:
# Uncomment the following code. Fix the typos so that it runs func1 and func2.

#import anotherlib.py
#from anotherlib import.func2
#anotherlib.py.func1()
#func2()

import anotherlib
from anotherlib import func2
anotherlib.func1()
func2()



