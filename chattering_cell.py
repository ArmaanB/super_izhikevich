#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:16:24 2021

@author: armaanb
"""

import izhikevich_cells as izh


class chCell(izh.izhCell):
    """Class containing definition for an intrinsically bursting cell"""
    def __init__(self, stimVal):
        """Create a new intrinsically bursting cell"""
        super().__init__(stimVal)
        self.celltype='Chattering cell'
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        self.stimVal = stimVal
    
test = chCell(4000)
test.simulate()
izh.plotMyData(test)