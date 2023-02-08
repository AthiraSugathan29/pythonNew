# 4. Dictionary Comprehension - Covert price from Dollar To Rupee.
def dollar_to_rupee():
    dict1 = {'Book' : 20,'Pen' : 12,'Pencil' : 10}
    dollar = 81.38
    dollar_dict = {i : j * dollar for i,j in dict1.items()}
    return dollar_dict
d_dict = dollar_to_rupee()
print("Dictionary : ",d_dict)


