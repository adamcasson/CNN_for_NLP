import numpy as np

def glove_embedding(text, max_len, nlp):
    word_vectors = np.zeros((len(text),max_len,300))
    
    for index1, x in enumerate(text):
        doc = nlp(x)
        if len(doc) >= max_len:
            for y in range(max_len):
                word_vectors[index1,y,:] = doc[y].vector
        else:
            for index2, y in enumerate(doc):
                word_vectors[index1,index2,:] = y.vector
                
    return word_vectors