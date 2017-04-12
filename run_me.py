import spacy
import sys
from sklearn import preprocessing
from datascript import grab_data
from LAZnet import LAZnet
from glove_embedding import glove_embedding
from keras.utils import np_utils

#filename = sys.argv[1]

task_1,task_2,task_3, processed_data = grab_data('/Users/adamcasson/Downloads/LAZnet_tf/PS3_test_data_indexed.txt')

def get_predictions(task, task_1, task_2, task_3):
    if task == 1:
        text = [x[0] for x in task_1]
        labels = [x[1] for x in task_1]
        weights_path = 'LAZnet_1_tf.h5'
    if task == 2:
        text = [x[0] for x in task_2]
        labels = [x[1] for x in task_2]
        weights_path = 'LAZnet_2_tf.h5'
    if task == 3:
        text = [x[0] for x in task_3]
        labels = [x[1].strip() for x in task_3]
        weights_path = 'LAZnet_3_tf.h5'
    
    labeler = preprocessing.LabelEncoder()
    labeler.fit(labels)
    classes = labeler.transform(labels)
    num_classes = labeler.classes_.shape[0]
    print(num_classes)
    class_matrix = np_utils.to_categorical(classes,num_classes)
    
    nlp = spacy.load('en')
    
    word_vectors = glove_embedding(text, 30, nlp)
    
    model = LAZnet(weights_path, task)
    model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])
    predictions = model.predict_classes(word_vectors, batch_size=32,verbose=0)
    print(model.evaluate(word_vectors,class_matrix, batch_size=32, verbose=0))
    
    predicted_labels = [str(labeler.classes_[x]) for x in predictions]
    
    return predicted_labels

task1_predictions = get_predictions(1, task_1, task_2, task_3)
print("Testing for task 1...")

for index, x in enumerate(task1_predictions):
    processed_data[index]['genre'] = x
    
task2_predictions = get_predictions(2, task_1, task_2, task_3)
print("Testing for task 2...")

for index, x in enumerate(task1_predictions):
    processed_data[index]['affect'] = x

task3_predictions = get_predictions(3, task_1, task_2, task_3)
print("Testing for task 3...")

c = 0
for x in processed_data:
    if x['event'] != 'NONE':
        x['event'] = task3_predictions[c]
        c += 1
       

f = open('predictions.txt', 'w', encoding="UTF-8")
for x in processed_data:
    f.write(str(x['index'])+'\t'+x['sen']+'\t'+x['affect']+'\t'+x['event']+'\t'+x['genre']+'\n')
f.close()

print("Testing completed. Results can be found in predictions.txt")

    