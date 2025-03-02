#!/usr/bin/env python3

def hello(func):                                                                                            
    def inner():                                                                                            
        print("Hello ")                                                                                     
        func()                                                                                              
    return inner                                                                                            
                                                                                                            
def name():                                                                                                 
    print("Alice")                                                                                          
                                                                                                            
                                                                                                            
obj = hello(name)                                                                                           
obj()

def who():                                                                                                  
    print("Alice")                                                                                          
                                                                                                            
def display(func):                                                                                          
    def inner():                                                                                            
        print("The current user is : ", end="")                                                             
        func()                                                                                              
    return inner                                                                                            
                                                                                                            
if __name__ == "__main__":                                                                                  
    myobj = display(who)                                                                                    
    myobj()

def pretty_sumab(func):                                                                                     
    def inner(a,b):                                                                                         
        print(str(a) + " + " + str(b) + " is ", end="")                                                     
        return func(a,b)                                                                                    
                                                                                                            
    return inner                                                                                            
                                                                                                            
@pretty_sumab                                                                                               
def sumab(a,b):                                                                                             
    summed = a + b                                                                                          
    print(summed)                                                                                      
                                                                                                            
if __name__ == "__main__":                                                                                  
    sumab(5,3)

import time                                                                                                               
                                                                                                                          
def measure_time(func):                                                                                                   
                                                                                                                          
  def wrapper(*arg):                                                                                                      
      t = time.time()                                                                                                     
      res = func(*arg)                                                                                                    
      print("Function took " + str(time.time()-t) + " seconds to run")                                                    
      return res                                                                                                          
                                                                                                                          
  return wrapper                                                                                                          
                                                                                                                          
@measure_time                                                                                                             
def myFunction(n):                                                                                                        
  time.sleep(n)                                                                                                           
                                                                                                                          
if __name__ == "__main__":                                                                                                
    myFunction(2)