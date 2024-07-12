'''
برنامه‌ای بنویسید که 10 عدد از ورودی بخواند و در انتها 
عددی که بیشترین تعداد مقسوم‌علیه عدد اول را دارد به همراه تعداد مقسوم‌علیه‌های اول آن، در خروجی چاپ کند
اگر چند عدد این حالت را داشتند، بزرگترین آن‌ها را چاپ کند
'''

def check_aval(i):
    is_prime=True
    for j in range(2,i-1):
        if i%j==0:
            is_prime=False
            break

    return is_prime

def check_maghsooms(x):
    m_list=[]
    for i in range(2,x-1):
        if x%i==0:
            if check_aval(i):
                m_list.append(i)
    return m_list.__len__()

####
# inputs_list={}

x=int(input('give number= '))
# inputs_list[str(x)]=check_maghsooms(x)

answer=[x,check_maghsooms(x)]

for i in range(0,9):
    x=int(input('give number= '))
    ch_ms=check_maghsooms(x)
    if ch_ms>answer[1]:
        answer[0]=x
        answer[1]=ch_ms
    elif ch_ms==answer[1] and x>answer[0]:
        answer[0]=x
        answer[1]=ch_ms
    # inputs_list[str(x)]=ch_ms

# print(inputs_list)
print(answer[0],answer[1])
    

