import pickle
from scipy import spatial
with open('vectors_for_images', 'r') as fp:
  image_vectors = pickle.load(fp)
  vector = None#image_vectors[3]
  #print(image_vectors)
  vector2 = None
  with open('vector_for_caption', 'r') as f:
    vector = pickle.load(f)
  with open('sleeveless_vector', 'r') as f:
    vector2 = pickle.load(f)
  vector = [a_i - b_i for a_i, b_i in zip(image_vectors[2], vector)]
  vector = [a_i + b_i for a_i, b_i in zip(vector, vector2)]
  #print(len(vector[0][0]))
  #vector = image_vectors[3]
  max_similarity = -1
  index = -1
  print(len(image_vectors))
  result = []
  for i, v in enumerate(image_vectors):
    if v is None:# or i == 3:
      continue
    #print(len(vector[0][0]), len(v[0]))
    similarity = 1 - spatial.distance.cosine(vector, v)
    result.append((i, similarity))
    #print(similarity)
    if max_similarity < similarity:
      max_similarity = similarity
      index = i
  result = sorted(result, key=lambda x: x[1])
  print(result[0:4], result[-5:])
  print ("Closest index:", index, "similarity", max_similarity)
