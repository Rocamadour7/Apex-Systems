import os
from moviepy.editor import *
import psycopg2
from psycopg2 import sql
import pandas as pd
from datetime import datetime

def create_video_clips_folder():
    if not os.path.exists('video_clips'):
        os.makedirs('video_clips')

def cut_video(input_file, output_folder):
    clip = VideoFileClip(input_file)
    video_duration = clip.duration
    clip_start_time = 0
    clip_index = 0

    while clip_start_time < video_duration:
        clip_name = f'{clip_start_time}thFrame'
        output_file = os.path.join(output_folder, f'{clip_name}.mp4')
        clip_end_time = clip_start_time + 60 if clip_start_time + 60 < video_duration else video_duration
        subclip = clip.subclip(clip_start_time, clip_end_time)
        subclip.write_videofile(output_file)
        clip_start_time += 60
        clip_index += 1

def create_db_connection():
    return psycopg2.connect(database="db_name", user="db_user", password="db_password", host="localhost", port="5432")

def create_video_data_table():
    conn = create_db_connection()
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE video_data (
        clip_name VARCHAR(255),
        clip_file_extension VARCHAR(5),
        clip_duration INT,
        clip_location VARCHAR(255),
        insert_timestamp TIMESTAMP
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_data_into_table(clip_name, clip_file_extension, clip_duration, clip_location):
    conn = create_db_connection()
    cur = conn.cursor()

    insert_query = sql.SQL("""
    INSERT INTO video_data (clip_name, clip_file_extension, clip_duration, clip_location, insert_timestamp)
    VALUES (%s, %s, %s, %s, %s);
    """)

    data = (clip_name, clip_file_extension, clip_duration, clip_location, datetime.now())
    cur.execute(insert_query, data)
    conn.commit()
    conn.close()

def create_report_folder():
    if not os.path.exists('report'):
        os.makedirs('report')

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('report/generated_video_files.csv', index=False)

if __name__ == "__main__":
    create_video_clips_folder()
    create_report_folder()
    create_video_data_table()
    cut_video("airshow.mp4", "video_clips")

    # Insert records into the video_data table and save to CSV
    video_data = []
    for clip_name in os.listdir("video_clips"):
        clip_file_extension = os.path.splitext(clip_name)[1]
        clip_location = os.path.abspath(os.path.join("video_clips", clip_name))
        clip = VideoFileClip(clip_location)
        clip_duration = int(clip.duration)
        insert_data_into_table(clip_name, clip_file_extension, clip_duration, clip_location)
        video_data.append({'clip_name': clip_name, 'clip_file_extension': clip_file_extension,
                           'clip_duration': clip_duration, 'clip_location': clip_location, 'insert_timestamp': datetime.now()})
    save_to_csv(video_data)
