#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:16:24 2021

@author: armaanb
"""

import izhikevich_cells as izh


class ibCell(izh.izhCell):
    """Class containing definition for an intrinsically bursting cell"""
    def __init__(self, stimVal):
        """Create a new intrinsically bursting cell"""
        super().__init__(stimVal)
        self.celltype='Intrinsically Bursting'
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
    
test = ibCell(4000)
test.simulate()
izh.plotMyData(test)