# it is also need the associativity








#    precedence opreator website se dekhkar yad kare and niche ki link copy karke chrome par paste kar dene par sare precedence yaad kar lenge
#            https://pythongeeks.org/python-operator-precedence/#:~:text=The%20thing%20that,at%20the%20last.











#-------------------------------------------------------------------------------------------------------
 # AND THIS PART LIKE THE `BOD-MAS RULE`
        # IN BODMAS RULE -
          # B - BRACKET - SMALL BRACKET  ()
                    #   - CURLY BRACKET {}
                     #  - SQAURE BRACKET []
          # O - OF [ POWER / % ]                   AND OF means like (multiple)
          # D - DIVIDE
          # M - MULTIPLICATION
          # A - ADDITION
          # S - SUBTRACTION
#---------------------------------------------------------------------------------------------------------
#  IN PRECEDENCE OPERATOR LIKE BOD-MAS RULE , BUT IT IS NOT ACTUALLY BOD-MAS RULE
# operator precedence
# multiplication has a higher precedence over substraction
print(10 - 4 * 2)

# parenthesis () has higher precedence over multiplication
print((10 - 4) * 2)



#  //        - THIS IS THE PART OF DIVISION , BUT IT GIVES ONLY QUOTIENT PART IT IS NOT GIVE QUOTIENT WITH DECIMAL MEANS IT IS NOT GIVE FULLY DECIMAL QUOTIENT PART
#  /         - THIS IS THE PART OF DIVISION  , BUT IT GIVES FULLY QUOTIENT WITH DECIMAL PART


# Associativity (left-to-right in python)
print(5 * 2 // 3 )
# BECAUSE // AND * SAME ORDER SO , THEY ARE EQUAL FOR ORDER
# BECAUSE LEFT TO RIGHT WE SOLVE IN   PRINT(5 // 2 * 3) FIRSTLY SOLVE  5//2  AND THEN WE GET 2 AND THEN SOLVE RIGHT PART  2*3  , IT IS ONLY APPLICABLE WHEN PRECEDENCE OPERATOR SAME

print(5 // 2 * 3)

# EXPONENT -  **  , EXPONENT OPERATOR HAS RIGHT TO LEFT ASSOCIATIVITY
print(2 ** 3 ** 2)

# X == Y
# X != Y
# X < Y
# X > Y
# X <= Y
# X >= Y

print(10-4*2)
print((10-4)*2)
print(5*2//3)



