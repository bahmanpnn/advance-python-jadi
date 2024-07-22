'''
The Persian League is the largest sport event dedicated to the deprived areas of Iran. 
The Persian League promotes peace and friendship.
This video was captured by one of our heroes who wishes peace.


2:Persian
3:League
15:Iran
17:Persian
18:League

'''

import re

text="""The Persian League is the largest sport event dedicated to the deprived areas of Iran.
        The Persian League promotes peace and friendship,
        This video was captured by one of our heroes who wishes peace.
        """

text=re.split(', .',text) #re.split('conditions',sting or variable)
text=text[0].split('\n')
text=[item.strip() for item in text]
# print(text)

words_count=0
temp_list=[]

for sentences in range(len(text)):
    new_sens=text[sentences].split()
    # print(sentences,text[sentences])

    for word in range(1,len(new_sens)):
        # if new_sens[word][0]==new_sens[word][0].upper():
        if new_sens[word].capitalize()==new_sens[word]:
            if new_sens[word].endswith('.') or new_sens[word].endswith('.'):
                # define the mapping table
                mapping_table = str.maketrans({',': '', '.': ''})

                # define the input string
                input_string =new_sens[word]

                # use translate() method to replace characters
                new_sens[word]= input_string.translate(mapping_table)
            l=[words_count+1+word,new_sens[word]]
            temp_list.append(l)

    words_count+=len(new_sens)

# print(words_count)
# print(temp_list) 


for item in temp_list:
    print(f'{item[0]}:{item[1]}')






















#############################

# text=text.split(' ')


# temp_list=[]
# for i in range(len(text)):
#     item=text[i]
#     counter=i+1
#     if item == item.capitalize():
#         if item.endswith('.'):
#             item=item.replace('.','')
#         temp_list.append(item)

# print(temp_list)


################# more tips
'''
    import re

    str1 = "Hi, my number is 08999XX. I am 23 years old. I live in 221B Baker Street."

    str1, n = re.subn('[0-9]', 'X',str1)

    print(str1)

    #########tip 2

    # define the mapping table
    mapping_table = str.maketrans({'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'})

    # define the input string
    input_string = "hello world"

    # use translate() method to replace characters
    output_string = input_string.translate(mapping_table)

    print(output_string)

'''