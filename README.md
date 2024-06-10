### DataMapperProject



## Project Overview

DataMapperProject is a FastAPI application designed to allow users to upload CSV files through a web interface. The application parses the uploaded CSV files and stores the contents in a SQLite database. It's specifically created for CSV files containing "Name" and "Age" columns.

## Features

  1.**CSV Upload**: Users can upload CSV files via the frontend, and the application will parse and store the content.


  2. **SQLite Database**: Persistent storage of CSV content into a SQLite database.


  3. **Jinja2 Templating**: Utilizes Jinja2 templates for rendering the frontend.


  4. **Data Validation**: Ensures that only CSV files with the correct format are processed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes



### Prerequisites

 Things you need to install the software and how to install them:

- Python 3


- pip


- virtual environment virtualenv 
- 

### Installation



1. **Clone the repository**

    
    git clone https://github.com/ciscoprogrammer/DataMapperProject.git


    cd DataMapperProject
    

2. **Set up a virtual environment** (optional)

    
    python -m venv venv
    



        
   .\venv\Scripts\activate
        

   

        

3. **Install required packages**

    
    pip install -r requirements.txt


    

4. **Start the FastAPI server**

   
    uvicorn main:app --reload


    

    The application will be available at http://127.0.0.1:8000





## Built With


- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used



- [SQLite](https://www.sqlite.org/index.html) - Database Engine




- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - Template Engine




## License 



This project is licensed under the MIT License.



