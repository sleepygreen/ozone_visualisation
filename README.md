ozone_visualisation
==============================

Visualising ozone distributions over Antarctica using data from NASA/ESA satellite sources.

Easiest to set up with Anaconda using the environment.yml file.
Requires logins for NASA/Copernicus websites - set these up at the links below then move .netrc and .cdsapirc files to the /user folder.
Example of how to run the code is containted in main.py

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── config.py          <- Container for all paths and dl options
    ├── .netrc             <- Move to /user and add nasa credentials - set up at https://disc.gsfc.nasa.gov/data-access
    ├── .cdsapirc          <- Move to /user and add esa credentials - set up at https://cds.climate.copernicus.eu/api-how-to  
    ├── main.py            <- Example code run
    |
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The requirements file for reproducing the analysis environment, recreate env in conda with
    │                        conda env create -f environment.yml
    |
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── download.py
    |   |   └── ingest.py
    |   |   └── process.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualization.py
    |       └── animate.py


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
