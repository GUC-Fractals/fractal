import turtle

amir = turtle.Turtle()

amir.getscreen().bgcolor("black")
amir.color("blue")
amir.speed(20)


amir.penup()
amir.goto(-200,-200)
amir.pendown()


length=450
def Sierpinski_Triangle():
	for j in range(28):
		if(j==0):
			for i in range(3):
				amir.forward(length)
				amir.left(120)
		elif j==1:
			length2 = length/2
			amir.left(60)

			for k in range(7):
				amir.forward(length2)
				amir.right(120)
				for l in range(3):
					amir.forward(length2)
					amir.left(120)
				length2/=2
				amir.left(120)
		elif(j==2):
			length3=length/4
			amir.penup()
			amir.goto(-200,-200)
			amir.pendown()
			
			for m in range(7):
				amir.forward(length3)
				amir.right(120)
				for n in range(3):
					amir.forward(length3)
					amir.left(120)
				
				length3/=2
				amir.left(120)
		elif(j==3):
			length4=length/4
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(length/2)
			amir.left(60)
			amir.pendown()

			for o in range(7):
				amir.forward(length4)
				amir.right(120)
				for p in range(3):
					amir.forward(length4)
					amir.left(120)
				
				length4/=2
				amir.left(120)
		elif(j==4):
			length5 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.right(60)
			amir.forward(length/4)
			amir.left(60)
			amir.pendown()
			
			for q in range(5):
				amir.forward(length5)
				amir.right(120)
				for r in range(3):
					amir.forward(length5)
					amir.left(120)
				
				length5/=2
				amir.left(120)
		elif(j==5):
			length6 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.pendown()
			
			for s in range(5):
				amir.forward(length6)
				amir.right(120)
				for t in range(3):
					amir.forward(length6)
					amir.left(120)
				
				length6/=2
				amir.left(120)
		elif(j==6):
			length7 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length7)
				amir.right(120)
				for v in range(3):
					amir.forward(length7)
					amir.left(120)
				
				length7/=2
				amir.left(120)
		elif(j==7):
			length8 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(length/4)
			amir.left(60)
			amir.pendown()
			
			for w in range(5):
				amir.forward(length8)
				amir.right(120)
				for x in range(3):
					amir.forward(length8)
					amir.left(120)
				
				length8/=2
				amir.left(120)
		elif(j==8):
			length9 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(length/2)
			amir.left(60)
			amir.pendown()
			
			for y in range(5):
				amir.forward(length9)
				amir.right(120)
				for z in range(3):
					amir.forward(length9)
					amir.left(120)
				
				length9/=2
				amir.left(120)
		elif(j==9):
			length10 = length/8
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward((3*length)/4)
			amir.left(60)
			amir.pendown()
			
			for a in range(5):
				amir.forward(length10)
				amir.right(120)
				for b in range(3):
					amir.forward(length10)
					amir.left(120)
				
				length10/=2
				amir.left(120)

		elif(j==10):
			length11 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.right(60)
			amir.forward(length/4)
			amir.left(60)
			amir.pendown()
			
			for q in range(5):
				amir.forward(length11)
				amir.right(120)
				for r in range(3):
					amir.forward(length11)
					amir.left(120)
				
				length11/=2
				amir.left(120)
		elif(j==11):
			length12 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.right(60)
			amir.forward((3/4)*(length/2))
			amir.left(60)
			amir.pendown()
			
			for q in range(5):
				amir.forward(length12)
				amir.right(120)
				for r in range(3):
					amir.forward(length12)
					amir.left(120)
				
				length12/=2
				amir.left(120)
		elif(j==12):
			length13 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.pendown()
			
			for s in range(5):
				amir.forward(length13)
				amir.right(120)
				for t in range(3):
					amir.forward(length13)
					amir.left(120)
				
				length13/=2
				amir.left(120)
		elif(j==13):
			length14 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/2)
			amir.right(60)
			amir.forward((length/2)-((3/4)*(length/2)))
			amir.left(60)
			amir.pendown()
			
			for s in range(5):
				amir.forward(length14)
				amir.right(120)
				for t in range(3):
					amir.forward(length14)
					amir.left(120)
				
				length14/=2
				amir.left(120)
		elif(j==14):
			length15 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length15)
				amir.right(120)
				for v in range(3):
					amir.forward(length15)
					amir.left(120)
				
				length15/=2
				amir.left(120)
		elif(j==15):
			length16 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length16)
				amir.right(120)
				for v in range(3):
					amir.forward(length16)
					amir.left(120)
				
				length16/=2
				amir.left(120)
		elif(j==16):
			length17 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(2*length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length17)
				amir.right(120)
				for v in range(3):
					amir.forward(length17)
					amir.left(120)
				
				length17/=2
				amir.left(120)
		elif(j==17):
			length18 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(3*length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length18)
				amir.right(120)
				for v in range(3):
					amir.forward(length18)
					amir.left(120)
				
				length18/=2
				amir.left(120)
		elif(j==18):
			length19 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(0.5*length)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length19)
				amir.right(120)
				for v in range(3):
					amir.forward(length19)
					amir.left(120)
				
				length19/=2
				amir.left(120)
		elif(j==19):
			length20 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(5*length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length20)
				amir.right(120)
				for v in range(3):
					amir.forward(length20)
					amir.left(120)
				
				length20/=2
				amir.left(120)
		elif(j==20):
			length21 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(6*length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length21)
				amir.right(120)
				for v in range(3):
					amir.forward(length21)
					amir.left(120)
				
				length21/=2
				amir.left(120)
		elif(j==21):
			length22 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.right(60)
			amir.forward(7*length/8)
			amir.left(60)
			amir.pendown()
			
			for u in range(5):
				amir.forward(length22)
				amir.right(120)
				for v in range(3):
					amir.forward(length22)
					amir.left(120)
				
				length22/=2
				amir.left(120)
		elif(j==22):
			length23 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/4)
			amir.pendown()
			
			for w in range(5):
				amir.forward(length23)
				amir.right(120)
				for x in range(3):
					amir.forward(length23)
					amir.left(120)
				
				length23/=2
				amir.left(120)
		elif(j==23):
			length24 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/4)
			amir.right(60)
			amir.forward(length/8)
			amir.left(60)
			amir.pendown()
			
			for w in range(5):
				amir.forward(length24)
				amir.right(120)
				for x in range(3):
					amir.forward(length24)
					amir.left(120)
				
				length24/=2
				amir.left(120)
		elif(j==24):
			length25 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/4)
			amir.right(60)
			amir.forward(4*length/8)
			amir.left(60)
			amir.pendown()
			
			for w in range(5):
				amir.forward(length25)
				amir.right(120)
				for x in range(3):
					amir.forward(length25)
					amir.left(120)
				
				length25/=2
				amir.left(120)
		elif(j==25):
			length26 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(length/4)
			amir.right(60)
			amir.forward(5*length/8)
			amir.left(60)
			amir.pendown()
			
			for w in range(5):
				amir.forward(length26)
				amir.right(120)
				for x in range(3):
					amir.forward(length26)
					amir.left(120)
				
				length26/=2
				amir.left(120)
				
		elif(j==26):
			length27 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward(3*length/4)
			amir.pendown()
			
			for a in range(5):
				amir.forward(length27)
				amir.right(120)
				for b in range(3):
					amir.forward(length27)
					amir.left(120)
				
				length27/=2
				amir.left(120)
		elif(j==27):
			length28 = length/16
			amir.penup()
			amir.goto(-200,-200)
			amir.forward((3*length)/4)
			amir.right(60)
			amir.forward(length/8)
			amir.left(60)
			amir.pendown()
			
			for a in range(5):
				amir.forward(length28)
				amir.right(120)
				for b in range(3):
					amir.forward(length28)
					amir.left(120)
				
				length28/=2
				amir.left(120)
	amir.penup()
	amir.goto(-300,-300)
		

Sierpinski_Triangle()

turtle.done()