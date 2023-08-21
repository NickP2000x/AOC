"""
        [G]         [D]     [Q]    
[P]     [T]         [L] [M] [Z]    
[Z] [Z] [C]         [Z] [G] [W]    
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]
"""

dic = {1: list('NCRTMZP'),
                             2: list('DNTSBZ'),
                             3: list('MHQRFCTG'),
                             4: list('GRZ'),
                             5: list('ZNRH'),
                             6: list('FHSWPZLD'),
                             7: list('WDZRCGM'),
                             8: list('SJFLHWZQ'),
                             9: list('SQPWN')}
                        

with open('2022\day5\input.txt', 'r') as f:
  for line in f.readlines():
    line = line.strip()
    s = line.split(" ")
    move, loc, to = int(s[1]), int(s[3]), int(s[5])
    print(move, loc, to)

    new = []
    for i in range(move):
      popped = dic[loc].pop()
      new.append(popped)
     
    dic[to].extend(new[::-1])
    new = []
  for num in dic.values():

    print(num[-1])
  
