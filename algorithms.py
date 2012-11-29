import instafeed_algorithms
import full_house_algorithms

_IF_algs = instafeed_algorithms._ALGORITHMS
_FH_algs = full_house_algorithms._ALGORITHMS
_algs = _IF_algs + _FH_algs

def RunAlgorithm(index, urls):
  module = _algs[index][2]
  return module.sort(urls)

def GetAlgorithms():
  return [tup[:2] for tup in _algs]

def analyzeURLs(urls):
  info = []
  sourceURLs = []
  canonicalizedURLs = []
  #Store all the source and canonicalized URLS in arrays so we can check
  #to see if any given array is unique
  for url in urls:
    sourceURLs.append(url.url)
    canonicalizedURLs.append(url.getNormalized);

  #Traverse through all URLs and find required information.
  #Append results to info list
  for url in urls:
    #Source URL
    source = url.url
    info.append("Source: " + source)
    #Is valid URL
    if url.isValid():
      info.append("Valid: True");
    else:
      info.append("Valid: False");
    #Canonicalized URL
    canonical = url.getNormalized()
    info.append("Canonical: " + canonical);
    #Source URL is unique
    if source in sourceURLs: 
      info.append("Source unique: False");
    else:
      info.append("Source unique: True");
    #Canoicalized URL is unique
    if canonical in canonicalizedURLs:
      info.append("Canonicalized URL unique: False");
    else:
      info.append("Canonicalized URL unique: True");
  return info
