import os
import time
import logging

# Configure logging
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_get_data_script():
    print("Attempting to run get_data.py")
    logging.info("Attempting to run get_data.py")
    try:
        os.system("python3 get_data.py")
        print("Successfully ran get_data.py")
        logging.info("Successfully ran get_data.py")
    except Exception as e:
        print(f"Error in get_data.py: {e}")
        logging.error(f"Error in get_data.py: {e}")
        return False
    print("Waiting 10 seconds after get_data.py")
    logging.info("Waiting 10 seconds after get_data.py")
    time.sleep(10)  # 10-second delay after running get_data.py
    return True

def run_youtube_upload_script():
    print("Attempting to run youtube_upload.py")
    logging.info("Attempting to run youtube_upload.py")
    try:
        os.system("python3 youtube_upload.py")
        print("Successfully ran youtube_upload.py")
        logging.info("Successfully ran youtube_upload.py")
    except Exception as e:
        print(f"Error in youtube_upload.py: {e}")
        logging.error(f"Error in youtube_upload.py: {e}")
        return False
    print("Waiting 10 seconds after youtube_upload.py")
    logging.info("Waiting 10 seconds after youtube_upload.py")
    time.sleep(10)  # 10-second delay after running youtube_upload.py
    return True

def update_urls_csv():
    print("Attempting to update urls.csv")
    logging.info("Attempting to update urls.csv")
    try:
        with open("urls.csv", "r") as file:
            lines = file.readlines()
        if lines:
            # Remove the first line (processed URL)
            lines.pop(0)
            with open("urls.csv", "w") as file:
                file.writelines(lines)
            print(f"Processed URL removed from urls.csv. Remaining URLs: {len(lines)}")
            logging.info(f"Processed URL removed from urls.csv. Remaining URLs: {len(lines)}")
        else:
            print("No more URLs to process in urls.csv.")
            logging.info("No more URLs to process in urls.csv.")
    except Exception as e:
        print(f"Error updating urls.csv: {e}")
        logging.error(f"Error updating urls.csv: {e}")

def main():
    loop_counter = 0
    while True:
        loop_counter += 1
        print(f"Starting Loop {loop_counter}")
        logging.info(f"Starting Loop {loop_counter}")

        if run_get_data_script():
            if os.path.exists("data.json"):
                if run_youtube_upload_script():
                    print("Deleting data.json file")
                    logging.info("Deleting data.json file")
                    os.remove("data.json")
                    update_urls_csv()
                    print("Waiting 10 seconds after updating urls.csv")
                    logging.info("Waiting 10 seconds after updating urls.csv")
                    time.sleep(10)  # 10-second delay after updating urls.csv

        waiting_time = 21600  # 6 hours in seconds
        print(f"Completed Loop {loop_counter}. Waiting for {waiting_time / 3600} hours before the next iteration.")
        logging.info(f"Completed Loop {loop_counter}. Waiting for {waiting_time / 3600} hours before the next iteration.")
        time.sleep(waiting_time)  # Wait for 6 hours

if __name__ == "__main__":
    main()
