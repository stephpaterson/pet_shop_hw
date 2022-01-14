import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash (pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    # Need to get the current total cash
    # Need to add the cash to the total
    # Need to update the total cash value with the result
    total_cash = pet_shop["admin"]["total_cash"]
    result = total_cash + cash
    pet_shop["admin"]["total_cash"] = result

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]   

def increase_pets_sold(pet_shop, pets_sold):
    total_pets = pet_shop["admin"]["pets_sold"]
    result = total_pets + pets_sold
    pet_shop["admin"]["pets_sold"] = result

def get_stock_count(pet_shop):
    # Need to count the number of pets (list of dict)
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    # Create empty list to hold matches
    # Need to loop through pets (list of dicts)
    # breed == breed given to list
    # return list
    breeds = []
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["breed"] == breed:
            breeds.append(pet)
    
    return breeds

def find_pet_by_name(pet_shop, name):
    found_pet_by_name = None
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            found_pet_by_name = pet
    return found_pet_by_name

def remove_pet_by_name(pet_shop, name):

    pets = pet_shop["pets"]
    for pet in range(len(pets)):
        if pets[pet]["name"] == name:
            del pets[pet]
            break

def add_pet_to_stock(pet_shop, new_pet):
    # need to append new_pet to the list of pets
    pets = pet_shop["pets"]
    pets.append(new_pet)
 
def get_customer_cash(customers):
    return customers["cash"] 

def remove_customer_cash(customer,cash_to_be_removed):
# find customer's cash
# cash = cash - cash_to_be_removed 
    customer_cash = customer["cash"]
    result = customer_cash - cash_to_be_removed
    customer["cash"] = result

def get_customer_pet_count(customer):
    # find customer's pets
    # count the length of the list
    # return the count
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    # add dict new_pet
    # to customer list of pets
    customer["pets"].append(new_pet)
   

