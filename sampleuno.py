import os
import pygame
from random import *

rednumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
bluenumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
yellownumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
greennumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

wild_card = ['wild']
draw4wild = ['wild4']
redspecials = ['skip', 'reverse', 'draw_two']
bluespecials = ['skip', 'reverse', 'draw_two']
yellowspecials = ['skip', 'reverse', 'draw_two']
greenspecials = ['skip', 'reverse', 'draw_two']

numbercards = {'':, '':, '':, '':, '':, ''}
special_cards = {'': , '': , '': , '': , '': , ''}

if card_played == wild_card:
	user_input = input("Pick a new color: ")
	user_input = lower()
	if user_input == "red":
		cardpile = "none"