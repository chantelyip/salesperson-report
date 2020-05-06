"""Generate sales report showing total melons each salesperson sold."""

 
salespeople = [] #empty list for salespeople
melons_sold = [] #empty list for melons sold

f = open('sales-report.txt') #open file
for line in f: #looping over each line in file
    line = line.rstrip() #stripping off trailing white spaces on the right of each line
    entries = line.split('|') #split words where 'pipe' is to distinguish individual entries, creating a list of data

    salesperson = entries[0] #each salesperson's name is at index 0
    melons = int(entries[2]) #melons sold is at index 3 

    if salesperson in salespeople: #if salesperson is already in `salespeople`, increment the no. of
    #melons they've sold.
    # Otherwise, add the salesperson's name to `salespeople` and
    # `melons` to `melons_sold`
        position = salespeople.index(salesperson)  #Find the position where `salesperson` is stored in `salespeople`
        # Use that position to index into `melons_sold`
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Loop over indices of `salespeople` and use it to index into `salespeople` and # `melons_sold`.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
