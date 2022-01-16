import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash (pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]   

def increase_pets_sold(pet_shop, number_pets_sold):
    # find pets_sold, add number of pets sold, update value of pets sold.
    pet_shop["admin"]["pets_sold"] += number_pets_sold

def get_stock_count(pet_shop):
    # find list of pets, return length of list i.e. number of pets in stock
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    # Create empty list to hold matches
    # Need to loop through pets (list of dicts)
    # breed == breed given to list
    # return list
    # for loop option:
    # breeds = []
    # pets = pet_shop["pets"]
    # for pet in pets:
    #     if pet["breed"] == breed:
    #         breeds.append(pet)
    # List comprehension method:
    breeds = [pet for pet in pet_shop["pets"] if pet["breed"]==breed]

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
    # find list of pets in pet shop, add new pet to list
    pet_shop["pets"].append(new_pet)
 
def get_customer_cash(customers):
    return customers["cash"] 

def remove_customer_cash(customer,cash_to_be_removed):
    # find customer cash, remove cash_to_be_removed, save to customer cash
    customer["cash"] -= cash_to_be_removed

def get_customer_pet_count(customer):
    # find customer's pets. count the length of the list
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    # add dict new_pet to customer list of pets
    customer["pets"].append(new_pet)
   
def customer_can_afford_pet(customer, new_pet):
    # find out how much money the customer has
    # is it equal or greater than the cost of the pet?
    return customer["cash"] >= new_pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    # take the arguements, pet_shop data, pet found by name (dictionary), customer data
    # return/effect customer pet count, pets sold (in pet shop) update customer cash and shop cash
    # is pet a dictionary? otherwise the pet hadn't been found
    if type(pet) is dict:
    # if customer can afford pet, continue with the sale and take their money and add it to the shop's cash
            if customer_can_afford_pet(customer, pet) == True:
                remove_customer_cash(customer, pet["price"])
                add_or_remove_cash(pet_shop, pet["price"])
    # give pet to customer & remove pet from shop, update number of pets sold
                add_pet_to_customer(customer, pet)
                remove_pet_by_name(pet_shop, pet)
                increase_pets_sold(pet_shop, 1)
