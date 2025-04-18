import pickle

with open('car-model.bin', 'rb') as f:
    w_0, w = pickle.load(f)

print(w_0)
print(w)
