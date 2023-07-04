import re
import json
from typing import List


class TextUtils:
    @staticmethod
    def get_input(msg: str, default: str = 'Y') -> bool:
        """
        获取用户输入并返回布尔值。

        :param msg: 提示消息
        :type msg: str
        :param default: 默认值。默认为'Y'。
        :type default: str
        :return: 如果用户输入是 'Y'、'y'、'yes'、'YES'、'Yes' 或 '1'，返回 True，否则返回 False。
        :rtype: bool
        """

        r = input(msg)
        if not r:  # 如果用户没有输入任何内容
            r = default

        # 忽略大小写进行比较
        if r.lower() in ['y', 'yes', '1']:
            return True

        return False

    @staticmethod
    def extract_letters(text: str) -> str:
        """
        从文本中提取字母，并返回提取后的结果。

        :param text: 输入的文本
        :type text: str
        :return: 提取后的字母
        :rtype: str
        """

        letters_only = re.sub(r'[^a-zA-Z]', '', text)
        return letters_only

    @staticmethod
    def compare_texts(texts: List[str], start_length: int = 2) -> str:
        """
        比较文本列表中的段落，并返回不同的比较段及其位置。

        :param texts: 包含多个文本段落的列表
        :type texts: list[str]
        :param start_length: 比较段的起始长度，默认为2
        :type start_length: int
        :return: 不同的比较段及其位置的字典，格式为JSON字符串
        :rtype: str
        """

        result = {}  # 存储位置和比较段的字典
        min_length = min(len(text) for text in texts) + 1  # 获取最短文本的长度

        if start_length <= 0 or start_length > min_length:
            return json.dumps(result)
        else:
            # 从指定长度开始逐渐增加比较长度
            for length in range(start_length, min_length + 1):
                for k in range(len(texts[0]) - length + 1):
                    segment = texts[0][k:k + length]  # 获取当前比较段
                    other_list = [text[k:k + length].zfill(len(segment)) for text in texts[1:]]

                    if segment not in other_list and len(other_list) == len(set(other_list)):
                        other_list.insert(0, segment)
                        result[k] = other_list  # 存储位置和比较段文本
                        return json.dumps(result)  # 在第一次发现不同的比较段后返回结果

            return json.dumps(result)  # 如果未找到不同的比较段，返回空结果

    @staticmethod
    def char_to_digit(char: str) -> int:
        """
        将字符转换为对应的数字。
        如果字符是数字，则返回字符的整数形式。
        如果字符是字母，则返回字母的索引（A 对应 1，B 对应 2，依此类推）。

        :param char: 要转换的字符
        :type char: str
        :return: 转换后的数字
        :rtype: int
        """

        if char.isdigit():
            return int(char)
        else:
            return ord(char.upper()) - ord('A') + 1

    @staticmethod
    def decimal_to_base3(decimal: int) -> List[int]:
        """
        将十进制数转换为基数为3的数字列表。

        :param decimal: 十进制数
        :type decimal: int
        :return: 基数为3的数字列表
        :rtype: List[int]
        """

        base3_digits = []
        while decimal > 0:
            base3_digits.append(decimal % 3)
            decimal //= 3
        base3_digits.reverse()
        return base3_digits

    @staticmethod
    def string_to_base3(string: str) -> str:
        """
        将字符串转换为三进制的字符串。

        :param string: 输入字符串
        :type string: str
        :return: 转换后的三进制的字符串
        :rtype: str
        """

        base3_string = ""
        for char in string:
            decimal = TextUtils.char_to_digit(char)
            base3_digits = TextUtils.decimal_to_base3(decimal)
            base3_string += ''.join(str(digit) for digit in base3_digits).zfill(5)
        return base3_string

    @staticmethod
    def digit_to_char(digit: int) -> str:
        """
        将十进制整数转换为对应的字符。

        :param digit: 十进制整数
        :type digit: int
        :return: 转换后的字符
        :rtype: str
        """

        if isinstance(digit, int):
            return chr(ord('A') + digit - 1)
        else:
            return str(digit)

    @staticmethod
    def base3_to_decimal(base3_digits: str) -> int:
        """
        将三进制的数字字符串转换为十进制整数。

        :param base3_digits: 三进制的数字字符串
        :type base3_digits: str
        :return: 转换后的十进制数
        :rtype: int
        """

        decimal = 0
        power = len(base3_digits) - 1
        for digit in base3_digits:
            decimal += int(digit) * (3 ** power)
            power -= 1
        return decimal

    @staticmethod
    def base3_to_string(base3_string: str) -> str:
        """
        将三进制的字符串转换为普通字符串。

        :param base3_string: 三进制的字符串，只包含数字0、1和2。
        :type base3_string: str
        :return: 转换后的普通字符串。
        :rtype: str
        """

        string = ""
        i = 0
        while i < len(base3_string):
            base3_digits = base3_string[i:i + 5]
            decimal = TextUtils.base3_to_decimal(base3_digits)
            if decimal:
                char = TextUtils.digit_to_char(decimal)
            else:
                char = '0'
            string = ''.join([string, char])
            i += 5
        return string

    @staticmethod
    def base3_to_image(base3_string, output_path="output.png", char_colors=None, horn_image_path="img/horn.png",
                       background_color=(255, 255, 255), background_image_path=None):
        """
        将base3字符串转换为图像并保存到指定路径。

        :param base3_string: 要转换的base3字符串
        :type base3_string: str
        :param output_path: 图像输出路径，默认为"output.png"
        :type output_path: str
        :param char_colors: 字符和颜色的映射字典，例如 {'0': (0, 0, 0), '1': (128, 128, 128), '2': (255, 255, 255)}
        :type char_colors: dict
        :param horn_image_path: 外部方块图片路径，默认为"img/horn.png"
        :type horn_image_path: str
        :param background_color: 新图像的背景颜色，默认为(255, 255, 255)（白色）
        :type background_color: tuple
        :param background_image_path: 新图像的背景图片路径，默认为None（无背景图片）
        :type background_image_path: str
        :return: 保存的图像路径
        :rtype: str
        """

        import os
        import math
        from PIL import Image

        # 判断output_path是否为空
        if len(output_path) <= 0:
            output_path = "output.png"
        # 判断horn_image_path是否为空
        if horn_image_path is None:
            horn_image_path = "img/horn.png"

        # 检查output_path是否为目录
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path, 'output.png')
        else:
            # 检查output_path是否为图片路径
            if not output_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # 修改为.png后缀
                output_path = output_path + '.png'

        # 计算图像的边长
        side_length = math.isqrt(len(base3_string))
        side_length = side_length + 1 if side_length ** 2 < len(base3_string) ** 2 else side_length

        # 设置方框和像素大小
        box_size = 10  # 方框的大小
        pixel_size = box_size - 2  # 像素的大小，留出2个像素的间隔用于绘制方框

        # 计算图像的大小
        image_size = side_length * box_size

        # 判断background_color是否为空
        if len(background_color) != 3:
            background_color = (255, 255, 255)
        # 创建一个空白图像对象
        image = Image.new('RGB', (image_size, image_size), color=background_color)

        # 设置字符和颜色映射
        if char_colors is None or len(char_colors) <= 0:
            char_colors = {'0': (0, 0, 0), '1': (128, 128, 128), '2': (255, 255, 255)}

        # 设置像素颜色和方框
        for i, char in enumerate(base3_string):
            row = i // side_length
            col = i % side_length

            # 计算像素的位置和方框的位置
            pixel_x = col * box_size + 1
            pixel_y = row * box_size + 1
            box_x1 = col * box_size
            box_y1 = row * box_size
            box_x2 = box_x1 + box_size - 1
            box_y2 = box_y1 + box_size - 1

            color = char_colors.get(char, (255, 255, 255))  # 默认为白色

            # 绘制方框
            for x in range(box_x1, box_x2 + 1):
                image.putpixel((x, box_y1), (255, 255, 255))
                image.putpixel((x, box_y2), (255, 255, 255))
            for y in range(box_y1, box_y2 + 1):
                image.putpixel((box_x1, y), (255, 255, 255))
                image.putpixel((box_x2, y), (255, 255, 255))

            # 绘制像素
            for x in range(pixel_x, pixel_x + pixel_size):
                for y in range(pixel_y, pixel_y + pixel_size):
                    image.putpixel((x, y), color)

        # 加载外部方块图片
        horn_image = Image.open(horn_image_path)

        # 计算新图像的大小和位置
        new_image_size = image_size + 2 * horn_image.width
        new_image = Image.new('RGB', (new_image_size, new_image_size), color=background_color)

        # 添加外部方块图片
        if background_image_path is not None:
            background_image = Image.open(background_image_path)
            background_image = background_image.resize((new_image_size, new_image_size))
            new_image.paste(background_image, (0, 0))  # 作为背景图片

        new_image.paste(horn_image, (0, 0))  # 左上角
        new_image.paste(horn_image, (new_image_size - horn_image.width, 0))  # 右上角
        new_image.paste(horn_image, (0, new_image_size - horn_image.height))  # 左下角

        new_image.paste(image, (horn_image.width, horn_image.width))

        # 保存图像
        new_image.save(output_path)

        return output_path
