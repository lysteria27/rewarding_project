# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:36:54 2021

@author: deyasini
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    key_code={}
    i=0
    d=[]
    for char in map_from:
        key_code[char]=map_to[i]
        i+=1
    
    for char in code:
        d.append(key_code[char])
    decoded=''.join(d)
    return (key_code, decoded)