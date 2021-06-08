time=int(input())
minute,seconds=divmod(time,60)
hour,minute=divmod(minute,60)
day,hour=divmod(hour,24)
year,day=divmod(day,365)
readable_text=[]
values=[year,day,hour,minute,seconds]
words=["year","day","hour","minute","second"]
binded=list(zip(values,words))
for i in binded:
    numbers,text=i
    if numbers:
        readable=[text if numbers==1 else text+"s"]
        readable_word=" "+str(numbers)+" "+"".join(readable)
        readable_text.append(readable_word)
if len(readable_text)==1:
    print("".join(readable_text).strip())
else:
    print((",".join(readable_text[:-1])+"".join(readable_text[-1])).strip())



