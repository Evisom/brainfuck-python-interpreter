import sys

def interpreter(code):
    if code.count('[') != code.count(']'):
        print('ERROR: Unbalanced brackets!')
        return 
    memory = [0]*30000
    memory_index = 0
    i = 0
    cycle_stack = []
    while i < len(code):
        if code[i] == '+': memory[memory_index] +=1
        elif code[i] == ">": memory_index +=1
        elif code[i] == "<": memory_index -=1
        elif code[i] == "-": memory[memory_index] -= 1
        elif code[i] == ".": print(chr(memory[memory_index]), end="")
        elif code[i] == ",": memory[memory_index] = int(input())

        elif code[i] == "[":
            
            inCycleStack = False 
            for q in cycle_stack:
                if i in q:
                    inCycleStack = True 
            if not(inCycleStack):
                cycle_stack.append([i, None])
            if memory[memory_index] == 0 and cycle_stack[-1][1] != None:
                i = cycle_stack[-1][1]

        elif code[i] == "]":
            cycle_stack[-1][1] = i 
            if memory[memory_index] == 0:
                del cycle_stack[-1]
            else:
                i = cycle_stack[-1][0]-1

        if memory_index >= len(memory):
            memory.append(0)
        i+=1

if len(sys.argv) == 1:
    print('BRAINFUCK PYTHON INTERPRETER\nrun script with filename as argument')
else:
    try:
        file = open(sys.argv[1]).readlines()
        file = ''.join(file)
        interpreter(file)
    except:
        print('ERROR: FILE NOT FOUND')
