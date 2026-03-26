def mobile_vivo(func):#decorator
    def wrapper(): 
        print("start of the function wrapper")
        func()
        print("end of the function wrapper")
    return wrapper    
@mobile_vivo
def my_cover():
    print("coffee")
my_cover()