class MyDictionary:
    def __init__(self, key=None, value=None, dctnry=None):
        if key and value and dctnry:
            self.dictionary = dctnry.copy()
            self.dictionary[key] = value
        elif key and value:
            self.dictionary = {key: value}
        elif dctnry:
            self.dictionary = dctnry.copy()
        else:
            self.dictionary = {}
        
    def add_key(self, key, value):
        if key in self.dictionary:
            if self.dictionary[key] == value:
                print("The key and value is already in the dictionary")
                return
            else:
                print("The value of key has been updated")
        self.dictionary[key] = value

    def remove_key(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
        else:
            print(f"The key {key} does not exist")

    def get_value(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            print(f"The key {key} does not exist")
            return None

# main function
if __name__ == "__main__":
    # Create a dictionary with key and value
    my_dict = MyDictionary("name", "John")
    print(my_dict.dictionary)

    # Add a new key and value
    my_dict.add_key("age", 25)
    print(my_dict.dictionary)

    # Add a new key and value
    my_dict.add_key("age", 30)
    print(my_dict.dictionary)

    # Get the value of a key
    print(my_dict.get_value("age"))

    # Remove a key
    my_dict.remove_key("age")
    print(my_dict.dictionary)

    # Remove a key
    my_dict.remove_key("age")
    print(my_dict.dictionary)

    # Create a dictionary with another dictionary
    my_dict = MyDictionary(dctnry={"name": "John", "age": 25})
    print(my_dict.dictionary)

    # Create a dictionary with key and value
    my_dict = MyDictionary("name", "John")
    print(my_dict.dictionary)

    # Create a dictionary with key and value
    my_dict = MyDictionary("name", "John", {"age": 25})
    print(my_dict.dictionary)



