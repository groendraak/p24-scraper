# P24 Scraper

## Overview
The P24 Scraper is a tool designed to extract data from the P24 website efficiently. It automates the process of gathering information and can run on a schedule to fetch the latest data continuously.

## Project Setup Instructions
1. **Clone the Repository**  
   Use the following command to clone the repository:  
   ```bash
   git clone https://github.com/groendraak/p24-scraper.git
   ```  

2. **Navigate into the Project Directory**  
   ```bash
   cd p24-scraper
   ```

3. **Install Dependencies**  
   Use `pip` to install the necessary dependencies listed in `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```  

## How to Run the Scraper
The scraper can be run with a custom scheduling feature. You can either choose to run it immediately or set a custom schedule for specific days of the week.

### Run Now Option
To run the scraper immediately, use the following command:  
```bash
python scraper.py --run-now
```

### Custom Scheduling Feature
You can schedule the scraper to run on specific days of the week. To do this, use the following command:  
```bash
python scraper.py --schedule <days_of_week>
```
Replace `<days_of_week>` with the desired days (e.g., 'mon,tue,wed').

## CSV Output
Once the scraper runs, it generates a CSV file containing the extracted data. The output file will be named `output.csv` and will be located in the project directory. You can open this file with any software that supports CSV format to view the scraped data.