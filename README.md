## SnapBot

## Member

### Robot && AI Software Developer
[최찬역(Chanyeok Choi)](https://github.com/Angledsugar), [김정한(Jeonghan Kim)](https://github.com/Kim-JeongHan), [남윤재(Yunjea Name)](https://github.com/ujma1234)

### Robot Hardware Developer
이왕건(Wanggeon Lee)

## Abstract
In the modern world, the creation of personal digital images has become increasingly important with the rapid development of social media platforms. Photography, especially selfies, is at the center of this shift. A great selfie can strengthen a person's digital identity and increase their influence on social media. In this context, choosing the right pose, lighting, and camera angle to get the best selfie of your life has become an important factor. However, getting the perfect combination of these elements requires specialized knowledge and skills, and hiring a photo studio and a professional photographer can be costly and difficult to schedule. Therefore, innovative methods are needed to fulfill this need. The goal of this research is to develop a photography studio automation system using robotic arms and AI to solve these problems. The robotic arm enables precise camera movement and angle adjustment, while the AI-based pose recommendation system can recommend optimal poses based on individual characteristics and situations. The system provides users with the convenience of taking the best selfie whenever they need it, which can make personal digital image creation easier and more effective. By using artificial intelligence technology to combine robot arm control, human recognition, understanding of user's personality, and recommendation of suitable poses and backgrounds, it presents a new paradigm for providing personalized photography services according to individual needs. This provides a means for each user to effectively express their own story, which will contribute to establishing a new way of personal expression in the digital age.

## System Architecture



## AI
### Human perception

video picture


### GAN && image enhancing





### How to run
#### install

```
git clone --recurse-submodules https://github.com/Plan-Real/Snapbot.git
```

Download the Isaac Gym Preview 4 release from the [website](https://developer.nvidia.com/isaac-gym), then follow the installation instructions in the documentation. We highly recommend using a conda environment to simplify set up.

you have to download nvidia issac-gym in this repository.
please, check your [.env](https://github.com/Plan-Real/Snapbot/blob/develop/.env) file when you install the isaac gym.

#### Run

First, To run our program, you should prepare the computer equipped with a GPU and UR.


'''
$ docker compose build dev
$ docker compose run dev
'''

if you can't run this docker file, you can fix the error by following [ROS_dev_template](https://github.com/Kim-JeongHan/ROS_dev_template) instruction.
