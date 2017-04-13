import time
start_time = time.time()
import primes
from fib import *

print  primes.primes(10)
print fib(200)
print("--- %s seconds ---" % (time.time() - start_time))
