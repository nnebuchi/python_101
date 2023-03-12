# In a family reality TV show, different families are expected to register three family members only.

# The criteria is such that the sum of the ages of the three family members must not exceed 100.

# Write a function to determine if the a family is eligible.

# Hint: your function should accept 3 arguments with each argument representing the age of each family member

# step 1

ageEligibility = {
    'fatherEligibilityAge': 45,
    'motherEligibilityAge': 30,
    'childEligibilityAge': 15
}

def checkEligibilty(father_age, mother_age, child_age):
        
    if (father_age + mother_age + child_age <= 100):
        print("you are eligible")
    else:
        print("you are not eligible")
    
checkEligibilty(55, 30, 45)

    
    
    


        




