# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:27:43 2021

@author: nanashi
"""

from dc_swc_decomp import decompress

with open("example_decompressed.bin", "rb") as ifile:
    decompressed = bytes(decompress("example_compressed.bin"))
    ref = ifile.read()
    
    if decompressed != ref:
        raise ValueError("Mismatch")
    
with open("decoded_test.bin", "wb") as ofile:    
    ofile.write(decompressed)
    
print("Success")