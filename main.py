# Курсовая работа #3. Шумихин Алексей. 15.11.2022, устранение замечаний 27.12.2022
from flask import Flask

from bp_api.views import bp_api
from bp_utils.views import bp_utils

app = Flask(__name__)

# next string decomment for debugging
# app.config["DEBUG"] = True
app.json.compact = True


app.register_blueprint(bp_utils)
app.register_blueprint(bp_api)

if __name__ == "__main__":
    app.run()
