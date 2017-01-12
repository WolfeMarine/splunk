import splunklib.results as results
import splunklib.client as client
import yaml


# Load settings config file
with open('Splunk_Query_and_Send.yml', 'r') as f:
    config = yaml.load(f)


# Create a Service instance and log in
service = client.connect(
    host=config["Splunk_Settings"]["SplunkServer"],
    port=config["Splunk_Settings"]["SplunkPort"],
    username=config["Splunk_Settings"]["SplunkAccount"],
    password=config["Splunk_Settings"]["SplunkPassword"])


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