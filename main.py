import datetime
import sys
import src.discover as discover


run_start = datetime.datetime.now()

if len(sys.argv) == 1:
    out = discover.recursive_list()
elif len(sys.argv) == 2:
    out = discover.recursive_list(sys.argv[1])
elif len(sys.argv) == 3:
    out = discover.hue(sys.argv[2], sys.argv[1])
else:
    print("Invalid number of arguments")

i = 1
for f in out:
    print(f'{i}:',f,out[f])
    i += 1
print("Time taken:",datetime.datetime.now()-run_start)
