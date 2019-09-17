import numpy as np

def Entropy(positive,nagative,total):
  
  return -(positive/total)* np.log2((positive/total))-(nagative/total)* np.log2((nagative/total))

def attribute_entropy(data,total):
  f_ent=0
  for att in data:
    f_ent=(f_ent+(att[0]+att[1])/total)*Entropy(att[0],att[1],att[0]+att[1])
    
  return f_ent

def Gain(class_entropy,attribute_entropy):
  
  gain=class_entropy-attribute_entropy
  
  return gain


gains=[]
i=0
for attribute in data:
  gains[i]=Gain(Entropy(positive,nagative,total),attribute_entropy(attribute,total))
  print(gains[i])
  i=i+1