from convert_to_grayscale import *
import os

x = os.getcwd()
pp = os.path.join(x,'dataset')
f = get_batches(pp)
f.__next__()
