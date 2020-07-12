import pandas as pd
import pickle


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


gAPI = API_google()
my_apis = gAPI.get_APIs("traffic")
print(my_apis)

# if __name__ == '__main__':
#     Google_API = API_google()


# # Creating a pickle file for the API_google
# filename = 'Google_API.pkl'
# pickle.dump(Google_API, open(filename, 'wb'))
#
# # Loading model to compare the results
# model = pickle.load(open('Google_API.pkl','rb'))
# print(model.get_APIs("ospf"))
