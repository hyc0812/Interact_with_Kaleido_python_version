import requests
import json
from random import randrange
node1Header = {"Content-Type": "application/json",
               "accept": "application/json",
               "Authorization": "Basic dTB3ODR1Y2Z4czpJbVhHUElWOEVyV2Z4ZEZxS2toWHM5aTZRb3ZGb0tobUpQN1YxVTZyZHZZ",
               # Signing address deployed the contract
               "kld-from": "0x0A14954680Ed13ae3Ddf2B2f31Be1721Ae5A53f3",
               "kld-sync": "true",
              }

node2Header = {"Content-Type": "application/json",
               "accept": "application/json",
               "Authorization": "Basic dTB3ODR1Y2Z4czpJbVhHUElWOEVyV2Z4ZEZxS2toWHM5aTZRb3ZGb0tobUpQN1YxVTZyZHZZ",
               # Signing address deployed the contract
               "x-kaleido-from": "0x46C620b0559c8aD8320d552dcD0e56b15da42d4b",
               "x-kaleido-sync": "true",
              }

# Base URI 
baseURI = "https://u0z109b1m2-u0e6xl8ne0-connect.us0-aws.kaleido.io/instances/sandra" 

# Contract Address
address='0xb1f0184e929938ca14f69c83278fd5611d2d2d6b'

# Application URI 
appURI  = baseURI + address

getRouteURI = baseURI + "/get"
postRouteURI = baseURI + "/set"
#
#tx = {"x": "29"}

# Get request api call
#response = requests.get(getRouteURI, headers=node1Header)
#print(response.status_code);

#if (response.status_code == 200 ):
#  print(response.json())

# Here we run a post request 100 times with a random transaction number
# Then print the time it took to commit the transaction
# We'll post the transaction to node1 and read the transaction from node2
for x in range(100):
  
  tx={"x": str(randrange(99)) }

  # Send a post request
  response = requests.post(postRouteURI, json=tx, headers=node1Header)
 
  # Validate the response code
  if (response.status_code == 200 or response.status_code == 201):
    
    # Uncomment this if you would like to see the transaction response
    #print (json.dumps(response.json(), indent=4, sort_keys=True))
    
    # Print the time it took from the elapse time from the response header
    print (response.json()['headers']['timeElapsed'])
  
  
  # If you would like to see the response of the get request, 
  # uncomment the below section of the code.
  response = requests.get(getRouteURI, headers=node2Header)
  if (response.status_code == 200 ):
    #print(response.json())
    print(json.dumps(response.json(), indent=4, sort_keys=True))
