import datetime
import os
import argparse
import src.discover as discover

parser = argparse.ArgumentParser(description='Search for files')
parser.add_argument('--key', type=str, help='Search term')
parser.add_argument('--path', type=str, help='Path to search', default=os.path.expanduser('~'))

args = parser.parse_args()

print(args)


run_start = datetime.datetime.now()

out = discover.hue(args.key, args.path)

i = 1
for f in out:
    print(f'{i}:',f,out[f])
    i += 1
print("Time taken:",datetime.datetime.now()-run_start)
