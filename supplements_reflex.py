from inference_engine import Inference, Rule
import exec_priori_with_data
from connection_mongodb import getRuleCollection

composite_rules = getRuleCollection().find()
inferences = []
for composite_rule in composite_rules:
    rules = []
    rule = composite_rule['rules']

    r = Rule(rule['relation'], rule['percept_ref'], rule['percept_name'], rule['action'])
    rules.append(r)

    inferences.append(Inference(rules, composite_rule['operators'], rule['action']))


item = input("What supplements did you buy? \n")
percepts = [{"supplement": "'" + item + "'" }]



for inference in inferences:

    for percept in percepts:

        inference_result = inference.infer(percept)
        if inference_result != 'False':
            print(f" Supplement bought: {percept.get('supplement')} \n Our purchase suggestion is : {inference_result}! Enjoy our discounts! ")