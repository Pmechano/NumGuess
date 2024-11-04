import random
import os

class RandomText: 
    def getRand(self,file_path="Text.txt"):
        try:
            # 打开文件并读取所有行
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # 确保文件不为空
            if lines:
                # 随机选择一行
                random_line = random.choice(lines).strip()
                return random_line
            else:
                return "文件是空的。"
        except FileNotFoundError:
            return "文件未找到。"
        except Exception as e:
            return f"发生错误：{e}"

if __name__ == "__main__":
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(current_dir, 'Text.txt')  # 构建文件路径
    file_path = "Text.txt"
    # random_line = getRand(file_path)
    print(random_line)
