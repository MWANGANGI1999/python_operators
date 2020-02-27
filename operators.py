#Arithmetic operators-are used with numeric values to perform common mathematical operations
#1
#Exponentiation(**)--Raises the first number to the power of the second
a = 3
b = 2

print(a ** b) # same as 3^2

#Modulus(% )--Divides left hand operand by right hand operand and returns remainder
a = 100
b = 2

print(a % b)

#Floor Division(//)--Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
a = 51
b = 3

print(a // b)


#2
#Relational  Operator -carries out the comparison between operands. They tell us whether an operand is greater than the other, lesser, equal, or a combination of those.
#Not equal to(!=)--If values of two operands are not equal, then condition becomes true.
a = 15
b = 3

print(a != b) # returns True because 15 is not equal to 3

#Equal to(= =)--If the values of two operands are equal, then the condition becomes true.
a = 11
b = 13

print(a == b) # returns False because 11 is not equal to 13

#Greater than or equal to(>=)--If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
a = 55
b = 23

print(a >= b) # returns True because 55 is greater, or equal, to 23


#3
#Assignment operators- are used in Python to assign values to variables.
#Assign(=)--Assigns a value to the expression on the left
a = 90

print(a)

#Add and Assign(+=)-Adds the values on either side and assigns it to the expression on the left.
a = 30

a += 10

print(a)

#Subtract and Assign(-=)-Subtracts the value on the right from the value on the left.
a = 500

a -= 100

print(a)


#4
#Logical Operators-These are conjunctions that you can use to combine more than one condition.
#AND-If both the operands are true then condition becomes true.
a = 15

print(a > 14 and a < 20) # returns True because 15 is greater than 14 AND 5 is less than 20

#OR-If any of the two operands are non-zero then condition becomes true.
a = 20

print(a > 13 or a < 14)# returns True because one of the conditions are true (20 is greater than 13, but 5 is not less than 14)

#NOT-Used to reverse the logical state of its operand.
x = 5

print(not(x > 3 and x < 10)) # returns False because not is used to reverse the result


#5
#Identity operators-They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.
#is-True if the operands are identical (refer to the same object)
a = ["Steven", "Mwangangi"]
b = a
print(a is b) # returns True because b is the same object as a

#is not-True if the operands are not identical (do not refer to the same object)
a = ["Steven", "Mwangangi"]
b = a
print(a is not b) # returns false because b is the same object as a


#6
#Membership operators are used to test if a sequence is presented in an object:
#in -Returns True if a sequence with the specified value is present in the object
a = ["Steven", "Mwangangi"]

print("Steven" in a) # returns True because a sequence with the value "Steven" is in the list

#not in-Returns True if a sequence with the specified value is not present in the object

Result Size: 668 x 508
a = ["Steven", "Mwangangi"]
​
print("Munene" not in a) # returns True because a sequence with the value "Munene" is not in the list
​


#7
#Bitwise operators -are used to compare (binary) numbers:
#&(Bitwise AND)-Sets each bit to 1 if both bits are 1
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary

a & b = 1010
         &
        0100
      = 0000
      = 0 (Decimal)
#|(Bitwise OR)-Sets each bit to 1 if one of two bits is 1
a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary

a & b = 1010
         |
        0100
      = 1110
      = 14 (Decimal)
#~(Bitwise NOT)-Inverts all the bits
a = 10 = 1010 (Binary)

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal)