import random as r
import pandas as pd
# import numpy as np
import tkinter as tk

Cis = [           ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l'],
                  ['g', 'k', 'h', 'm', 'n', 's', 'r'],
                  ['v', 'w', 'z', 'l'],
                  ["dr", "tr", "br", "pr"],
                  ["bl", "pl", "kl", "sl"],
                  ["sm", "sn", "sp", "st", "sk", "str"]]

Vs = [            ['a', 'e', 'i', 'o', 'u'],
                  ["_a_e", "_e_e", "_i_e", "_o_e", "_u_e"],
                  ["ay", "ai", "ea", "ee", "oa"],
                  ["ar", "er", "ir", "or", "ur"],
                  ["ou", "ow", "oi"]]

Cs =  [           ['s', "ss"], ['b', 'p'], ['d', 't'],
                  ['g', 'k'], ["st", "sp", "sk"], ['m', 'n'], 
                  ['m', "mb", "mp"], ['n', "nd", "nt"], ["ph", "ch", "sh", "th"]]
            
class pro_generator():
      def __init__(self, word_number, Ci_order, V_order, C_order):

            self.Cis = Cis
            self.Vs = Vs
            self.Cs = Cs
            
            self.word_number = word_number
            self.Ci_order = Ci_order
            self.V_order = V_order
            self.C_order = C_order

            self.C_on = True

      def generate_Ci(self):
            Ci_pick = self.Cis[self.Ci_order - 1][r.randint(0, len(self.Cis[self.Ci_order - 1]) - 1)]
            return Ci_pick
      
      def generate_V(self):
            V_pick = self.Vs[self.V_order - 1][r.randint(0, len(self.Vs[self.V_order - 1]) - 1)]
            
            if not (V_pick[-1] in ['a', 'e', 'i', 'o', 'u', 'r']):
                  self.C_on = False 
            else:
                  self.C_on = True
            return V_pick
      
      def generate_C(self):
            if self.C_on:
                  C_pick = self.Cs[self.C_order - 1][r.randint(0, len(self.Cs[self.C_order - 1]) - 1)]
                  return C_pick
            return ''
      def generate_phonics(self):
            
            
            words_generated = [ self.generate_Ci() + self.generate_V() + self.generate_C() if self.V_order != 2 
                               else  self.generate_Ci() + self.generate_V()[1] + self.generate_C() + self.generate_V()[3] for _ in range(self.word_number)]
            return pd.Series(data=words_generated, index=range(1, self.word_number + 1))

print("------------------Set number of phonics------------------------------")

word_number = int(input("Number of phonics (>0): "))


print("--------------------Customization settings----------------------")

Ci_cost_on = input("Customization for Ci? (yes/no): ")

if Ci_cost_on == "yes":
      Cis.append(list(map(lambda p: p.strip(), input("Enter customized Ci's (Separated by ','): ").split(","))))
      Ci_order = len(Cis)
else:
      Ci_order = int(input("Select from Ci1~Ci6: "))

V_cost_on = input("Customization for V? (yes/no): ")
if V_cost_on == "yes":
      Vs_cos = list(map(lambda p: p.strip(), input("Enter customized V's (Separated by ','): ").split(",")))
      Vs.append(Vs_cos)
      V_order = len(Vs)
     
else: 
      V_order = int(input("Select from V1~V5: "))

C_cost_on = input("Customization for C? (yes/no):")
if C_cost_on == "yes":
      Cs.append(list(map(lambda p: p.strip(), input("Enter customized C's (Separated by ','): ").split(","))))
      C_order = len(Cs)
else:
      C_order = int(input("Select from C1~C9: "))

phonics = pro_generator(word_number, Ci_order, V_order, C_order)
print("word list: \n\n", phonics.generate_phonics())


#1. 自行輸入頭子音、母音: by 5/10 
# mltk: django/LineBot/
# UI: by 5/10
# 架構先出來[p1][by the end of 4/29]