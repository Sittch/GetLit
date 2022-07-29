my_file = open("corpus/WheelockFull.txt", "r")

data = my_file.readlines() 
memory = [line.strip() for line in data]

my_file.close()


my_file = open("DeBelloGallicoTEST.txt", "r")
data2 = my_file.readlines()

text = [line.split()[0] for line in data2]
my_file.close()

temp = list(set(memory) & set(text)) 


# print(temp)


res = [ ele for ele in text ]
for a in text:
  if a in memory:
    res.remove(a)

print("The Subtracted list is : " + str(res))

print(len(res)/len(text))