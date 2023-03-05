def greet():
    return "Hello Man"

def sum(a, b):
    ans = a+b
    # print(ans)
    return ans

# print(greet())
# print(sum(3, 5))
#num = sum(3, 4)
#new_num = 9

#print(num * new_num)

'''
write a function to count the number of even and odd numbers from a series of numbers
'''
list = [34, 2, 9, 100, 43];
ages = [12, 32, 90, 43]

def odd_and_even_count(array):
    even_no_count = 0;
    odd_no_count = 0;
    for x in array:
        if x % 2 == 0:
            even_no_count = even_no_count + 1;
        else:
            odd_no_count = odd_no_count + 1;

    print("even numbers count: "+str(even_no_count))
    print("odd numbers count: "+str(odd_no_count))


odd_and_even_count(list)