# graph-generator-python
Generate sample graph data with Python.

This script creates three CSV files. One contains "users" which have an ID and a randomly generated name (pulled from 1990 census data). Another CSV file conains nodes which have only an ID. The last CSV contains connections (edges) between the nodes and users.
## Usage
Install dependencies with pip using the requirements file.

The createData.py script will need to be edited for your needs.

Edit the values like the number of nodes, users, and number of maximum edges per user inside createData.py.  

Edit the output directories for the three CSV files.

Run the createData.py script and enjoy your data.
