#standard input/standard output dna nucleotide counter

#important for standard input/output function
import sys

dataset = sys.stdin.read().strip() 

A = dataset.count('A')
G = dataset.count('G')
T = dataset.count('T')
C = dataset.count('C')

#print('Number of A is:', A)
#print('Number of G is:', G)
#print('Number of T is:', T)
#print('Number of C is:', C)

all = A + G + T + C

percentA = A/all *100
percentG = G/all *100
percentT = T/all *100
percentC = C/all *100

percentArounded = round(percentA, 2)
percentGrounded = round(percentG, 2)
percentTrounded = round(percentT, 2)
percentCrounded = round(percentC, 2)

#print('A:', percentArounded, '%')
#print('G:', percentGrounded, '%')
#print('T:', percentTrounded, '%')
#print('C:', percentCrounded, '%')

print('Number of A is:', A,', this is', percentArounded, '%.')
print('Number of G is:', G,', this is', percentGrounded, '%.')
print('Number of T is:', T,', this is', percentTrounded, '%.')
print('Number of C is:', C,', this is', percentCrounded, '%.')
