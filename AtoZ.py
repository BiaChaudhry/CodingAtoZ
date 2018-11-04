# Python 3 code
# can also be found on my blog: http://seblog1312.blogspot.com/2018/08/coding-to-z.html

#function for drawing alphabets
def alphabet(data):
 str = "O"
 dot = " "
 j = -1

#for drawing A
 if data == "A":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 + str
  for a in range(1,2):
   print(str) + (str)*2 + str
  for a in range(1,3):
   print(str) + (dot)*2 + str

#for drawing B

 elif data == "B":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 + str
  for a in range(1,2):
   print(str) + (str)*3
  for a in range(1,2):
   print(str) + (dot)*2 + str
  for a in range(1,2):
   print(str) + (str)*3

#for drawing C

 elif data == "C":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,4):
   print(str) 
  for a in range(1,2):
   print(str) + (str)*3

#for drawing D

 elif data == "D":
  for a in range(4,5):
   print(str) * a 
  for a in range(3,5):
   print(str) + (dot)*a + str
  for a in range(3,4):
   print(str) + (dot)*a + str
  for a in range(1,2):
   print(str) + (str)*3

#for drawing E

 elif data == "E":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 
  for a in range(1,2):
   print(str) + (str)*3
  for a in range(1,2):
   print(str) + (dot)*2 
  for a in range(1,2):
   print(str) + (str)*3

#for drawing F

 elif data == "F":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 
  for a in range(1,2):
   print(str) + (str)*3
  for a in range(1,2):
   print(str) + (dot)*2 
  for a in range(1,2):
   print(str) 

#for drawing G

 elif data == "G":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 
  for a in range(1,2):
   print(str) 
  for a in range(1,2):
   print(str) + (dot)*2 + str*3
  for a in range(1,2):
   print(str) + (str)*3 + dot + str
  for a in range(1,2):
   print(dot)*5  + str

#for drawing H

 elif data == "H":
  for a in range(1,3):
   print(str) + (dot)*2 +str
  for a in range(1,2):
   print(str) + (str)*3
  for a in range(1,3):
   print(str) + (dot)*2 +str

#for drawing I

 elif data == "I":
  for a in range(5,6):
   print(str) * a 
  for a in range(1,4):
   print(dot)*2+ str + dot
  for a in range(5,6):
   print(str) * a
 
#for drawing J 
 elif data == "J":
  for a in range(5,6):
   print(str) * 9
  for a in range(1,4):
   print(dot)*4+ str 
  for a in range(1,2):
   print(str)+ dot*3 + str
  for a in range(4,5):
   print(str) * a
 
#for drawing K

 elif data == "K":
  for a in range(5,6):
   print(str) + (dot)*3 + str 
  for a in range(1,2):
   print(str) + dot*2 + str
  for a in range(1,2):
   print(str) + str
  for a in range(1,2):
   print(str) + dot*2 + str
  for a in range(1,2):
   print(str) + (dot)*3 + str

#for drawing L

 elif data == "L":
  for a in range(4,5):
   print(dot) * a 
  for a in range(1,4):
   print(str) 
  for a in range(1,2):
   print(str) + (str)*3

#for drawing M

 elif data == "M":
  for a in range(1,2):
   print(str) + (dot)*5 +str
  for a in range(1,2):
   print(str) +str + dot*3 + str*2
  for a in range(1,2):
   print(str) + dot*2 + str + dot*2 + str 
  for a in range(1,3):
   print(str) + (dot)*5 +str

#for drawing N

 elif data == "N":
  for a in range(1,2):
   print(str) + (dot)*5 +str
  for a in range(1,2):
   print(str) +str + dot*4 + str
  for a in range(1,2):
   print(str) + dot*2 + str + dot*2 + str 
  for a in range(1,2):
   print(str) + (dot)*4 +str*2
  for a in range(1,2):
   print(str) + (dot)*5 +str

