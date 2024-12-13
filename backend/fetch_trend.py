from pytrends.request import TrendReq

def fetch_google_trends():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[], geo="US", timeframe="now 1-H")
    trending_searches = pytrends.trending_searches()

    for trend in trending_searches[0]:
        print(trend)  # Replace with logic to save to DB

if __name__ == "__main__":
    fetch_google_trends()
