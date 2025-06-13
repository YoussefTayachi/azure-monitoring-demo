from flask import Flask
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

app = Flask(__name__)

# Logging aktivieren
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=4d0fa20b-7055-48db-8cd3-badfafc17b30;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/;LiveEndpoint=https://westeurope.livediagnostics.monitor.azure.com/;ApplicationId=c67713ca-3e91-4377-b48b-6c4b79f1efd1'
))
logger.setLevel(logging.INFO)

# TEST: Log direkt beim Start der App
logger.info("🚀 Flask App has started")

@app.route('/')
def homepage():
    logger.info('👋 User visited the homepage')
    return 'Hello from Azure Monitoring Demo!'

if __name__ == '__main__':
    app.run(debug=True)
