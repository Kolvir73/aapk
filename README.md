Badly hacked together programs to manage the POS exchange on aapks.



copy.py

Reads names and address from a text file a copies each block to the clipboard so I can paste them into a private message on the forum. 
I have my browser open in private messages, a spreadsheet with which user sends to whom, and a terminal running this program.
I create a new PM to the appropriate user and paste the address in it and send. Then I hit enter in the terminal and the next address is copied.
Seems convoluted, but much easier than using the mouse to select and copy each address.


addr_from_csv.py

Makes the formatted text file for use with above. Each is a block separated by a blank line:
Name
Address
Address2 if needed
City, State, Zip


pos_pick.py

Ideally it would take the data from the current year's form, update the addresses if changed, randomly assign a username to each person in the current year, checking to see if they already
have sent to that user in the past.
Mostly AI generated code and doesn't work right. Needs tweaked, but didn't have time this year. 

chart3.py

I could find a easy way to grab the charts for the google form results without having every response, including names and addresses, shown so it takes data from the response and generates
a separate image I could paste in the forum. Mostly AI generated code; I was extremely busy with real work at the time.
