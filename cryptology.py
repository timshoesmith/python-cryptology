code = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh.'

def decoder(message, offset):
    i = 0
    the_sol = ''
    for i in range(len(message)):
        if ord(message[i]) < 97 or ord(message[i]) > 122:
            the_sol += (chr(ord(message[i])))
        else:
            if ord(message[i]) < (122 - offset):
                the_sol += (chr(ord(message[i]) + offset))
            else:
                the_sol += chr( 96 +  (ord(message[i]) + offset) % 122) 
    return the_sol    
print(decoder(code, 10))
print("This is an example of a caesar cipher.")
print("---------------------------------------")


print(decoder(code, 10))
print("This is an example of a caesar cipher.")
print("---------------------------------------")

tocode='hey there! this is an example of a caesar cipher.'

def createCode(tocode, offSet):
    the_sol = ''
    for i in range(len(code)):
        if ord(code[i]) < 97 or ord(code[i]) > 122:
            the_sol += (chr(ord(code[i])))
        else:
            if 96 < (ord(code[i]) - offSet):
                the_sol += (chr(ord(code[i]) - offSet))
                
            else:
                the_sol += chr(122 - ((96 - (ord(code[i]) - offSet))))                  
                
                
               
    return the_sol  

print('This is an example of coding')                     
print(createCode(tocode, 10))
print("----------------------------------")
code2 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx."
print("----------------------------------")
#decoding "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx." using 7
print(decoder(code2,7))
print("-----------------------------------")
letters = 'abcdefghijklmnopqrstuvwxyz'
codeWord = 'friends'

codeToBreak = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
#(decoder(code, 18))

brokenCode = []
def letterNumber(letter):
    j = 0
    for j in range(len(letters)):      
        if letters[j] == letter:      
            return j
def createCodeIndex(code, codeWord):
    i = 0
    codeKey = []
    codeIndex = 0
    for i in range(len(codeToBreak)):
        if ord(code[i]) < 97 or ord(code[i]) > 122:
            codeKey.append(code[i])
        else:
            codeKey.append(letterNumber(codeWord[codeIndex % len(codeWord)]))
            codeIndex += 1   
    return codeKey
    
def printSolution(code, codeWord):
    i = 0
    solution = ''
    codeIndex = createCodeIndex(code, codeWord)
    for i in range(len(code)):
        if ord(code[i]) < 97 or ord(code[i]) > 122:
            solution +=  (code[i])
        else:
            solution += createCode(code[i],codeIndex[i])
    return solution

  
print(printSolution(codeToBreak,codeWord))
print("----------------------------------")
codeToBreak2 = 'you were able to decode this? nice work! you are becoming quite the expert at crytography!'
#(decoder(code, 18))

print(printSolution(codeToBreak2,codeWord))