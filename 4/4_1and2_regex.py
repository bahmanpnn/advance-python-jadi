"""
    https://regex101.com/
    
    . ==>? /everything
    \. ==> own dot
    \w ==>word
    \s ==>white space
    \d ==>digits
    *   =>default {0,infinity}
    *{n}
    *{m,n}
    ^ ==>start
    $ ==>end
    ^abc
    [abc] / [^abc]
    (\.)==>(group)
    .*? ==>be lazy and dont calculate and mine other data

    _____________________________ examples
    .*com$ ==> everything and end of it is com
    @(.*)\.com ==>filter to @everything.com
    ^\d.*
    ^\d.*\d$
    ^\d+$ ==>filter all the lines that just has number
    ^email:(.*) ==> everything that has email: in start of line and grouping after that and filter and save them
    phone:(\d{11}$) ==>group all phone number that have 11 digits after phone:
    this .*? end ==> find the sentences that start with this and end of them is end word.
    ^(\w+)\.*(\w+)\.(\w+) ==> filter and grouping all the names that seprated with . and
                                its possible to have 2 part or 3 part and we want first till third words for grouping and
                                if a name be more than 3 part regex just get first three parts and words
    
    "^\w+\W+"gm


    ############
    ep 2
    package of regex is re and have some methods that we can use.==> re=regular expression
    search / match / findall / sub
    span
    start
    end
    ...


    
    [sS][aA][lL][aA][mM] (\w+)[\.]?
    [sS][aA][lL][aA][mM]\s(.+?)[\.]
    .+@.+\..{2,3}
    .+\@.+\..{2,3} ==>i dont know why jadi used \ for @ ==>\@ :///

"""

import re


# example 1
str="salam bahman.salam amir.Salam asghar. SALAM haji.saLam dadash.salam sotoon"

result=re.search(r'[sS][aA][lL][aA][mM]\s(.+?)[\.]',str)
result2=re.match(r'[sS][aA][lL][aA][mM]\s(.+?)[\.]',str)
print(result)
print(result2)
print("_"*50)
print(result.start())
print(result.end())
print(result.span())



print("_"*50)
# example 2
email="bahmanpn@gmail.com"


result=re.search(r'.+@.+\..{2,3}',email)
if result== None:
    print("email input is not correct!!")
else:
    print(result.group())



print("_"*50)
# example 3
str='''
    the price of oil is 65$ for 3 boshke for yesterday
    the price of oil is 78$ for 3 boshke for today
    the price of oil is 61$ for 3 boshke for tomorrow 23-03
    the price of oil is 63$ for 3 boshke for 24/03/2025
'''

# res=re.findall(r'the price of oil is (\d+)\$ for (\d+\s)boshke for (.*)',str)
res=re.findall(r'the price of oil is (\d+)\$ for (\d+) boshke for (.*)',str)
print(res)
print(res[0])

print("="*25)
for price,boshke_count,day in res:
    print(price,boshke_count,day)



# example 4 sub
print("_"*50)
str="salam bahman.salam amir.Salam asghar. SALAM haji.saLam dadash.salam sotoon"
# print(re.sub('','',str))
# print(re.sub('salam','Hi',str))
# print(re.sub('[sS][aA][lL][aA][mM]','Hi',str))
# print(re.sub('[sS][aA][lL][aA][mM]','Hi',str))
# print(re.sub('([sS][aA][lL][aA][mM])','Hi \g<0>',str)) # all str
# print(re.sub('([sS][aA][lL][aA][mM])','Hi \g<1>',str)) # ==>first group
print(re.sub('[sS][aA][lL][aA][mM] (\w+)\.','Hi \g<1>.',str)) # ==>first group ==> Hi+(\w+).
print(re.sub('[sS][aA][lL][aA][mM] (\w+)','Hi \g<1>',str)) # ==>first group ==> Hi+(\w+)




print("_"*50)
# example 5 ****
str2='''
    the price of oil is 65$ for 3 boshke for yesterday
    the price of oil is 78$ for 3 boshke for today
    the price of oil is 61$ for 3 boshke for tomorrow 23-03
    the price of oil is 63$ for 3 boshke for 24/03/2025
'''

replace_str="the price of oil is (\d+)\$ for (\d+) boshke for (.*)"
res2=re.sub(replace_str,'day: \g<3> -price: \g<1> dollars - \g<2> boshke',str2)
print(res2)