#!/usr/local/bin/python3

# print("hello world")

# the support function to get different types of input
# the GET_NUM type: get a positive number with msg as input requirement string
# the YES_NO type: get a yes or no option with msg as input requirement string
def getInput(msg,type):
    if type=="GET_NUM":
        while True:
            line= input(msg)
            try:
                iRound= int(line)
                if(iRound>0):
                    break;
            except ValueError as err:
                print(err)
        return iRound
    elif type=="YES_NO":
        result= "y"
        while True:
            c= input(msg)
            if c=="y" or c=="Y":
                result= "y"
                break
            elif c=="n" or c=="N":
                bContinue= False
                result= "n"
                break;
            else:
                continue
        return result
    else:
        return None

# ref url: https://blog.csdn.net/zhw864680355/article/details/79406383
# import math    
#%a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度      
#只是%f时表示原值，默认是小数点后5位数    
# print "PI=%f" % math.pi             # output: PI=3.141593    
#只是%9f时，表示打印长度9位数，小数点也占一位，不够左侧补空格    
# print "PI=%9f" % math.pi            # output: PI=_3.141593    
#只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0    
# print "PI=%03.f" % math.pi          # output: PI=003    
#%6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格    
# print "PI=%6.3f" % math.pi          # output: PI=_3.142     
#%-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格    
# print "PI=%-6.3f" % math.pi         # output: PI=3.142_    
#还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定    
#如下，不过这种方式06就失去补0的功能，只能补空格    
# print "PI=%*.*f" % (06,3,math.pi)   # output: PI=_3.142    
def showResult(iRound, iCorrect,iWidth):
    print("{0:-^30}".format("轮次："+str(iRound)))
    display= "{0:^30}".format("正确率：" + "%6.2f"%(iCorrect*100.00/iRound)+"%")
    print(display)
    print("-"*(iWidth+3),"\n")
    return None

def showReport():
    return None

# the main framework
while True:
    iRound= getInput("请输入要测试的轮数（请输入整数）: ","GET_NUM")
    iCount=0
    while iCount<iRound:
        showResult(iCount+1,iCount,30)
        iCount+=1
    
    c= getInput("本轮测试完毕！继续测试请输入y，否则输入n结束：","YES_NO")
    if c=="n":
        break;
    
            

