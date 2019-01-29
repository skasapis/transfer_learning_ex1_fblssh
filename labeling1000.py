#labeling code
import os , json

which_one = "val"

if which_one == "test":
    #first piece of code to make the test labeling file
    label_names = []
    image_labels = []
    image_names = []
    i = 0
    for imgclass in os.listdir("C:/imagenet_1000/train"):
        label_names.append(imgclass)
        for image in os.listdir("C:/imagenet_1000/train/" + imgclass):
            image_labels.append(i)
            image_names.append("train/"+imgclass+"/"+image)
        i += 1

    data = {}
    data['label_names'] = label_names
    data['image_labels'] = image_labels
    data['image_names'] = image_names

    with open('dataaaa.json', 'w') as outfile:
        json.dump(data, outfile)

elif which_one == "val":
    #second piece of code to make the val labeling file (fixing the already given)
    with open('C:/Users/skasapis/Desktop/low-shot-shrink-hallucinate-master/base_classes_val_meta.json') as json_file:
        data = json.load(json_file)
        image_names = data["image_names"]
        i = 0
        for name in image_names:
            image_names[i] = "val/" + name[14:]
            i += 1
        with open('base_classes_val_meta.json', 'w') as outfile:
            json.dump(data, outfile)
            #print(image_names[i])

#print(len(label_names))
#print(len(image_labels))
#print(len(image_names))
