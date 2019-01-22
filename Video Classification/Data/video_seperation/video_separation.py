import cv2
import os
import imageio

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir,"data")
for root, dirs, files in os.walk(data_dir):
    for filename in files:
        # Thumbs.db dosyası kendiliğinden oluşabiliyor ve hata verebiliyor o yüzden kontrol ediliyor ve değilse işlem yapılıyor
        if filename != "Thumbs.db":
            # videonun olduğunu dizin
            file = "data/" + filename
            # video ismi için videonun noktadan önceki kısım alınıyor
            parts = filename.split(".")
            filename = parts[0]
            # videoyu okunuyor
            reader = imageio.get_reader(file)
            fps = reader.get_meta_data()['fps']
            print(fps)
            video_chapter_name = 1
            if (fps > 30):
                each = 2
            if (fps <= 30):
                each = 1
            j = -1
            if (each==2):
                fps = int((fps/each))
            writer = imageio.get_writer("../test/z/" +filename + "_c" +str(video_chapter_name).zfill(2) + ".avi", fps=fps)
            for i, frame in enumerate(reader):
                if((i+1) % each == 0):
                    """ j -1 ise ilk kez girdiği anlaşılıyor"""
                    if (j==-1):
                        j = 0
                    writer.append_data(frame)
                    j = j+1
                if (j % 36 == 0):
                    j = -1
                    writer.close()
                    video_chapter_name = video_chapter_name + 1
                    writer = imageio.get_writer("../test/z/" + filename + "_c" + str(video_chapter_name).zfill(2) + ".avi", fps=fps)
            writer.close()




