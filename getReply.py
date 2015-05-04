from gw2spidy import Gw2Spidy
import re
from datetime import datetime, date, time

def gemComment(amount):
	# Raw API casted to a string, then split into parts using "{"
	apiReturn = (str(Gw2Spidy.getGemPrice())).rsplit("{")
	# Split again using ","
	split = (apiReturn[2]).split(", ")

	for line in split:

		# Deconstructing the API's return string
		#    The second value of the array will have a "}}" at the end, however it is unknown which part will
		#    So we test both strings

		if "gem_to_gold" in line:
			gemToGold = line
			gemToGold = gemToGold.rsplit(": ")
			gemToGold = gemToGold[1]
			if "}}" in gemToGold:
				gemToGold = gemToGold[:-2]
					
		if "gold_to_gem" in line:
			goldToGem = line
			goldToGem = goldToGem.rsplit(": ")
			goldToGem = goldToGem[1]
			if "}}" in goldToGem:
				goldToGem = goldToGem[:-2]

	today = datetime.utcnow()
	dateTimeString = "As of " + today.strftime(" %m/%d/%y  %I:%M:%S %p (UTC)") + "\n"

	# Crafting the reply with some unit conversions and reddit comment formatting
	reply = dateTimeString + ("The current gem conversion rates for " + str(amount) + " gems are: \n\n" +
			"* "+ str(amount) + " gems costs **" + str(round((((float(goldToGem)/10000)/100)*amount), 2)) + " gold** to buy. \n\n"
			"* " +  str(amount) + " gems will convert into **" + str(round((((float(gemToGold)/10000)/100)*amount), 2)) + " gold**. \n\n" +
			"* " + str(amount) + " gems costs **" + str(round((amount*0.0125), 2)) + " USD** if purchased with real money. \n\n***\n\n"
			"^^Hi! ^^I'm ^^a ^^bot ^^run ^^by ^^/u/snowspirit. ^^If ^^there ^^are ^^any ^^problems, ^^please ^^send ^^her ^^a ^^message! ^^You ^^can ^^also ^^view ^^my ^^source ^^code ^^over ^^[here](https://github.com/snowspirit/gemBot).")
	return(reply)