#for drawing O

 elif data == "O":
  for a in range(5,6):
   print(dot)*2 + str*a
  for a in range(5,6):
   print(dot) + str + (dot)*a + str
  for a in range(7,8):
   print(str)  + (dot)*a + str
  for a in range(5,6):
   print(dot) + str + (dot)*a + str
  for a in range(5,6):
   print(dot)*2 + str*a

#for drawing P
 elif data == "P":
  for a in range(4,5):
   print(str) * a 
  for a in range(1,2):
   print(str) + (dot)*2 + str
  for a in range(1,2):
   print(str) + (str)*2 + str
  for a in range(1,3):
   print(str) 

#for drawing Q

 elif data == "Q":
  for a in range(5,6):
   print(dot)*2 + str*a
  for a in range(5,6):
   print(dot) + str + (dot)*a + str
  for a in range(7,8):
   print(str)  + (dot)*a + str
  for a in range(5,6):
   print(dot) + str + (dot)*a + str
  for a in range(5,6):
   print(dot)*2 + str*a + dot +str

#for drawing R

 elif data == "R":
  for a in range(5,6):
   print(dot) + (str)*3 + dot
  for a in range(5,6):
   print(str) + (dot)*3 + str 
  for a in range(1,2):
   print(str) + dot*2 + str
  for a in range(1,2):
   print(str) + str
  for a in range(1,2):
   print(str) + dot*2 + str
  for a in range(1,2):
   print(str) + (dot)*3 + str

#for drawing S

 elif data == "S":
  for a in range(5,6):
   print(dot) + (str)*3 + dot
  for a in range(5,6):
   print(str) + (dot)*3 + str 
  for a in range(1,2):
   print(str) 
  for a in range(1,2):
   print(str) + str
  for a in range(1,2):
   print(dot) + dot*2 + str
  for a in range(1,2):
   print(dot) + (dot)*3 + str
  for a in range(5,6):
   print(str) + (dot)*3 + str  
  for a in range(5,6):
   print(dot) + (str)*3 + dot

#for drawing T

 elif data == "T":
  for a in range(5,6):
   print(str) * 9
  for a in range(1,4):
   print(dot)*4+ str 
  for a in range(1,2):
   print(dot)+ dot*3 + str
 
#for drawing U

 elif data == "U":
  for a in range(1,5):
   print(str)+ dot*4 + str
  for a in range(5,6):
   print(dot) + str*(a-1) 

#for drawing V

 elif data == "V":
  for a in range(2,6):
   print(dot)*(a) + str + (dot)*(6-(j))+str
   j+=2
  for a in range(2,3):
   print(dot)*(a+4) + str
 
#for drawing W
 elif data == "W":
  for a in range(1,3):
   print(str) + (dot)*5 +str
  for a in range(1,2):
   print(str) + dot*2 + str + dot*2 + str 
  for a in range(1,2):
   print(str) +str + dot*3 + str*2
  for a in range(1,2):
   print(str) + (dot)*5 +str

#for drawing X

 elif data == "X":
  for a in range(1,2):
   print(str) + (dot)*5 +str
  for a in range(1,2):
   print(dot) +str + dot*3 + str
  for a in range(1,2):
   print(dot) + dot*2 + str  
  for a in range(1,2):
   print(dot) +str + dot*3 + str
  for a in range(1,2):
   print(str) + (dot)*5 +str

#for drawing Y

 elif data == "Y":
  for a in range(1,2):
   print(str) + (dot)*5 +str
  for a in range(1,2):
   print(dot) +str + dot*3 + str
  for a in range(1,4):
   print(dot) + dot*2 + str
 
#for drawing Z

 elif data == "Z":
  for a in range(1,2):
   print(str) + (str)*5 +str
  for a in range(1,2):
   print(dot) + dot*4 + str
  for a in range(1,2):
   print(dot) + dot*2 + str  
  for a in range(1,2):
   print(dot) +str 
  for a in range(1,2):
   print(str) + (str)*5 +str
 
#function for calling alphabet() function

def main():
 data = input("Please Enter an Alphabet: ")
 alphabet(data.upper())

main()  #calling main()

