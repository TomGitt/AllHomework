# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = ('\U0001F463')

User_name = input('Please, enter your name >>> ').title()
User_age =input('Please, enter your age >>> ')

результат = 'My name is'+ ' ' + User_name + ", I am" + ' ' + User_age + ' ' + 'years old' + smile_footprint

print (результат)
