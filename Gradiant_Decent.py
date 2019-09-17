
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
  
  
  
data =[[1,33.8],[2,35.6],[3,37.4],[4,39.2],[5,41.0],[6,42.8]]
a=0.5
b=0.5
learning=0.1
Gradiant_decent(a,b,learning,data)