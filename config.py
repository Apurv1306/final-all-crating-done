import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    GOOGLE_SHEET_CSV_URL = os.getenv('https://docs.google.com/spreadsheets/d/1ghgpG1z4ugXpu4cfOZjkPfPh-7oAQvOZhVRz2XHfot0/export?format=csv')
    GOOGLE_FORM_VIEW_URL = os.getenv('https://docs.google.com/forms/u/0/d/e/1FAIpQLScO9FVgTOXCeuw210SK6qx2fXiouDqouy7TTuoI6UD80ZpYvQ/formResponse')
    GOOGLE_FORM_POST_URL = os.getenv('https://docs.google.com/forms/u/0/d/e/1FAIpQLScO9FVgTOXCeuw210SK6qx2fXiouDqouy7TTuoI6UD80ZpYvQ/formResponse')
    EMAIL_ADDRESS = os.getenv('faceapp0011@gmail.com')
    EMAIL_PASSWORD = os.getenv('ytup bjrd pupf tuuj')
    ADMIN_EMAIL_ADDRESS = os.getenv('projects@archtechautomation.com')
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    FRAME_REDUCE_FACTOR = 0.5
    RECOGNITION_INTERVAL = 180
    HAAR_CASCADE_PATH = './haarcascade_frontalface_default.xml'
