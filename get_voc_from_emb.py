count = 0

with open('voc.en.txt', 'w') as outfile:
  with open('/ssd_scratch/cvit/binu.jasim/fastText/wiki.en.vec') as f:
    line = f.readline()
    while(line):
      count += 1
      word = line.split(' ', 1)[0]
      outfile.write(word + '\n')
      line = f.readline()

print ('total number of lines = ' + str(count))

