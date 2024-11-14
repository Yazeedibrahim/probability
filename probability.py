print("A box contain 5 red and 7 blue. if you randomly pick one ball, what is the probability that is red?\n\n" )
print("######################################\n")
print("########       SOLUTION     ##########\n")
print("######################################")
r = 5
b = 7

total = r+b

print("Red balls = ",r)
print("Blue balls = ",b)

print("The Total balls are = ",total)
p = r/total
per = p * 100
print("the probability of picking a red = ",p ," OR ",per,"%","\n\n")
print("The probability of picking blue ball \n")
ps = b/total
pre = ps * 100
print("the probability of picking a blue = ",ps," OR ",pre,"%")