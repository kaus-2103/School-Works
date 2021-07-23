def func(x,y):
    
  if x<0 or x>=y:
    print("Stop")
    return -1
  else:
    print(y)

  return func(x+1,y)
x=4
y=x*2
func(x,y) 