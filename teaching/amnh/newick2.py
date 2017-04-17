import turtle

def printTree(s):
     tess = turtle.Turtle()
     level = 1
     for c in s:
          if c == '(':
               level += 1
               tess.left(45)
               tess.forward(1000/2**level)
               tess.right(45)
          elif c == ',':
               tess.right(135)
               tess.forward(1000/2**level)
               tess.left(90)
               tess.forward(1000/2**level)
               tess.left(45)
          elif c == ')':
               tess.left(135)
               tess.forward(1000/2**level)
               tess.right(135)
               level -= 1
          else:
               tess.write(c)
     turtle.exitonclick()

def printTree2(s):
     """
     PrintTree revisited with a while-loop
     (to allow more than single character names)
     """
     tess = turtle.Turtle()
     level = 1
     i = 0
     while i < len(s):
          if s[i] == '(':
               level += 1
               tess.left(45)
               tess.forward(1000/2**level)
               tess.right(45)
               i += 1
          elif s[i] == ',':
               tess.right(135)
               tess.forward(1000/2**level)
               tess.left(90)
               tess.forward(1000/2**level)
               tess.left(45)
               i+= 1
          elif s[i] == ')':
               tess.left(135)
               tess.forward(1000/2**level)
               tess.right(135)
               level -= 1
               i+=1
          else:
               #Build up name-- keep adding until you hit a ',' or ')':
               name = ""
               while not (s[i] == ',' or s[i] == ')'):
                    name = name + s[i]
                    i += 1
               tess.write(name)
               
     turtle.exitonclick()
     

printTree2("((Ape,(Baboon,Chimp)),Dog)")
