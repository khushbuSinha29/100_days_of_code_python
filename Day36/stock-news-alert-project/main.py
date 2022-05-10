import requests
# from twillio.rest import client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# TWILLIO_SID=""
# TWILLIO_AUTH = ""

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    'apikey':"You api key"
}

news_parameters = {
    'q':STOCK,
    'qInTitle':STOCK,
    'apikey': 'Your api key'
}
response_stock = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data=response_stock.json()
# print(stock_data)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

day_before_yest = stock_data['Time Series (Daily)']['2022-05-05']
yesterday = stock_data['Time Series (Daily)']['2022-05-06']
# print(day_before_yest)
# print(yesterday)
day_before_yest_close = day_before_yest['4. close']
# print(day_before_yest_close)
yesterday_close= yesterday['4. close']
print(yesterday_close)


diff_price = float(day_before_yest_close) - float(yesterday_close)
print(diff_price)

up_down=None
if diff_price>0:
    up_down='upemoji'
else:
    up_down='downemoji'

percentage_change = round((diff_price/float(yesterday_close)) *100)
print(percentage_change)
if abs(percentage_change)>5:
    print('Display relevent News')
    print(f"{STOCK}: {up_down}{percentage_change}%")
#
    response_news= requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = response_news.json()
    # print(news_data)
    news_slice = news_data['articles'][:3]
    # print(news_slice)
    for news in news_slice:
        print(f"Headline: {news['title']}")
        print(f"Description: {news['description']}")



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

# client = Client(TWILLIO_SID, TWILLIO_AUTH)
#
# message = client.message.create(
#     body: "",
#     from="twillio phone no,",
#     to = 'actual no.'
# )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

