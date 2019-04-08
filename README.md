# Sentiment Analysis
Scripts to fetch TimeSeries and Sentiment data from Quandl and push them to Azure Event Hub

Enabling co-relation of pricing data and sentimental analysis with Azure streaming analytics service
Sentiment analysis offers added parameter for any company evaluation that may provide insight into what analyst and other influential people are thinking about stock future.  Apart from many regular research information such as quarterly earnings, PE ratio etc., market sentiment can provide another datapoint. 
As shown below, Azure streaming analytics and visualization product such as Power BI can provide real-time view on sentimental data and its relationship with price fluctuations.


Typical flow will include:
1.	Receiving feed from multiple external sources
2.	Processing feeds by fetching relevant information using Azure Streaming Analytics Query Language, a subset of T-SQL syntax
3.	Presenting output to database or Power BI dashboard for real-time visualization


gettsdata.py - This script will receive pricing and sentiment feed from data provider (Quandl in this case)
pushtsdata.py - Script to push pricing and sentiment data to Azure Event Hub
