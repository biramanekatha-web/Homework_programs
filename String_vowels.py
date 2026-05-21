String="Instagram"
s="aeiouAEIOU"
count=0
for a in String:
    if a in s:
        count=count+1
print("Total vowels present in a string are ",count)