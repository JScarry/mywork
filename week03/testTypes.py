#Variable types
#Author: Jarlath Scarry

#practice print variable types
i = 3
print (type(i))

fl = 3.5
print (type(fl))

isa = True
print (type(isa))

memo = "how now Brown Cow"
#added the phrase "how now brown cow" as a memo
print (type(memo))

lots = ["lots"]
#added the letters l,o,t and s to the list lots
print(lots)

i = 3
fl = 3.5
isa = True
memo = 'how now Brown Cow'





#.format to format values and assign them into strings according to their relative position. 1st, 2nd, 3rd.
print('variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))

