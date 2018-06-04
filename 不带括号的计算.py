import re
expression= '100.5+40*5/2-3*2*2/4+9'
l = re.findall('([\d\.]+|/|-|\+|\*)',expression)
print(100.5+40*5/2-3*2*2/4+9)                     # 206.5
def multdiv(l,x):                                 #定义最小的乘除运算单元，l是列表，x代表*或/
    a = l.index(x)                                #首先获取乘除运算符的位置
    if x=='*':                                    #如果是*则执行乘法运算
        k = float(l[a - 1]) * float(l[a + 1])     #获取乘法运算的结果，比如k=3*2
    else:
        k = float(l[a - 1]) / float(l[a + 1])
    del l[a - 1], l[a - 1], l[a - 1]              #删除掉列表里刚做运算的三个元素，比如，3 * 2
    l.insert(a - 1, str(k))                       #将刚计算的结果插入到列表中然后执行下一次计算
    return l
 
def fun(s):
    sum=0
    while 1:                                     #先将乘除运算计算完，在计算加减
        if '*' in l and '/' not in l:            #先判断，如果只有*的话，先计算 *
            multdiv(l, '*')
        elif '*' not in l and '/' in l:          #如果只有 /的话，先计算 /
            multdiv(l, '/')
        elif '*' in l and '/' in l:              #如果既有 / 也有 *的话，先获取他们的下标，
            a = l.index('*')                     #根据下标判断先执行哪个
            b = l.index('/')
            if a < b:
                multdiv(l, '*')
            else:
                multdiv(l, '/')
        else:                                   #当上面的乘除计算完之后，就可以计算加减了
            if l[0]=='-':                       #这里需要判断一下，如果列表里第一个符号是‘-’
                l[0]=l[0]+l[1]                  #的话，表示第一个数是负数，所以我们需要将列表第一和第二项合并起来
                del l[1]
            sum += float(l[0])                  #做完上面的处理后列表中就只剩加减计算了，
            for i in range(1,len(l),2):
                if l[i]=='+':                   #根据符号执行加减计算，将结果保存在sum中
                    sum+=float(l[i+1])
                else:
                    sum-=float(l[i+1])
            break
    return  sum                                 #最后返回这个不含括号表达式的结果
a=fun(l)
print(a)