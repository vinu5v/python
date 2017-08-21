
c = Cricbuzz()
matches = c.matches()
for match in matches:
	if(match['mchstate'] != "nextlive"):
		print (json.dumps(c.livescore(match['id']),indent=0))
