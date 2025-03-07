# MarioKartLearn
A mario kart machine learning project.

# Requirements.
Docker must be installed. Then, to set up the docker container:
```
docker-compose down
docker rm -v -f $(docker ps -qa)
docker-compose build
docker-compose up -d
docker ps -a
```

# Data Collection
The dolphine emulator has been used for the Mario Kart Wii game.
To capture the training data, frame dumping has been enabled. 
See: https://wiki.dolphin-emu.org/index.php?title=Frame_Dumping.
To set the path from which frames are dumped, from the dolphine emulator:
    options > configuration > paths > dump path

# Pre-Processing
As the raw images are too large for real-time learning, they have been pre-processed by resizing and using grey-scalling. 
