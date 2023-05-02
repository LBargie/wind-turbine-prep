How to
======

First, clone the repository and then run 

`pip install -e <path/to/setup/file>'

Run the task scripts in the terminal by using, for example, in the "tasks" folder:

`python task1.py'

Notes on Improvements and Future Considerations
===============================================

### Python packages

These are some python packages that I would include in future:

    - Pydantic and Pandera

       I'd use Pydantic to parse values passed as arguments to methods, functions, etc., for example the user inputs. I'd use Pandera
       to validate the dataframes passed as arguments to methods/functions (or read in from csv/database, etc.)

    - Logging
    
       I'd use Python's logging package to implement a log in the scripts.
    
    - DuckDB

       If the files remain in .csv format then you could use something like DuckDB and perform SQL directly on the .csv
       without having to use .read_csv(). In addition, the Ibis package provides a pandas-like API on top of DuckDB if 
       you want to avoid writing SQL queries.

### Other tools

Some other tools I would use:

    - Docker
    
       I'd use Docker to containerize the code as an application, i.e. task 3 could be run in a container, then there is
       no need to have python, etc. configured at the user side. I'd use Docker as an evironment for developing the code.


### Notes on scaling

Some considerations for scaling the application:

    - The raw could be stored in S3, or a database (AWS Redshift, for example). The data is sensor-like so if it was to "real-time", i.e. streaming data, then AWS Kinesis services could be used. 

