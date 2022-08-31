# Hyperia-Assignment
This small project is an assingment for a potential position from Hyperia. The given task was to scrape a website for information about available job positons and write them into a JSON file.

## Usage
In order to run this program change direction to project folder and run this command:
    
`python main.py`

## Short explanation

Firstly I request HTML code from given URL. Then i scrape given code for available job links using class `JobsFinder`.

After that I again request HTML code from all returned links using class `JobDataFinder`. Later using the same class I extract specific information about the job posting using beautifulsoup. 
After extraction is done I store recieved information into a dataclass `JobData` which is stored in list located in `JobDataFinder` 's memory.

Later when all information is extracted I return said list of objects to main, where I call my util function to write given objects into a JSON file.


## Dependencies
Developed on python 3.10.5

Required dependencies for this project in order to run properly are:

| Modul     | version |
| ----------- | ----------- |
| beautifulsoup4     | 4.11.1       |
| requests   | 2.28.1       |
