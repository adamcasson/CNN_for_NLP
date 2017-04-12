#read in data from file
def grab_data(filename):
    file = open(filename,encoding="UTF-8")

#task 1 strip everything except string and genre tag
#initialize empty array
    processed_data = []
    #feed each line into the array
    for line in file.readlines():
            rawarray = line.split("\t")
            processed_data.append({ 
            "index":int(rawarray[0]),
            "sen":rawarray[1],
            "affect":rawarray[2],
            "event":rawarray[3],
            "genre":rawarray[4]})

 
    #It's an array of dictionaries with each numbered index as an entry.
    #You can query it like this:       
    #processed_data[1]['sen']
    #This way we can only read in the file once and use the data by tag as needed.
    
    #task 1
    task_1 = []
    for line in processed_data:
        task_1.append((line["sen"],line["genre"]))
    #Task_1 is now an array of tuples, [0] is the string, [1] is the genre
    
    #task 2
    task_2 = []
    for line in processed_data:
        task_2.append((line["sen"],line["affect"]))
    #Task_2 is now an array of tuples, [0] is the string, [1] is the affect tag
    
    #task3
    task_3 = []
    for line in processed_data:
        #only genre_a lines have action tags
        if(line["genre"]== "GENRE_A"):
            task_3.append((line["sen"],line["event"]))
    #Task_3 is now an array of tuples, [0] is the string, [1] is the event tag

    return task_1, task_2, task_3, processed_data

#BASELINE METRICS: MAJORITY CLASS LABELS
#task1 baseline
#counta = 0
#countb = 0
#for line in task_1:
#    if(line[1]=="GENRE_A"):
#        counta += 1
#    else:
#        countb += 1
#majority_class1 = max(counta,countb)   
#baseline1 = (majority_class1/len(task_1))    
##GENRE_B is the majority class, our baseline is 0.500780031201248 which is basically %50
#
##task2 baseline
#count_pos = 0
#count_neu = 0
#count_neg = 0
#for line in task_2:
#    if(line[1]=="POSITIVE"):
#        count_pos += 1
#    elif(line[1]=="NEUTRAL"):
#        count_neu += 1
#    elif(line[1]=="NEGATIVE"):
#        count_neg += 1
#majority_class2 = max(count_pos,count_neu,count_neg)
#baseline2 = (majority_class2/len(task_2))
##NEGATIVE is our majority class, our basline is 0.5, a dead %50
#
##task3 baseline
##initialize dicitonary to keep a count of each label
#counts3 = {}
#for line in task_3:
#    #if the label doesn't exist in the dictionary, make an entry with value of 1 for first sight
#    if not line[1] in counts3: 
#        counts3[line[1]]=1
#    #if the label already exists, increment by 1
#    else:
#        counts3[line[1]] += 1
#baseline3 = (counts3["ATTENDING_EVENT"]/len(task_3))
#GOING_TO_PLACES, LEGAL_ISSUE and ATTENDING_EVENT are tied at 160 for the 
#majority class label. I'm not sure how to deal with this. 
#my proposed baseline is %12.5. If we just take the first majority label
#alphabetically, it's ATTENDING_EVENT, which has a baseline of 0.125


