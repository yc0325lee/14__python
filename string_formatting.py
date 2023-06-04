# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : string_formatting.py
# - author : yc0325lee
# - created : 2022-10-12 23:03:54 by lee2103
# - modified : 2022-10-12 23:03:54 by lee2103
# - description : 
# ----------------------------------------------------------------------------

# -------------------------------------
# string formatting

if False:
    # (1) formatting with '%'
    year= 2021; month="May"; day=4;
    print("year= %d" % year) # single argument
    print("year= %d, month= %d, day= %s" % (year, month, day)) # multiple arguments with tuple
    print("year= %s, month= %s, day= %s" % (year, month, day)); # %s -> flexible. context를 보고 형변환으로 맞춤
    print("Error rate is %d%%." % 99) # %% -> '%' character

if False:
    # (2) formatting with format()
    year= 2021; month="May"; day=4;
    print("year= {0}, month= {1}, day= {2}".format(year, month, day))
    print("year= {year}, month= {month}, day= {day}"
        .format(year=2021, month="May", day=4) # 'name=value' pair
    )
    print("pi= {0:0.10f}".format(3.141592))

    kwargs = {
        'year' : 2021,
        'month' : "May",
        'day' : 4
    }
    print("year= {year}, month= {month}, day= {day}"
        .format(**kwargs)) # 'name=value' pair

if False:
    # combining positional and keyword arguments
    print("Number one portal is {0}, {1}, and {other}.".format('Geeks', 'For', other='Geeks'))
     
    # using format() method with number format specifiers
    print("Geeks :{0:2d}, Portal :{1:8.2f}".format(12, 0.546))
     
    # Changing positional argument
    print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
     
    print("Geeks: {a:5d},  Portal: {p:8.2f}" .format(a = 453, p = 59.058))

    # adjusting to left/right/center & filling
    # :<10 - left
    # :>10
    # :^10
    print("year= {0:0>6}, month= {1:->6}, day= {2: >4}".format(year, month, day))


if False:
    # (3) formatted string literals or f-string
    # ; string is prefixed with 'f' or 'F'
    # ; python v3.6 or later - see 2.4.3 on LRM
    # ; the most encouraged way for formatting!

    # using simple variables
    name = "Daniel"; age = 45
    print( f"My name is {name} and I'm {age} years old." )
    print( f"I'll be {age+1} years old next year." )
    
    # using dictionary
    me = {"name":"Daniel", "age":45}
    print( f"My name is {me["name"]} and I'm {me["age"]} years old." )
    print( f"I'll be {me["age"]+1} years old next year." )
    
    pi = 3.1415926
    print( f"pi= {pi:10.4f}" ) # with floating-point format specified!
