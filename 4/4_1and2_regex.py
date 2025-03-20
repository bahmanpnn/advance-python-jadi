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
"""
