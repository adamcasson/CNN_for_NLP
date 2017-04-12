LAZnet READ ME 

OVERVIEW:

The system intakes data from a .txt file in the format of:
 "index \t STRING \t AFFECT_LABEL \t EVENT \t GENRE \n" 
where the index, string and class labels are tab delminatated 
and each entry is new line deliminated. 

RUN INSTRUCTIONS:

All of the necessary components are packaged,
so once downloaded all that is required is to run "run_me.py" 
in the LAZnet_tf with the pathway of the data file as a 
run-time argument. For example:

$ cd /path/to/LAZnet_tf

$ python3 run_me.py "/path/to/test_data.txt"

which will generate a text file called "predictions.txt" 
which will contain all of the strings with predicted class labels. 
Additonally, during run-time the program will output the current
task being tested and when testing is completed.

FILE MANIFEST:

datascript.py
glove_embedding.py
LAZnet_1_tf.h5
LAZnet_2_tf.h5
LAZnet_3_tf.h5
LAZnet.py
run_me.py

BUGS:

No known bugs

TROUBLESHOOTING:

If TensorFlow throws the following warning it is safe ignore:

"The TensorFlow library wasn't compiled to use SSE instructions, 
but these are available on your machine and could speed up CPU 
computations”

There must not be any typo’s in the class labels for any of the
samples otherwise this will add to the number of classes and will 
not work with LAZnet.
