from apscheduler.schedulers.background import BackgroundScheduler
import fetch_hashtags
import fetch_trends

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_hashtags.fetch_trending_hashtags, "interval", minutes=15)
    scheduler.add_job(fetch_trends.fetch_google_trends, "interval", minutes=15)
    scheduler.start()

    try:
        while True:
            pass  # Keep the script running
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    start_scheduler()
