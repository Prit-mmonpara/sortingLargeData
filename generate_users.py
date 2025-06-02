import requests
import json
import random
from concurrent.futures import ThreadPoolExecutor
import time

# Base URL of your API
BASE_URL = "http://localhost:8080/users"

# List of sample names
names = [
    "John", "Jane", "Michael", "Emily", "David", "Sarah", "James", "Emma",
    "William", "Olivia", "Robert", "Sophia", "Daniel", "Isabella", "Matthew",
    "Mia", "Christopher", "Charlotte", "Andrew", "Amelia"
]

# List of sample last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

# List of sample streets
streets = [
    "Main St", "Oak Ave", "Maple Dr", "Cedar Ln", "Pine Rd", "Elm St",
    "Washington Ave", "Park Dr", "Lake Rd", "Hill St", "River Ln",
    "Forest Ave", "Meadow Dr", "Valley Rd", "Mountain St"
]

# List of sample cities
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville",
    "Fort Worth", "Columbus", "San Francisco"
]

def generate_user_data(index):
    """Generate unique user data for each request"""
    first_name = random.choice(names)
    last_name = random.choice(last_names)
    name = f"{first_name} {last_name}"
    email = f"{first_name.lower()}.{last_name.lower()}{index}@example.com"
    street = random.choice(streets)
    city = random.choice(cities)
    address = f"{random.randint(1, 9999)} {street}, {city}"
    
    return {
        "name": name,
        "email": email,
        "address": address
    }

def send_request(user_data):
    """Send a single POST request"""
    try:
        response = requests.post(
            BASE_URL,
            json=user_data,
            headers={"Content-Type": "application/json"}
        )
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending request: {e}")
        return False

def main():
    start_time = time.time()
    successful_requests = 0
    failed_requests = 0
    
    # Number of requests to send
    total_requests = 10000
    
    # Number of concurrent threads
    max_workers = 10
    
    print(f"Starting to send {total_requests} requests...")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Generate all user data first
        user_data_list = [generate_user_data(i) for i in range(total_requests)]
        
        # Send requests in parallel
        results = list(executor.map(send_request, user_data_list))
        
        # Count results
        successful_requests = sum(1 for result in results if result)
        failed_requests = total_requests - successful_requests
    
    end_time = time.time()
    duration = end_time - start_time
    
    print("\nResults:")
    print(f"Total requests: {total_requests}")
    print(f"Successful requests: {successful_requests}")
    print(f"Failed requests: {failed_requests}")
    print(f"Total time: {duration:.2f} seconds")
    print(f"Average time per request: {(duration/total_requests)*1000:.2f} ms")

if __name__ == "__main__":
    main() 