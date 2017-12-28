import sys
import time
import numpy as np

if (len(sys.argv) < 2):
  print ("Should provide a word as argument")
  sys.exit(1)

word1 = sys.argv[1]

def find_emb(word):
  """Find the vector representation (embedding) of a given word"""
  count = 0  
  with open('/scratch/binu.jasim/fastText/wiki.en.vec') as f:
    line = f.readline()
    while(line):
      count += 1
      #tokens = line.split(' ')
      if (line.split(' ', 1)[0] == word):
        #print (' '.join(tokens[1:]))
        #print (word + ' found')
        return line
      if (count % 100000 == 0):
        print ('In progress: ' + str(count))
      
      line = f.readline()
 
  #print ('Word not found')
  return 0


a = time.time()
line1 = find_emb(word1) 

if line1:
  #print(line1)
  #for s in line1.split(' ')[1:301]:
  #  print(float(s))
  emb1 = np.array(line1.split(' ')[1:301]).astype(float)
  
  # If two words are given as arguments, then find the similarity between them 
  if (len(sys.argv) == 3):
    word2 = sys.argv[2]
    line2 = find_emb(word2)
    if line2:
      emb2 = np.array(line2.split(' ')[1:301]).astype(float) 
      sim = np.inner(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
    else:
      print ('Word `' + word2 + '` not found')
      sim = 0
  else:
    # else find the word(s) most similar to word1
        

    sim = np.inner(emb1, emb1) / (np.linalg.norm(emb1)**2)
  print(sim) 
else:
  print('Word `' + word1 + '` not found')

b = time.time()
print ('Time taken: ' + str(b-a) + 's')

#print ('Total number of lines: ' + str(count))        

 
