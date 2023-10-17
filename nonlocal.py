# outside function 
def outer():
    message = 'abc'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'def'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()