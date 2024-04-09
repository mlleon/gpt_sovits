# 可以在任意地方跨目录调用get_tts_wav()
"""
# ===关于推理文本的语种 参考===
# 在config和调用get_tts_wav时，对于prompt_language和text_language参数
    "all_zh"    #全部按中文识别
    "en"        #全部按英文识别#######不变
    "all_ja"    #全部按日文识别
    "zh"        #按中英混合识别####不变
    "ja"        #按日英混合识别####不变
    "auto"      #多语种混合，启动切分识别语种
}
"""
"""
def get_tts_wav(
    text: str,      # 要转换为语音的文本。get_tts_wav()内部会对文本按标点自动切割。
    text_language: str = "en", # 推理出的语音语言
    wav_savepath: str = "temp/output.wav" # 推理结果存放的路径与文件名称。会得到一个完整的wav
    ==其他次要参数==
    how_to_cut: str = "凑四句一切", # 切割推理文本的方法，一共有5种。
            # 推荐"凑四句一切"和"按标点符号切"。"按标点符号切"语速最慢,推理最准确
            # "凑四句一切","凑50字一切","按中文句号。切","按英文句号.切","按标点符号切"
    top_k: int = 20,
    top_p: float = 0.6,
    temperature: float = 0.6,
            # 关于上面三个参数 https://github.com/RVC-Boss/GPT-SoVITS/pull/457
    ref_free: bool = False  # 不输入参考音频内对应文本，进行推理。默认关闭
) -> None
"""

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
