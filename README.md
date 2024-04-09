
## 项目描述

原始[GPT_SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)的效果体验和推理服务较大依赖于基于Gradio的webui界面，为了更方便地推理体验GPT_SoVITS效果，本项目将其推理部分提取分离出来.
## 模型设置


- 预训练模型设置
需要两个HF预训练模型，将其放在项目目录GPT_SoVITS_Inference/GPT_SoVITS/Pretrained_Models下
模型1名称：chinese-hubert-base， 模型2名称：chinese-roberta-wwm-ext-large

- 微调模型权重设置
将自己训练的GPT模型权重放在项目目录GPT_SoVITS_Inference/GPT_SoVITS/Finetune_Weights/GPT_weights下
将自己训练的SoVITS模型权重放在项目目录GPT_SoVITS_Inference/GPT_SoVITS/Finetune_Weights/SoVITS_weights下

## 安装依赖

推荐 Python>=3.9,<=3.10

```
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia

git clone https://github.com/X-D-Lab/GPT_SoVITS_Inference.git
cd GPT_SoVITS_Inference
pip install -r requirements.txt

sudo apt update
sudo apt install ffmpeg
```
如果您是windows使用者，请下载并将 [ffmpeg.exe](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/ffmpeg.exe) 和 [ffprobe.exe](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/ffprobe.exe) 放置在本项目的根目录下。


## 如何使用

详细内容可以参见[example.py](./example.py)

```Python

import os
import sys

project_root = os.path.abspath('.')
sys.path.append(project_root)


from get_tts_wav import GPT_SoVITS_TTS_inference

text = """but when the entire family,reunite once again his chair his bowl"""

inference = GPT_SoVITS_TTS_inference()

inference.get_tts_wav(text=text)

```
