''' 
該腳本功能:
在終端機執行coding_lesson.py <偵測的文檔>
return該文件的: 行數,字數,字母數 
'''
from sys import argv
# argv 會 返回 終端機 所輸入的內容
print(f"{argv}")
print(f"資料長度{len(argv)}")
print("<---------------------------------->")

# 如果資料長度小於2
if len(argv) < 2:
    print("請提供文件名。")
else:
    # 開啟文檔
    file = open(argv[1])
    # 文檔內容
    lines = file.read()
    # 分割的依據為"\n"
    lines = lines.split("\n")

    # 計算字元數
    letter_count = 0
    # 算字數
    word_count = 0
    for line in lines:
        # 分割的依據為" "
        words = line.split(" ")
        word_count += len(words)
        letter_count += len(line)

    # 計算行數 = 長度 - 1(空格)
    line_count = len(lines)

    # 輸出
    print(lines)
    print(type(lines))
    print(f"line count is {line_count}")
    print(f"word count is {word_count}")
    print(f"letter count is {letter_count}")
