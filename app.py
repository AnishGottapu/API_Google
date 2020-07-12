# Importing essential libraries
from flask import Flask, render_template, request, url_for
import pandas as pd

# filename = 'Google_API.pkl'
# classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


class API_google():
    def __init__(self):
        self.df = pd.read_excel("API_list.xlsx")
        self.length = len(self.df.index)

    def get_APIs(self, input):
        return_list = []
        for i in range(self.length):
            if input in self.df.loc[i][0]:
                return_list.append(self.df.loc[i][0])
        return return_list


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        apiname = request.form['APINAME']
        gAPI = API_google()
        my_apis = gAPI.get_APIs(apiname)

        return render_template('result.html', apiname=apiname, my_apis=my_apis)


if __name__ == '__main__':
    app.run()
