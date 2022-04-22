from random import sample
from connection_mongodb import getSoldSupplementsCollection

supplements_type = ["Creatine",
                    "Whey Protein",
                    "Amino",
                    "Antioxidant",
                    "Arginine",
                    "BCAA",
                    "Casein Protein",
                    "Multivitamin",
                    "Omega-3",
                    "Melatonin",
                    "Caffeine",
                    "Zinc",
                    "Magnesium",
                    "Glutamine"]

def createIdList():
    id_list = []
    for id in range(0,100):
        id_list.append(id)

    return id_list

def generate_list_sold_supplements(supplements_type):
    all_sales = []
    for sale in range(0,2000):
        supplement = sample(supplements_type, 1)
        id = sample(createIdList(), 1)
        sale = [id[0],supplement[0]]
        all_sales.append(sale)
    return all_sales

list_sold_supplements = generate_list_sold_supplements(supplements_type)

def insertListMongoDB(list_sold_supplements):
    for sold_supplement in list_sold_supplements:

        getSoldSupplementsCollection().insert_one({
            'id': sold_supplement[0],
            'supplement_name': sold_supplement[1]
        })


#insertListMongoDB(list_sold_supplements)