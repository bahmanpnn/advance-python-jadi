'''
در یک نظرسنجی از افراد علاقه‌­مند به تماشای فیلم، درخواست شد تا 3 تا از ژانرهای مورد علاقه‌­ی خود را بنویسند. 6 ژانر مختلف برای انتخاب به آن­‌ها داده شده است که شامل:

Horror, Romance, Comedy, History , Adventure , Action

 برنامهای بنویسید که تعداد افراد را بگیرد
 سپس اسم هر فرد را با ژانرهای مورد علاقش بگیرد
 و اسم هر ژانر و تعداد افراد علاقه‌مند به آن ژانر را به ترتیب از بیشترین علاقه‌مندی در خروجی چاپ کند.
( در صورتی که میزان علاقه‌مندی در ژانرهای مختلف یکسان شد، به ترتیب الفبای انگلیسی در خروجی چاپ کنید.)
 در صورتی که ژانری انتخاب نشد، مقدار آن را صفر در نظر بگیرید و در خروجی اسم و عدد 0 را چاپ کنید.

 4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

'''

n=int(input('give how many persons= '))
genre_dic={'Horror':0,'Romance':0,'Comedy':0,'Action':0,'History':0,'Adventure':0,}


for i in range(0,n):
    p=input('person name+3 genres= ')
    p=p.split(' ')
    for j in range(1,4):
        genre_dic[p[j]]+=1
    

# for key, value in sorted(genre_dic.items(),key=lambda item:item[1],reverse=True):
#first sort by item[1] second sort by item[0]==>sort by count then sort by genres
for key, value in sorted(sorted(genre_dic.items(),key=lambda item:item[0]),key=lambda item:item[1],reverse=True):
    print(key,' : ',value)

