# Dog_Breed_Classification
Dog Breed Classification for 2021 Fall IIE4123 Deep Learning and its application lecture.

First of all the requirements for this project is summarized in 'requirements.txt'. Please go check that out.

We used Stanford Dogs Dataset. Download the dataset at http://vision.stanford.edu/aditya86/ImageNetDogs/
Create 'data' folder and unzip the 'images.tar' and 'annotation.tar' in 'data' folder.
Run 'dataset_rename.py' with 'python3 dataset_rename.py'.
This process will revise the folders' name under 'images' and 'annotation' folder. In addition it explicitly split the train data and test data. I splited based on 5 fold and I fixed the random seed to make sure that all team mates are on the same data.
