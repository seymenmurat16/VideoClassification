"""
Given a video path and a saved model (checkpoint), produce classification
predictions.

Note that if using a model that requires features to be extracted, those
features must be extracted first.

Note also that this is a rushed demo script to help a few people who have
requested it and so is quite "rough". :)
"""
from keras.models import load_model
from data_news import DataSet
import numpy as np
import glob
import cv2
import os
import imageio
os.environ["CUDA_VISIBLE_DEVICES"]="1"

def predict(data_type, seq_length, model, image_shape, video_name, class_limit):

    # Get the data and process it.
    if image_shape is None:
        data = DataSet(seq_length=seq_length, class_limit=class_limit)
    else:
        data = DataSet(seq_length=seq_length, image_shape=image_shape,
            class_limit=class_limit)
    
    # Extract the sample from the data.
    sample = data.get_frames_by_filename(video_name, data_type)

    # Predict!
    prediction = model.predict(np.expand_dims(sample, axis=0))
    # print(prediction)
    sport = data.print_predictions(np.squeeze(prediction, axis=0))
    return sport

def putText(frame,label):
    cv2.putText(frame, label[0], (15, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, label[1], (15, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, label[2], (15, 45), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    return frame

def main():
    # model can be one of lstm, lrcn, mlp, conv_3d, c3d.
    model = 'lstm'
    # Must be a weights file.
    saved_model = 'data/checkpoints/lstm-features.012-0.180.hdf5'
    # Sequence length must match the lengh used during training.
    seq_length = 36
    # Limit must match that used during training.
    class_limit = 9

    # Demo file. Must already be extracted & features generated (if model requires)
    # Do not include the extension.
    # Assumes it's in data/[train|test]/
    # It also must be part of the train/test data.
    # TODO Make this way more useful. It should take in the path to
    # an actual video file, extract frames, generate sequences, etc.
    video = 'tennis'
    video_class = "Z"
    videos = glob.glob(os.path.join('data', 'test', video_class, video + '_c*.avi'))

    # Chose images or features and image shape based on network.
    if model in ['conv_3d', 'c3d', 'lrcn']:
        data_type = 'images'
        image_shape = (80, 80, 3)
    elif model in ['lstm', 'mlp']:
        data_type = 'features'
        image_shape = None
    else:
        raise ValueError("Invalid model. See train.py for options.")

    """ Videonun kaç fps olacağını öğrenmek için ilk videodaki fps değeri alınıyor """
    reader = imageio.get_reader(videos[0])
    fps = reader.get_meta_data()['fps']
    # Video yazıcıyı oluşturuluyor
    writer = imageio.get_writer(video + ".mp4", fps=fps)
    reader.close()
    # Tüm ayırılmış videoları geziliyor
    model = load_model(saved_model)
    for item in videos:
        # İtemi ayırıp sadece video ismi alınıyor
        news = item.split("\\")
        news_name = news[3]
        parts = news_name.split(".")
        video_name = parts[0]
        # Tahmin yapılıyor
        predict_label = predict(data_type, seq_length, model, image_shape, video_name, class_limit)
        # Tahmin edilen videoya tahmin sonucunu yazdırılıyor
        reader = imageio.get_reader(item)
        for i, frame in enumerate(reader):
            frame = putText(frame,predict_label)
            writer.append_data(frame)
        reader.close()
    writer.close()
if __name__ == '__main__':
    main()
