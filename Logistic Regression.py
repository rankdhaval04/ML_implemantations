

'''implemantation of logistic or sigmoid function

         e=2.71828
         e^x=positive value
         e^-x=vlues between 0 and 1
         
         sigmod function=1/1+e^-x
                  here x is linear equation
         
         '''

def sigmoid(a,b,x):
  
  
  y=(1/(1+(2.71828 ** -(a+(b*x)))))
  
  if(y<=0.5):
    print("Class A")
  else:
    print("Class B")
  
  

def Gradiant_decent(a,b,learning,data):
  
  m=len(data)
  
  for g in range(1,10000):
    cost_a=0
    cost_b=0
  #  print(m)
    for value in data:

      cost_a=cost_a+(((a+(b*value[0]))-value[1]))
      cost_b=cost_b+((((a+(b*value[0]))-value[1]))*value[0])


    cost_a=(cost_a/m)* learning
    cost_b=(cost_b/m)* learning

    a=a-cost_a
    b=b-cost_b
    print(a)
    print(b)
    print("______________")
  return a,b
  
# enter training data in data list
data =[]
a=0.5
b=0.5
learning=0.1
a,b=Gradiant_decent(a,b,learning,data)

#enter value of x for classify
x=
sigmoid(a,b,x)