"""

  The main function. Assume all characters are in ASCII.

"""

import sys, random
import algorithms

from url import URL

def get_strings(f):
  strings = []
  line = f.readline()
  while len(line) > 0:
    # do not add empty line
    if len(line) > 1:
      strings.append(line[:len(line) - 1])
    line = f.readline()
  return strings

if __name__ == "__main__":
  filename = None
  if len(sys.argv) not in (3,3):
    print 'Usage: python main.py input-file output-file'
    exit(1)

  inputfile = open(sys.argv[1])

  strings = get_strings(inputfile)
  urls = [URL(x) for x in strings]

  outputfile = open(sys.argv[2], 'w+')
  results = algorithms.analyzeURLs(urls)
  for item in results:
    outputfile.write('%s\n' % item)

  inputfile.close()
  outputfile.close()
