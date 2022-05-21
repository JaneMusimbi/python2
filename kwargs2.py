def great_multiple(**kwargs):
    keys=kwargs.keys()
    if"name" in keys:
        print("Hello{kwargs['name']}")


    elif "country" in keys:

        print("Hello from{kwargs[country]}")

    else:
        print("Hello Anomous")        
    
    