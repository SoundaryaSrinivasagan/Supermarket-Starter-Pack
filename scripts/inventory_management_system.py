import sample_data

# Add Item to Inventory
'''
 Function:         add_item(name, price)
 Description:      This function should be able to add an item to the Cost dictionary / item_dict
 Input Parameters: Name  : String
                   Price : Integer (Assumption)
'''
add_item = lambda name, price: item_dict.update({str(name):int(price)})

# Remove Item to Inventory
'''
 Function:         remove_item(name)
 Description:      This function should be able to remove an item from the Cost dictionary / item_dict
 Input Parameters: Name : String
'''
def remove_item(name):
  del item_dict[name]
  success_msg = 'Item has been removed successfully'
  return(success_msg)

# Frequency Counter of Items in Inventory
'''
 Function:         frequency_counter(flag)
 Description:      This Function will create a Frequency Counter to count the number of items
 Input Parameters: flag : Boolean
                          If the Flag is true, the frequency counter will become active
'''
frequency_dict = {}  # creating the Empty Dictionary

def frequency_counter(flag):
  if (flag == True):
    for transaction in transaction_data: # looping over each transaction
      for item in transaction: # looping over each item present in the transaction
        if item in frequency_dict:
           frequency_dict[item] += 1 # increment the frequency by 1 if the item is found in the dictionary
        else:
           frequency_dict[item] = 1 # create a new key with the item name if the item is found for the first time
  return(frequency_dict)

# Update Frequency Counter with every transaction
'''
 Function:         update_counter(flag)
 Description:      This Function will automatically update the Frequency Counter in the case any New Transactions are made
 Input Parameters: flag : Boolean
                          If the Flag is true, the frequency counter will become active
'''
update_counter = lambda flag: frequency_counter(flag)

