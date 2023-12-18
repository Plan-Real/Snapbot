## SnapBot

## Member

### Robot && AI Software Developer
[최찬역(Chanyeok Choi)](https://github.com/Angledsugar), [김정한(Jeonghan Kim)](https://github.com/Kim-JeongHan), [남윤재(Yunjea Name)](https://github.com/ujma1234)

### Robot Hardware Developer
이왕건(Wanggeon Lee)

## Abstract


You can watch the video of our project. Click here.
[![thumbnail](https://github.com/Plan-Real/Snapbot/assets/98142496/27023b42-f5d0-4ed7-a711-d1a5a00fed4c)](https://drive.google.com/file/d/13aQ0mCv9reuY-JInxXiSdqex67w7G5Ey/view?usp=drive_link)

### Manipulator Control
<img src="https://github.com/Plan-Real/Snapbot/assets/98142496/f2c28590-5a2b-4454-bc70-96c2c4ea1181" width="80%"/>


### Photography
|                         **AnimeGAN**                       | **selecting frame**                                          |  **printing image**                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
|  <img src="https://github.com/Plan-Real/Snapbot/assets/98142496/77f31169-ed0d-4bea-b66e-f01fe0013e6f" />     |     ![selecting frame](https://github.com/Plan-Real/Snapbot/assets/98142496/5e8ecf4f-98a3-4595-aa87-05c893b96846)   |  ![print photo](https://github.com/Plan-Real/Snapbot/assets/98142496/54a578f7-4e60-412c-a3fc-cc3be6d27c2f) |



## Web Server
If you are curious about the contents related to the web server, click this link.






### How to run
#### install

```
git clone --recurse-submodules https://github.com/Plan-Real/Snapbot.git
```

Download the Isaac Gym Preview 4 release from the [website](https://developer.nvidia.com/isaac-gym), then follow the installation instructions in the documentation. We highly recommend using a conda environment to simplify set up.

you have to download nvidia issac-gym in this repository.
please, check your [.env](https://github.com/Plan-Real/Snapbot/blob/develop/.env) file when you install the isaac gym.

#### Run

To run our program, you should prepare the computer equipped with a GPU and UR.

###### docker build
```
docker compose build dev
```
###### docker run
```
docker compose run dev
```

if you can't run this docker file, you can fix the error by following [ROS_dev_template](https://github.com/Kim-JeongHan/ROS_dev_template) instruction.
