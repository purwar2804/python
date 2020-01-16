
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in range(0,len(subjects)):
        for j in range(0,len(verbs)):
            for k in range(0,len(objects)):
	            s=subjects[i]+" "+verbs[j]+" "+objects[k]
	            sentence_list.append(s)
	
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
