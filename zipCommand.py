months = ["Jan","Feb","Mar" , "Apr" 
          , "May","Jun", "Jul" , "Aug" 
          , "Sep" , "oct" , "Nov", "Dec"]

sun = [44.7,65.4,101.7,148.3,170.9
       ,171.4,176.7,186.1,133.9,105.4
       ,59.6,45.8]

# Like a zipper bag
# concatinat 2 listes

for s,m in sorted(zip(sun,months),reverse = True):
    print('{}: {:5.1f} hrs'.format(m, s))
    
# {:5.1f} ==> f = float num , 5 = 5 digit , .1 = get one digit after .     