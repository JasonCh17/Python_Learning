# condition =1
# while condition<10:
#     print(condition)
#     condition=condition+1
# while True:
#     print("I'm True")
# example_list=[1,2,3,4,5,6,7,12,5,55,1,54,212,545,25]
# for i in example_list:
#      print(i)
#      print('inner of for')
#      print('outer of for')
#
# for i in range(1,10,2):
#     print(i)
# x=-1
# y=2
# z=3
# if x>1 :
#     print('x >1')
# elif x<1:
#     print('x<1')
# else:
#     print('x =1')
# def function(a,b):
#     print(a+b)
#
# function(1,3)
# def sale_car(price,color='red',brand='carmy',is_second_hand=True):
#     print('price:',price,
#           'color:',color,
#           'brand:',brand,
#           'is_second_hand:',is_second_hand,
#           )
#
# # sale_car(1000,'red','carmy',True)
# sale_car(1000,color='blue')
# APPLE=100
# a=None
# def fun():
#     global a
#     a=20
#     return a+100
# print('pass=',a)
# print(fun())
# print('now=',a)
# text='This is my first test.' \
#      '\nThis is next line.' \
#      '\nThis is last line'
# # print(text)
# my_file=open('my file.txt','w')
# my_file.write(text)
# my_file.close()
# append_text='\nThis is appended file.'
# my_file=open('my file.txt','a')
# my_file.write(append_text)
# my_file.close()
# file=open('my file.txt','r')
# # content=file.read()
# # print(content)
# content_list=file.readlines()
# print(content_list)
#
# class Calculator:
#     name='Good calculator'
#     price=18
#
#     def add(self,x,y):
#         print(self.name)
#         result=x+y
#         print(result)
#     def minus(self,x,y):
#         result=x-y
#         print(result)
#     def times(self,x,y):
#         print(x*y)
#     def divide(self,x,y):
#         print(x/y)
#
# calcul=Calculator()
# print(calcul.name)
# print(calcul.price)
#
#
# a_input=input('please give a number:')
# print('This input number is:',a_input)
# if a_input =='1':
#     print('this is a good one')
# elif a_input==str(2):
#     print('see you next time')
# else:
#     print('good luck')
import matplotlib.pyplot as plt
import numpy as np
x =np.linspace(-3,3,50)
y1=2*x +1
y2=x**2

plt.figure(num=1)
plt.plot(x,y1)

plt.figure(num=8,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks=np.linspace(-1,2,5)
print(new_ticks)

plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
	[r'$really\ bad $',r'$bad\ \alpha$',r'$normal$',r'$good$','$really\ good$'])

plt.show()


#散点图
import matplotlib.pyplot as plt
import numpy as np
n=1024
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)  #corlor

plt.scatter(X,Y,s=75,c=T,alpha=0.2)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.show()

#柱状图
#等高线
import matplotlib.pyplot as plt
import numpy as np
def f(x,y):
    return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)


plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap='hot')  #热度图
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5) #等高线
plt.clabel(C,inline=True,fontsize=10) #等高线label
plt.show()

#打印图像
#3D图
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)

X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)


plt.show()

#子图(复杂)
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,1])

plt.subplot(223)
plt.plot([0,1],[0,1])

plt.subplot(224)
plt.plot([0,1],[0,1])
plt.show()


