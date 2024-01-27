import pygame
import random 
import math 

def generate_rand_number(num1, num2):
    """
    Generates a random number in [num1, num2[
    
    """
    rand_number = random.uniform(num1, num2)
    return rand_number 
    
def check_answer(num1, num2, op, answer):
    """
    Checks if answer is correct based on provided numbers and operator. 

    """
    
    if (op == "+"):
        return (num1 + num2 == answer)
    
    elif (op == "-"):
        return (num1 - num2 == answer)
    
    elif (op == "x"):
        return (num1 * num2 == answer)
    
    elif (op == "/"): 
        return (num1 / num2 == answer)
    
