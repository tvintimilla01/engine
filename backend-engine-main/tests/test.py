import pickle

with open(r'recommendation_app\data\user_dict.pkl', 'rb') as f:
    user_dict = pickle.load(f)

print(user_dict[5000])