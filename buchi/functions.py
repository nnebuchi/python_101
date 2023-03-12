def greet():
    return "Hello Man"

def sum(a, b):
    ans = a+b;
    return ans;
    # print(ans)
    


# print(greet())
# print(sum(3, 5))
#num = sum(3, 4)
#new_num = 9

#print(num * new_num)

'''
write a function to count the number of even and odd numbers from a series of numbers
'''
list = [34, 2, 9, 100, 43];
ages = [12, 32, 90, 43];

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

#odd_and_even_count(list);

def checkEligibilty(age):

    if(age >= 35):
        print("you are eligible for presidency");
    elif(age >= 30):
        print('You are eligible for Senate');
    elif(age >= 25):
        print("You are eligible for House of Representative");
    else:
        print('You are not eligible for public office')

# checkEligibilty(2);

ng_office_eligibilty_age = {
    "presidency": 35,
    "house_of_senate": 30,
    "house_of_representative": 25
}

gh_office_eligibilty_age = {
    "presidency": 45,
    "house_of_senate": 35,
    "house_of_representative": 30
}

#print(ng_office_eligibilty_age['presidency'])

def checkEligibiltyByOffice(office, current_age):
    office_age = ng_office_eligibilty_age[office];
    if(current_age >= office_age):
        print("You are eligible");
    else:
        print("You are not eligible");

#checkEligibiltyByOffice("house_of_senate", 26);

def checkEligibilty2(office, current_age, country_eligibilty):
    office_age = country_eligibilty[office];
    if(current_age >= office_age):
        print("You are eligible");
    else:
        print("You are not eligible");

checkEligibilty2("presidency", 36, ng_office_eligibilty_age);