# define Python user-defined exceptions
try:
    age= -10
    print("Age is:")
    print(age)
    if age<0:
        raise ValueError
    yearOfBirth= 2021-age
    print("Year of Birth is:")
    print(yearOfBirth)
except ValueError:
    print("Input Correct age.")
