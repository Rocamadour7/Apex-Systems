# Video Processing and Database Interaction

This repository contains a Python script that downloads a video, cuts it into 1-minute clips, and stores information about the clips in a PostgreSQL database. It also saves the clip information to a CSV file.

## Prerequisites

Before running the code, ensure that you have the following prerequisites installed on your system:

- Python 3.x: You can download and install Python from the [official Python website](https://www.python.org/downloads/).

- Required Python libraries: Install the necessary libraries using `pip` by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

- PostgreSQL: Make sure PostgreSQL is installed and running on your system. You will need to have a PostgreSQL database available for the code to interact with.

- Video downloaded.

## Instructions

Follow these steps to set up and run the code:

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where you've saved the code.

3. Modify the code to specify your PostgreSQL database credentials. Open the Python script (e.g., `main.py`) and update the following lines with your database information:

    ```python
    return psycopg2.connect(database="db_name", user="db_user", password="db_password", host="localhost", port="5432")
    ```

4. Run the Python script by executing the following command in your terminal:

    ```
    python main.py
    ```

    This will create the "video_clips" folder, create the "report" folder, cut the video into 1-minute clips, create the `video_data` table in PostgreSQL, insert records into the database, and save the records to a CSV file in the "report" folder.

5. The generated CSV file can be found in the "report" folder with the name `generated_video_files.csv`.

## Additional Notes

- The video clips are named based on the starting frame count, as specified in the assignment. The code will handle this naming convention automatically.

- This repository does not contain the output video clips generated in the process, only the script, CSV file, and this README.

Feel free to reach out if you have any questions or encounter issues.
