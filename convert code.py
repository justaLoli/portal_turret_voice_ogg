from pydub import AudioSegment
import os

def convertmain(fn:str):

    def convert_wav_to_opus(input_wav_file, output_ogg_file):
        # Load the wav file
        sound = AudioSegment.from_wav(input_wav_file)

        # Convert to opus format
        sound.export(output_ogg_file, format="opus")

    # 输入wav文件名和输出ogg文件名
    input_wav_file = f"./wav/{fn}.wav"
    output_ogg_file = f"./ogg/{fn}.ogg"

    # 调用函数进行转换
    convert_wav_to_opus(input_wav_file, output_ogg_file)

fs = os.listdir("./wav/")
fs = [i[:-4] for i in fs]
# print(fs)

for i in fs:
    print(f"current: {i}")
    convertmain(i)

print("转换完成，主人！")
