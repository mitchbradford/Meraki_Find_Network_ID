#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Python 3, Meraki python library
# Instructions - Run script to find network ID

#-------------------------------------------------------------------

# Import library
from meraki import meraki

#-------------------------------------------------------------------

# Define API key, org ID, etc
apikey = "XXX"
orgid = "YYY"

#-------------------------------------------------------------------

def get_network_names(myNetworks):
	"""
	Function to search for all the networks in an organisation and create a list containing their names
	"""
	return [element['name'] for element in myNetworks]

def get_network_id(myNetworks):	
	"""
	Function to search for all the network ID's in an organisation and create a list containing their ID's
	"""
	return [element['id'] for element in myNetworks]

	
def main():
	"""
	Function to output network ID and network name for each network in the organisation
	"""
	
	myNetworks = meraki.getnetworklist(apikey, orgid)

	network_name_list = get_network_names(myNetworks)
	network_id_list = get_network_id(myNetworks)
	
	index = 0
	for i in network_name_list:
		
		print(network_name_list[index])
		print(network_id_list[index])
		index = index + 1

		

if __name__ == "__main__":
	main()