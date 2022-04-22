import pandas as pd
from apriori_2_algorithm import *
from connection_mongodb import *

# CARREGA DADOS DA BASE - MONGODB
supplements_data_sold_mongodb = getSoldSupplementsCollection().find()


def formatDataMongoDBtoApriori(supplements_data_sold_mongodb):
    data_apriori = []
    for supplement_data in supplements_data_sold_mongodb:
        data_apriori.append([supplement_data['id'], supplement_data['supplement_name']])
    return data_apriori


data_apriori = formatDataMongoDBtoApriori(supplements_data_sold_mongodb)

def formatItemSet(data_apriori):
    data_itemset = []
    text = ""
    for item in data_apriori:
        if item[1] not in str(data_itemset):
            data_itemset.append(item[1])
    for unique in data_itemset:
        text = text + " " + unique
    return data_itemset


def items_by_id(data_apriori):
    ids = []
    items_id = []
    for data_y in data_apriori:
        if str(data_y[0]) not in str(ids):
            ids.append(data_y[0])
    ids_ordenados = sorted(ids)
    for id in ids_ordenados:
        items = []
        for data in data_apriori:
            if id == data[0]:
                items.append(data[1])
        items_id.append(items)
    return items_id

def itemsInStock(data_apriori):
    items_stock = []
    for data in data_apriori:
        if data[1] not in str(items_stock):
            items_stock.append(data[1])
    return items_stock

items_id =items_by_id(data_apriori)
items_by_transaction = pd.Series(items_id)

itemset = formatItemSet(data_apriori)

rules = apriori_2(itemset, items_by_transaction, 0.8, 0.7)

# Products in Stock Message
print("Tip: Our products in stock is: ", itemsInStock(data_apriori))


composite_rule = []
getRuleCollection().drop()

for rule in rules[1]:

    percept = rule['rule'].split('==>')[0].replace(" ", "")
    action = rule['rule'].split('==>')[1].replace(" ", "")

    newRule = {'relation':"==", 'percept_ref': "'" + percept + "'", 'percept_name': "supplement", 'action': "'" + action + "'"}

    getRuleCollection().insert_one({
        'rules': newRule,
        'operators': []
    })