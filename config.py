import schedule
import time

# Schedule a job every day at a specific time
# Change 'HH:MM' to your desired time (e.g., '14:00' for 2 PM)
def job():
    print("Job is running...")

# Schedule the job for every day at 09:00 (9 AM)
schedule.every().day.at('09:00').do(job)

# Run the job immediately if needed
if __name__ == '__main__':
    job()  # Run now option
    while True:
        schedule.run_pending()
        time.sleep(1)