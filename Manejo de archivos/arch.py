import re
pattern = r"\b(cat)\b"
if re.search(pattern, "The cat sat!"):
    print ("Match 1")
if re.search(pattern, "We s>cat<tered?"):
    print ("Match 2")
if re.search(pattern, "We scattered."):
    print ("Match 3")