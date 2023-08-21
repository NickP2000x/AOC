
l = []
loc = 1
with open("2022\day6\input.txt", 'r') as f:
  line = f.read()
  for i in range(len(line)):
    if len(set(line[i:i+14])) == 14:
      print(i + 14)
      break