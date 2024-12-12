import requests
import csv
import datetime

"""
Website Health Checker with Python

Project Description
Create a command-line tool that monitors the health of a list of websites. 
The app reads a website.txt file where you have listed the websites you want to check.

When executed, the program prints out the status of each website:

Optionally, the program logs the response time and HTTP status code and outputs results into a log.csv file. 
Here is how generated log.csv file should look like after running the program:

"""

# Read URLs from the input file
with open("websit.txt", "r") as file:
    file_list = file.read().strip()

print(file_list)

# Open the output CSV file for writing
with open("output.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "URL", "Response Time (ms)", "Status Code", "Status"])

    # Iterate over each URL
    for i in file_list.split(","):
        i = i.strip()  # Remove any leading/trailing whitespace
        try:
            # Record start time
            start_time = datetime.datetime.now()

            # Make the HTTP GET request with a timeout
            response = requests.get(i, timeout=4)

            # Record end time and calculate response time
            end_time = datetime.datetime.now()
            response_time = (end_time - start_time).total_seconds() * 1000  # Convert to ms

            # Write to CSV
            writer.writerow([
                start_time.strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
                i,  # URL
                int(response_time),  # Response Time (ms)
                response.status_code,  # Status Code
                "online" if response.status_code == 200 else "offline"  # Status
            ])

        except requests.exceptions.RequestException as e:
            # Handle connection errors or timeouts
            writer.writerow([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
                i,  # URL
                "N/A",  # Response Time
                "N/A",  # Status Code
                "offline"  # Status
            ])

print("Data saved to output.csv")

