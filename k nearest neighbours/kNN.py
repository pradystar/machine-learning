import sys
import math
import csv
import operator

def read_file(data):
    file=open(data)
    read=csv.reader(file)
    dataset=list()
    for example in read:
        dataset.append(example)      
    return dataset

def cal_distance(example, training_instance):
    distance=0
    for x in range(0,len(example)-1):
        distance+= pow((float(example[x]) - float(training_instance[x])), 2)
        # print(distance)
    return math.sqrt(distance)

def find_neighbour(example,training_list,k):
    dist_list=[]
    for i in range(0,len(training_list)):
        dist=cal_distance(example, training_list[i])
        '''store class of the training set and its distance from the test example'''
        dist_list.append((training_list[i][-1], dist))
    dist_list.sort(key=operator.itemgetter(1))
    # print(dist_list)
    neighbors=[]
    for j in range(k):
        # closet will be 1st,2nd,...upto k and class will be in [j][0]
        neighbors.append(dist_list[j][0])
    # print(neighbors)
    return neighbors

def get_class(neighbor):
    class_vote={}
    for x in neighbor:
        if x in class_vote:
            class_vote[x]+=1
        else:
            class_vote[x]=1
    # print(class_vote)
    return max(class_vote, key=lambda k: class_vote[k])
    
def main(args):
    train=args[1]
    test=args[2]
    k=int(args[3])
    training_list=read_file(train)
    test_list=read_file(test)
    hits=0
    for i in range(0,len(test_list)):
        # print(len(test_list[i]))
        neighbour=find_neighbour(test_list[i],training_list,k)
        example_class=get_class(neighbour)  
        # print(example_class,test_list[i][-1]) 
        if example_class==test_list[i][-1]:
            hits+=1
    # print('hits',hits)
    accuracy=(hits/len(test_list))*100
    print('Accuracy for',k,'is',accuracy)

main(sys.argv)