import re
state= dict()
def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")
def runCodeDomLang(program): 
    for line in program.splitlines():
        line = line.strip()
        if not line:
            continue
        statements = line.split(maxsplit=1)
        if len(statements) != 2:
            continue
        print("statements:",statements)
        statements = line.split()        

        instruction = line
        expression = statements 
      #  expression = statements
       # instruction = line
        #expression= statements
        wholeLine= line
       # print("instruction:", instruction)
       # print("expression:", expression)
       # print("statements:", statements)
        #firstPartG=expression.find("[")+1
        #secondPartG=expression.find("]")    
        if instruction == "ASSIGN":
            firstPart=expression.find("[")+1
            secondPart=expression.find("]")
            
            #print(state)
            #var, val = expression.strip().split('=') ## if a variable x =1 var = X , val = 1
            #print("this is var",var,"this is val", val)
            #print(expression) #also expression would equal x=1
           ## state[var] = val # also make for state which is dict at position var which is a string to equal to val 
            #print("this is state[var]",state[var])
           
            #var, val =expression.strip().split('=')
            state[instruction] = var
            state[var] =val
            var= expression      
        elif line.find("Come on guys, you didn't learn about this from elementary school?") > -1:

            print(line.find("Come on guys, you didn't learn about this from elementary school?"))
            print("this is expression:",expression)

           # firstPart=expression.find("[")+1
           # secondPart=expression.find("]")
            #print(expression[firstPart:secondPart])
            #newExpression = expression[firstPart:secondPart]
            #newLine= expression.strip().split('=')
            #print(newLine)
            #print(expression.strip().split('='))
            var, val =line.strip().split('=')

           # print(expression.strip().split('='))
         
            state[expression[11]] = val
            #print(var[len(var)]-3)            
        elif instruction.find("So the department says") > -1:
            printFunction(expression[len(expression)-1], state)

        elif instruction.find("Ok guys, I'm going to cut your midterm time by half") > -1: 
            thisLine = instruction.strip().split("=")
            print(thisLine)
            getterValLine = thisLine[1]
            print(getterValLine)
            
            under=getterValLine.split(" ")
            print(under[0])
            sum=int(varmap(under[0],state)) 
            print(sum)
            print("this")
            #for i in range(0,len(under)-1):
            sum =0      
            print("under",under[0])
            if(under[0].isdigit()): 
                sum=int(varmap(under[0],state)) 
                if(under[1] == '+'):
                    print(under[2])
                    if(under[2].isdigit()):
                        sum+=int(varmap(under[i+2]),state)
                        print("this sum",sum)
                    #print(expression)  
                if(under[1]== '-'):
                    if(under[2].isdigit()) :
                        sum-=int(varmap(under[i+2]),state)
            else:   
                sum=int(varmap(under[0],state))
                if(under[1] == '+'):
                        sum+=(int)(varmap(under[2],state))
                        print("this sum",sum)
                if(under[1] == '-'):
                    sum-=(int)(varmap(under[2],state))
                    print("this sum",sum)
        else:
            print("Catchphrase not found")

def printFunction(expression, state):
    try:
        val = varmap(expression, state)
        print(val)
    except:
        print("Error: Val not found")

sampleTest1 ="""Come on guys, you didn't learn about this from elementary school? X = 1 
Come on guys, you didn't learn about this from elementary school? Y = 2 
Ok guys, I'm going to cut your midterm time by half =X - Y
"""
sampleTest2 ="""Come on guys, you didn't learn about this from elementary school? X = 1 
Come on guys, you didn't learn about this from elementary school? Y = 2 
So the department says X
So the department says Y
"""
runCodeDomLang(sampleTest1)
runCodeDomLang(sampleTest2)