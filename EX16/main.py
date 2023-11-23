
def aDictionary(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

aDictionary(**my_dict)