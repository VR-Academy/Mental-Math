# -*- coding: utf-8 -*-
"""
Mental Math Trainer (Benjamin Secrets of Mental Math)
"""
import random

CORRECT = 0
ATTEMPT = 0


print('Which chapter do you want to train? (1-9/all)')
ch = int(input())
print('How many?')
num = int(input())
index = 0
stop = False

def addition(CORRECT, ATTEMPT):
    x=int(random.randint(1,1000))
    print('x={}'.format(x))
    y=int(random.randint(1,1000))
    print('y={}'.format(y))
    
    sol = x+y
    
    print('x+y?:')
    sol_human = int(input())
    ATTEMPT += 1
    if sol_human == sol:
        CORRECT+=1
        print('correct')
    else: 
        print('incorrect: {}'.format(sol))

def subtraction(CORRECT, ATTEMPT):
    x=int(random.randint(1,1000))
    print('x={}'.format(x))
    y=int(random.randint(1,1000))
    print('y={}'.format(y))
    
    sol = x-y
    
    print('x-y?:')
    sol_human = int(input())
    ATTEMPT+=1      
    if sol_human == sol:
        CORRECT+=1
        print('correct')
    else:
        print('incorrect: {}'.format(sol))
        
def multiplication(CORRECT, ATTEMPT):
    x=int(random.randint(1,100))
    print('x={}'.format(x))
    y=int(random.randint(1,100))
    print('y={}'.format(y))
    
    sol = x*y
    
    print('x*y?:')
    sol_human = int(input())
    ATTEMPT+=1      
    if sol_human == sol:
        CORRECT+=1
        print('correct')
    else:
        print('incorrect: {}'.format(sol))

def square(CORRECT, ATTEMPT):
    x=int(random.randint(1,100))
    print('x={}'.format(x))
    
    sol = x*x
    
    print('x^2?:')
    sol_human = int(input())
    ATTEMPT+=1      
    if sol_human == sol:
        CORRECT+=1
        print('correct')
    else:
        print('incorrect: {}'.format(sol))
        
if 0<=ch<=9:
    while index < num:
        index+=1
        if 0<=ch<=1:
            addition(CORRECT,ATTEMPT)
            subtraction(CORRECT, ATTEMPT)
        if 1<ch<=2:
            multiplication(CORRECT,ATTEMPT)
            square(CORRECT,ATTEMPT)
print('correct: {}, incorrect: {}'.format(CORRECT, ATTEMPT))