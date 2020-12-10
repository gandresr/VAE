import os
import numpy as np
import pickle

from PIL import Image

def vid_to_ndarray(fpath, shape):
    for root, dirs, files in os.walk(fpath):
        frames = []
        for name in sorted(files):
            if name.endswith(('.jpg',)):
                impath = os.path.join(root, name)
                img = np.array(Image.open(impath).convert('L'))
                frames.append(img[:shape[0],:shape[1]])
        pk_name = os.path.join(root, os.path.basename(root) + '.pkl')
        if frames:
            with open(pk_name, 'wb') as f:
                pickle.dump(np.array(frames), f)
            print(pk_name)

def get_batches(dataset_path, train = True, batch = 16):
    '''
    batch: batch size
    '''

    dtp = 'train' if train else 'test'
    fpath = os.path.join(dataset_path, dtp)
    dirs = os.listdir(fpath)
    N = len(dirs)
    N_batches = N // batch

    n = np.arange(N)
    nn = np.arange(N_batches) * batch

    for i in n:
        if i == N_batches - 1:
            idx = n[nn[i]:]
        else:
            idx = n[nn[i]:nn[i+1]]
        video_batch = []
        for folder in idx:
            with open(os.path.join(fpath, str(folder), str(folder) + '.pkl'), 'rb') as f:
                video_batch.append(pickle.load(f))
        yield np.array(video_batch)


vid_to_ndarray('videos_adobe240/original_high_fps_videos', shape=[32,32])