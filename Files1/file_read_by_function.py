# Write a program to read a file line by line and store it into a list.
def file_read(fna):
    with open(fna) as f: # open the file by default read mode and give alias name 'f'.File close also working with this code
        output_list = f.readlines() # read file line by line and returns it into a list
    print(output_list)
file_read('file_test1')

# def file_read(fna):
#     with open(fna,'a') as f: # open the file by default read mode and give alias name 'f'.File close also working with this code
#         output_list = f.readlines() # read file line by line and returns it into a list
#     print(output_list)
# file_read('file_test1')