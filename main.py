import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

f = open("chat.txt", "r")
z = []
labls = []
n = 0
e = 0
num = int(
    input(
        'Would you like to check how many times someone sent a word, the actvity of one person, who texts the most, grapoh of chat actvity or time of day or who sends the most iamges or who sends the most charcters'
    ))
if num == 1:
  person = input('Which person do you want to check')
  k = f.readline()
  word = input('WHich word')
  k = k.lower()
  for x in f:
    k = f.readline()
    for i in range(len(k) - len(person) + 1):
      if k[i:i + len(person)] == person:
        e = e + 1
        for i in range(len(k) - len(word) + 1):
          if k[i:i + len(word)] == word:
            n = n + 1
  print(f"they used the word {n} times out of {e} messages")
if num == 2:
  person = input('Which person do you want to check')
  for x in f:
    k = f.readline()
    for i in range(len(k) - len(person) + 1):
      if k[i:i + len(person)] == person:
        r = k.index('[')
        c = k[r + 1:r + 11]
        z.append(c)
  date_counts = dict(Counter(z))

  x_values = list(date_counts.keys())
  y_values = list(date_counts.values())

  plt.plot(x_values, y_values)
  plt.xlabel('Date')
  plt.ylabel('Frequency')
  plt.title(person + ' Frequency Chart')
  plt.show()

if num == 3:
  for x in f:
    k = f.readline()
    if ']' in k:
      p = ']'
      r = k.index(p)
      if ':' in k:
        v = -1
        for i in range(0, 3):
          v = k.find(':', v + 1)
        c = k[r + 2:v]
        if c not in labls:
          labls.append(c)
          z.append(1)
        t = labls.index(c)
        z[t] = z[t] + 1
  myexplode = [0, 0, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  labls[2], labls[4] = labls[4], labls[2]
  z[2], z[4] = z[4], z[2]
  labls[2], labls[3] = labls[3], labls[2]
  z[2], z[3] = z[3], z[2]
  print(len(labls))
  print(len(myexplode))
  plt.pie(z, labels=labls, explode=myexplode, shadow=True)
  plt.title('chat proportions')
  plt.show()

if num == 4:
  for x in f:
    k = f.readline()
    for p in k:
      if p == '[':
        r = k.index(p)
        c = k[r + 1:r + 11]
        z.append(c)
  date_counts = dict(Counter(z))

  x_values = list(date_counts.keys())
  y_values = list(date_counts.values())

  plt.plot(x_values, y_values)
  plt.xlabel('Date')
  plt.ylabel('Frequency')
  plt.title('Date Frequency Chart')
  plt.show()

if num == 5:
  for x in f:
    k = f.readline()
    for p in k:
      if p == ']':
        r = k.index(p)
        c = k[r - 9:r - 4]
        z.append(c)
  date_counts = dict(Counter(z))

  x_values = list(date_counts.keys())
  y_values = list(date_counts.values())

  plt.plot(x_values, y_values)
  plt.xlabel('Time')
  plt.ylabel('Frequency')
  plt.title('Time Frequency Chart')
  plt.show()

if num == 6:
  for x in f:
    k = f.readline()
    for i in range(len(k) - len('image omitted') + 1):
      if k[i:i + len('image omitted')] == 'image omitted':
        p = ']'
        r = k.index(p)
        if ':' in k:
          v = -1
          for i in range(0, 3):
            v = k.find(':', v + 1)
          c = k[r + 2:v]
          if c not in labls:
            labls.append(c)
            z.append(1)
          else:
            t = labls.index(c)
            z[t] = z[t] + 1
  plt.pie(z, labels=labls, shadow=True)
  plt.title('image proportions')
  plt.show()

if num == 7:
  for x in f:
    k = f.readline()
    if ']' in k:
      r = k.index(']')
      if ':' in k:
        v = -1
        for i in range(0, 3):
          v = k.find(':', v + 1)
        c = k[r + 2:v]
        if c not in labls:
          labls.append(c)
          z.append(len(k) - v)
        else:
          t = labls.index(c)
          z[t] = z[t] + (len(k) - v)
  s = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
  for i in range(len(z)):
    s[i].insert(0, z[i])
    s[i].insert(1, labls[i])

  #s.sort(key=lambda x: x[0], reverse=True)
  s.sort(key=lambda x: x[0])
  print(s)
  g = s[0:5]
  u = []
  labls3 = []
  for i in range(len(g)):
    u.append(g[i][0])
    labls3.append(g[i][1])
  plt.bar(labls3, u)
  plt.title('top 5 charcter proportions')
  plt.show()
