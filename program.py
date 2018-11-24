#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:16:08 2018

@author: kushaldeb
"""

import pandas as pd
import csv
tennis_data = []
result = {}
column = {}
unique_values = []
value_list = {}
output_class_value = {}

def laplacian_estimate(flag):
    for key in probability_dict:
        for classes in output_class_value:
            if(flag == True):
                lap_value = probability_dict[key][classes]+1
                lap_div = output_class_value[classes]+1
            else:
                lap_value = probability_dict[key][classes]
                lap_div = output_class_value[classes]
            
            probability = (lap_value/lap_div)
            probability_dict[key][classes] = probability
    
    prob_calculations = []
    for classes in output_class_value:
        del prob_calculations[:]
        for key in probability_dict:
            prob_calculations.append(probability_dict[key][classes])
        probability_final = prob_calculations[0]
        for i in range(1, len(prob_calculations)):
            probability_final=prob_calculations[i]*probability_final
        if(flag==True):
            lap_total=len(tennis_data)+1
            lap_class=output_class_value[classes]+1
        else:
            lap_total=len(tennis_data)
            lap_class=output_class_value[classes]
        
        probability_final=probability_final*(lap_class/lap_total)
        result[classes]=probability_final
        
    v = list(result.values())
    k = list(result.keys())
    answer = k[v.index(max(v))]
    return answer
                

def main():
    with open("Q2-tennis.csv") as q:
        file = csv.DictReader(q, delimiter=",")
        for row in file:
            tennis_data.append(row)
    i = 0
    for key in tennis_data[0]:
        column[i] = key
        i += 1
    
    print("-"*80)    
    print("Dataset -:")
    data = pd.read_csv("Q2-tennis.csv")
    print(data)
    
    for i in range(0, len(tennis_data)):
        x = tennis_data[i][column[4]]
        flag = 0
        for j in output_class_value:
            if(j == x):
                flag = 1
        if(flag == 0):
            output_class_value[x] = 1
        else:
            output_class_value[x] += 1

    del column[4]
    
    print("-"*80)
    print("\nChoose values for prediction.\n")
    for key in column:
        for i in range(0, len(tennis_data)):
            x = tennis_data[i][column[key]]
            if x not in unique_values:
                unique_values.append(x)
        sq_no = 1
        print("Following are the values of %s:"%(column[key]))
        for fields in unique_values:
            print("%d. %s"%(sq_no, unique_values[sq_no-1]))
            sq_no += 1
        value = int(input("Enter the sequence number of the value to be selected.\n"))
        value_list[column[key]] = unique_values[value-1]
        del unique_values[:]
        print("\n")
    
    print("-"*80)    
    print("The chosen values are:\n")
    for value in value_list:
        print("%s\t:\t%s"%(value, value_list[value]))
    print("-"*80)
    
    laplacian = False
    global probability_dict
    probability_dict = {}
    for value in value_list:
        temp_dict = {}
        for classes in output_class_value:
            for x in column:
                if(value == column[x]):
                    index = x
            prob = 0
            for i in range(0, len(tennis_data)):
                if(value_list[value] == tennis_data[i][column[index]] and classes == tennis_data[i]['Play']):
                    prob += 1
            temp_dict[classes] = prob
        probability_dict[value] = temp_dict
        
    for prob in probability_dict:
        for classes in output_class_value:
            if(probability_dict[prob][classes] == 0):
                laplacian = True
    
    if(laplacian == True):
        print("\nApplying Laplacian smoothing")
        prediction = laplacian_estimate(laplacian)
        
    else:
        print("\nNot applying Laplacian smoothing")
        prediction = laplacian_estimate(laplacian)
       
    return prediction
    
    
if __name__ == "__main__":
    answer = main()
    print("-"*80)
    print("\nProbablility to PLAY")
    for i in result:
        print("%s\t:\t%s"%(i, result[i]))
    print("\nPrediction for PLAY is %s"%(answer))
    print("-"*80)