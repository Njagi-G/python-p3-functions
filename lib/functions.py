#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")

greet("Guido")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

greet_with_default()

def add(num1, num2):
    pass
    return num1 + num2

sum_add = add(45, 55)
print(sum_add)

def halve(number):
    pass
    return number / 2

answer = halve(100)
print(answer)
