How to use
==========

First, clone the repository and then run 

`pip install -e <path/to/setup/file>`

Run the `etl.py` script first to prepare the data before execuiting the task scripts. Combining all the time
series data resulted in too big a file for GitHub. Not all the data joins because the metadata is limited so
the missing records could be dropped to shrink the file size. Or it could be stored in S3, for example.

Run the etl script in the terminal by using:

`python etl.py`

Run the task scripts in the terminal by using, for example, in the "tasks" folder:

`python task1.py`

Notes on Improvements and Future Considerations
===============================================

### Python packages

These are some python packages that I would include in future:

    - Pydantic and Pandera

       I'd use Pydantic to parse values passed as arguments to methods, functions, etc., for example the user inputs. Pandera would allow for
       checks against the timestamp formatting, for example, and reject the input if the format is not what is expected. I'd use Pandera
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

    - GitHub Actions

      I'd use GitHub Actions for CI/CD to run the unit tests and linter when new code is pushed to the main branch. 

### Notes on scaling

Some considerations for scaling the application:

    - The raw could be stored in S3, or a database (AWS Redshift, for example). The data is sensor-like so if it was to be "real-time", i.e. streaming, data then AWS Kinesis services with AWS lambda could be used for ETL. As part of this pipeline a message could be sent, via AWS SNS for example, from a Lambda function warning the user if the vibration level is rising above a cut-off value that could potentially lead to the turbine shutting down.

    - A web app could be designed to allow the user to select a timestamp and wind farm from an interface. This would then display the status
    information and sensor plots for each turbine on that farm. The sensor information could be displayed in the app as a map of the wind farms showing the status overlaid on the map. Data could be received via APIs, for example.

