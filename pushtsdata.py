#!/usr/bin/python

# Script to push pricing and sentiment data to Azure Eventbus
# Usage: pushtsdata.py -i price_data
#        pushtsdata.py -i senti_data
# Run script twice as shown above to push both pricing data and sentiment data t                                                                                                         o simulate two separate feeds

import sys
import logging
import datetime
import getopt
import time

def main(argv):
 FILE_DATA = ''
 ADDRESS = ''

 try:
   opts, args = getopt.getopt(argv,"hi:o:",["iSym="])
 except getopt.GetoptError:
   print ('pushtsdata.py -i <FILE_DATA>')
   sys.exit(2)
 for opt, arg in opts:
   if opt == '-h':
         print ('pushtsdata.py -i <FILE_DATA>')
         sys.exit()
   elif opt in ("-i", "--iSym"):
         FILE_DATA = arg

 from azure.eventhub import EventHubClient, Sender, EventData

 logger = logging.getLogger("azure")

# Address can be in either of these formats:
# "amqps://<URL-encoded-SAS-policy>:<URL-encoded-SAS-key>@<mynamespace>.serviceb                                                                                                         us.windows.net/myeventhub"
# "amqps://<mynamespace>.servicebus.windows.net/myeventhub"
# For example:
#ADDRESS = "amqps://mynamespace.servicebus.windows.net/myeventhub"
#ADDRESS = "sb://timeseriesns.servicebus.windows.net/timeserieseh"

# Get pricing data from static file created using gettsdata.py script
 if FILE_DATA == "price_data":
        #ADDRESS="sb://tseventhubsns.servicebus.windows.net/tseventhubs"
        #USER = "MyPolicy"
        #KEY = ""
        ADDRESS = sb://<Your event hub namespace>.servicebus.windows.net/<Your event hub name for price data>
        USER = <Your shared access policy name for price data>
        KEY = <generated key for price data>


# Get sentiment from static file created using gettsdata.py script
 elif FILE_DATA == "senti_data":
        #ADDRESS="sb://tseventhubsns.servicebus.windows.net/sentieventhub"
        #USER = "sentipolicy"
        #KEY = ""
        ADDRESS = sb://<Your event hub namespace>.servicebus.windows.net/<Your event hub name for sentiment data>
        USER = <Your shared access policy name for sentiment data>
        KEY = <generated key for sentiment data>


 try:
    if not ADDRESS:
        raise ValueError("No EventHubs URL supplied.")

# Create Event Hubs client on partition 1
    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    sender = client.add_sender(partition="1")
    client.run()
    try:
        start_time = time.time()
        f = open(FILE_DATA, "r")
        for line in f:
                words = line.split()

# Push data to Azure eventhub
                sender.send(EventData(line))
                print (line)
    except:
        raise
    finally:
        end_time = time.time()
        client.stop()
        run_time = end_time - start_time
        f.close()
        logger.info("Runtime: {} seconds".format(run_time))
 except KeyboardInterrupt:
    pass

if __name__ == "__main__":
   main(sys.argv[1:])
