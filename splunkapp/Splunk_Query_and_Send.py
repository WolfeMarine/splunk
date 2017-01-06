import splunklib.results as results
import splunklib.client as client

HOST = "localhost"
PORT = 8089
USERNAME = "admin"
PASSWORD = "expediarules"

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Print installed apps to the console to verify login
#for app in service.apps:
#    print app.name


# Run an export search and display the results using the results reader.

# Set the parameters for the search:
# - Search everything in the last hour
# - Run a normal-mode search
# - Search internal index
kwargs_export = {"earliest_time": "-15m",
                 "latest_time": "now",
                 "search_mode": "normal"}
searchquery_export = "search * index=main | head 10"

exportsearch_results = service.jobs.export(searchquery_export, **kwargs_export)

# Get the results and display them using the ResultsReader
reader = results.ResultsReader(exportsearch_results)
for result in reader:
    if isinstance(result, dict):
        print "Result: %s" % result
    elif isinstance(result, results.Message):
        # Diagnostic messages may be returned in the results
        print "Message: %s" % result

# Print whether results are a preview from a running search
#print "is_preview = %s " % reader.is_preview