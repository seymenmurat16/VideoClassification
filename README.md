# CLASSIFICATION OF SPORT NEWS WITH DEEPLEARNING METHODS

A system has been designed and implemented to classify sports news in news programs broadcasted on television channels according to their content with deep learning methods. The Convolutional Neural Network and Long - Short Term Memory were used as deep learning methods.
    
The project consists of several sub-steps. At the end of the project, video types were predicted by using videos in "Unsegmented Sports News" data set. At the beginning of the project, data set scanning was performed to use in training and test operations. The data sets, which are the type of sports on the internet, were examined and a suitable data set was selected and used throughout the project.\par

The videos in the Unsegmented Sports News data set include anchor parts as well as sports news. 
Prior to the classification of sports types, the anchor partitions in the videos were removed and the classification process was made only with videos of sports news. The face detection method was used to remove the anchor from the video and the part where the anchor's face was detected was removed from the video. The process of removing the anchor consists of several steps. In the first stage, the key-frames of each video were extracted. The histogram difference between consecutive frame pairs was used for key-frame detection. 64-bin method was used to construct the frame histogram. After the key-frames were extracted for each video, the system was trained to recognize the anchor. Many pictures of the anchor are required for training. The anchor is in the first 5 seconds of news videos. For this reason, the frames in the first 5 seconds of each video were recorded and the image data set of the anchor was created. In the next step, the training process was started for face recognition. Different algorithms have been tried for face recognition. Experiments have been conducted using 3 different algorithms including Eigenfaces, Fisherfaces and Local Binary Patterns Histograms. When the results were checked, it was found that the most successful algorithm was LBPH. By looking at the key-frames of each video, it was determined whether the anchor was present and the parts where the anchor was detected were removed from the videos. \par

After the videos without the anchor were obtained, the classification of the videos started. As a result of the research, it was seen that different methods were tried for video classification and one of the successful results was taken by CNN - LSTM method. Therefore, it was decided to use this method in the project. Firstly, 10 classes related to sports were selected from the UCF-101 data set and videos in these classes were divided into test and train videos. Each video is divided into frames and frames are recorded for use. For each video test or train video, class type, video name and number of frames are recorded in the csv file. After these operations, all the features of the videos were extracted using CNN and these features were recorded. Recorded features were used by LSTM. The resulting weights were recorded in the hdf5 file type. As a result of these trainings, a success rate of \%94 was achieved.\par

After the experiment was successful, a new training process was started to determine the class in news videos. Since the sports images in the news videos are different from the images found in the UCF-101, a new data set has been created using youtube videos. The news videos are divided into 36-frame pieces, as news videos have different lengths and include more than one type of sports in a news video. For each part, the system made the class type predict and the predicted classes were overwritten by the video and an output video was created.\par

When the results are checked for all videos, the system is able to make incorrect estimations due to class estimation once every 3 seconds, but when the system is evaluated in general terms, it is seen that sports types are estimated with a very high success rate.\par

### Face Recognation

<img src="https://github.com/seymenmurat16/VideoClassification/blob/master/0.PNG"/>

### Video Classification

<img src="https://github.com/seymenmurat16/VideoClassification/blob/master/1.PNG"/>
<img src="https://github.com/seymenmurat16/VideoClassification/blob/master/2.PNG"/>
<img src="https://github.com/seymenmurat16/VideoClassification/blob/master/3.PNG"/>
