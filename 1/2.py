'''
در گروه B مسابقات جام‌جهانی تیم‌های ایران، پرتغال، اسپانیا و مراکش حضور دارند.    
 برنامه‌ای بنویسید که با دریافت نتایج بازی‌ها،
 نام تیم و تعداد برد و باخت و تفاضل گل و امتیاز آن‌ها را
 به ترتیب در یک خط چاپ کند. هر تیم به ترتیب امتیاز در یک خط چاپ شود.
 (در صورتی که امتیاز برابر بود، تعداد برد مدنظر قرار گیرد.
 در صورتی که هم تعداد برد و هم امتیاز برابر بود، بر اساس ترتیب حروف الفبا چاپ شوند.)

نکته: تیم در صورت باخت صفر امتیاز، در صورت تساوی یک امتیاز و در صورت برد سه امتیاز کسب می کند.
تفاضل گل تفاوت گل های زده و گل های خورده یک تیم است

نتایج بازی‌ها را به ترتیب زیر بخواند: (در ورودی نمونه عدد سمت چپ مربوط به تیم سمت راست می‌باشد.)

m_1='Iran-Spain'
m_2='Iran-Portugal'
m_3='Iran-Morocco'
m_4='Spain-Portugal'
m_5='Spain-Morocco'
m_6='Portugal-Morocco'

2-2
2-1
1-2
2-2
3-1
2-1

# x='2-2'
# y=x.split('-')
# print(type(y[0])) ==> str

Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
'''


teams={'Spain':{'wins':0,'loses':0,'draws':0,'goal_difference':0,'points':0},
'Iran':{'wins':0,'loses':0,'draws':0,'goal_difference':0,'points':0},
'Portugal':{'wins':0,'loses':0,'draws':0,'goal_difference':0,'points':0},
'Morocco':{'wins':0,'loses':0,'draws':0,'goal_difference':0,'points':0}}

# print(teams['spain'.capitalize()])


matches=[['Iran','Spain'],['Iran','Portugal'],['Iran','Morocco'],['Spain','Portugal'],['Spain','Morocco'],['Portugal','Morocco']]

for i in range(0,6):
    m_result=input('give match result= ')
    match_result=m_result.split('-')
    m_1=int(match_result[0])
    m_2=int(match_result[1])
    

    # print(matches[i][0])
    # print(type(match_result[0])) #str

    # print(teams[matches[i][0]])
    # print(teams[matches[i][0]]['wins']) #intger
    # print(teams[matches[i][0]]['goal_difference']) #integer
    # print(teams[matches[i][0]]['points']) #integer

    #team 1 win ==>wins+=1,goal_difference+=match_result[1]-match_result[0],points+=3
    #team 2 lose==>loses+=1,goal_difference+=match_result[1]-match_result[0]
    if (m_1>m_2):
        

        #team 1
        teams[matches[i][0]]['wins']+=1
        teams[matches[i][0]]['goal_difference']+=m_1-m_2
        teams[matches[i][0]]['points']+=3

        
        #team 2
        teams[matches[i][1]]['loses']+=1
        teams[matches[i][1]]['goal_difference']-=m_1-m_2
    
    #team 1,2 both get 1 score==> draws+=1,points+=1
    elif int(match_result[0])==int(match_result[1]):
        #team1
        teams[matches[i][0]]['draws']+=1
        teams[matches[i][0]]['points']+=1
        
        #team2
        teams[matches[i][1]]['draws']+=1
        teams[matches[i][1]]['points']+=1

    #team 1 lose==>loses+=1,goal_difference+=match_result[1]-match_result[0]
    #team 2 win ==>wins+=1,goal_difference+=match_result[1]-match_result[0],points+=3
    else:
        
        #team 1
        teams[matches[i][0]]['loses']+=1
        teams[matches[i][0]]['goal_difference']+=m_1-m_2
        # teams[matches[i][0]]['goal_difference']-=m_2-m_1

        #team 2
        teams[matches[i][1]]['wins']+=1
        teams[matches[i][1]]['goal_difference']-=m_1-m_2
        # teams[matches[i][1]]['goal_difference']+=m_2-m_1
        teams[matches[i][1]]['points']+=3


print(teams)



        








