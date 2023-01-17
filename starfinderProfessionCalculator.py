#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""starfinderProfessionCalculator.py - A program that calculates how much money you make in a week as a Starfinder character."""

"""
 /$$$$$$$$                                      /$$$$$$        /$$       /$$            /$$                    
| $$_____/                                     /$$__  $$      | $$      |__/           |__/                    
| $$        /$$$$$$   /$$$$$$  /$$$$$$$       | $$  \ $$      | $$       /$$ /$$    /$$ /$$ /$$$$$$$   /$$$$$$ 
| $$$$$    |____  $$ /$$__  $$| $$__  $$      | $$$$$$$$      | $$      | $$|  $$  /$$/| $$| $$__  $$ /$$__  $$
| $$__/     /$$$$$$$| $$  \__/| $$  \ $$      | $$__  $$      | $$      | $$ \  $$/$$/ | $$| $$  \ $$| $$  \ $$
| $$       /$$__  $$| $$      | $$  | $$      | $$  | $$      | $$      | $$  \  $$$/  | $$| $$  | $$| $$  | $$
| $$$$$$$$|  $$$$$$$| $$      | $$  | $$      | $$  | $$      | $$$$$$$$| $$   \  $/   | $$| $$  | $$|  $$$$$$$
|________/ \_______/|__/      |__/  |__/      |__/  |__/      |________/|__/    \_/    |__/|__/  |__/ \____  $$
                                                                                                      /$$  \ $$
                                                                                                     |  $$$$$$/
                                                                                                      \______/ 
                                                                                                      
"""

#import modules
from random import randint

# Authorship information
__author__ = "@cirewire"
__email__ = "dreaded.sushi@gmail.com"
__file__ = "starfinderProfessionCalculator.py"
__license__ = "The Unlicense"
__version__ = "1.0.0"
__date__ = "2023/01/16"

# Ask player for Starfinder profession.
profession = input("What is your profession? ")
profession = profession.lower()

# Roll a 1d20 and add the profession's modifier.

roll = randint(1, 20)
modifier = input("What is your modifier? ")
modifier = int(modifier)
total = roll + modifier

# Grab total and then double it.
total = total * 2

# Print the result.
print("You made " + str(total) + " credits as a(n) " + profession + " for the week.")
