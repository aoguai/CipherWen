import json
from Article import Article, QA
from Config import Config
from TextUtils import TextUtils


class CipherWen:
    def __init__(self, articles_path: str = 'articles.txt', config_path: str = 'config.ini',
                 article_separator: str = "============", qa_separator: str = "------------") -> None:
        """
        初始化 CipherWen 对象。

        :param articles_path: 文章数据文件路径，默认为 'articles.txt'
        :type articles_path: str
        :param config_path: 配置文件路径，默认为 'config.ini'
        :type config_path: str
        :param article_separator: 文章分隔符，默认为 "============"
        :type article_separator: str
        :param qa_separator: 问答分隔符，默认为 "------------"
        :type qa_separator: str
        """

        self.config = Config(config_path, article_separator, qa_separator)
        self.text_utils = TextUtils()
        self.articles = []

        # 从文件中读取文章数据
        with open(articles_path, 'r', encoding='utf-8') as data_file:
            data = data_file.read()
        # 以文章分隔符分割文章;
        article_texts = data.split(self.config.article_separator)

        # 遍历文章数据
        for article_data in article_texts:
            # 以问答分隔符分割问答对
            article_parts = article_data.split(self.config.qa_separator)
            article = Article(self.text_utils.extract_letters(article_parts[0].strip()))
            qas = article_parts[1].strip().split("\n")
            for i in range(0, len(qas), 2):
                question = self.text_utils.extract_letters(qas[i][2:].strip())
                answer = self.text_utils.extract_letters(qas[i + 1][2:].strip())
                qa = QA(question, answer)
                article.add_qa_pair(qa)
            self.articles.append(article)

    def print_articles(self) -> None:
        """
        打印文章数据。
        """

        for article in self.articles:
            print("文章：", article.text)
            for qa in article.qa_pairs:
                print("问题：", qa.question_text)
                print("答案：", qa.answer_text)
                print()
            print("----------------------------")

    def print_cipher_articles(self) -> None:
        """
        打印密文数据。
        """

        for article in self.articles:
            print("文章：", article.cipher_text)
            for qa in article.qa_pairs:
                print("问题：", qa.cipher_question_text)
                print("答案：", qa.cipher_answer_text)
                print()
            print("----------------------------")

    def print_articles_with_cipher_start(self) -> str:
        """
        返回以密文开头的文章数据的字符串。

        :return: 以密文开头的文章数据字符串
        :rtype: str
        """

        print_text = ''
        for article in self.articles:
            print_text = ''.join([print_text, article.cipher_text, '0',
                                  ''.join([qa_pairs.cipher_answer_text for qa_pairs in article.qa_pairs])])
        return print_text

    # 生成密文
    def cipher(self, output_path=None, char_colors=None, horn_image_path=None, background_color=None,
               background_image_path=None) -> None:
        """
        进行加密操作。
        """

        articles_text_data_dict = json.loads(self.text_utils.compare_texts([article.text for article in self.articles]))
        if len(articles_text_data_dict) <= 0:
            print("加密失败，该题目无法加密")
            exit(0)
        _, articles_cipher_texts = next(iter(articles_text_data_dict.items()))
        for i in range(len(self.articles)):
            self.articles[i].cipher_text = articles_cipher_texts[i]
            articles_qa_pairs_data_dict = json.loads(
                self.text_utils.compare_texts([qa_pairs.answer_text for qa_pairs in self.articles[i].qa_pairs], 1))
            if len(articles_qa_pairs_data_dict) <= 0:
                print("加密失败，该题目无法加密")
                exit(0)
            _, cipher_articles_qa_pairs_answer_texts = next(iter(articles_qa_pairs_data_dict.items()))
            for j in range(len(self.articles[i].qa_pairs)):
                self.articles[i].qa_pairs[j].cipher_answer_text = cipher_articles_qa_pairs_answer_texts[j]
        cipher_string = self.print_articles_with_cipher_start()
        if self.text_utils.get_input("加密成功，是否转成三进制(Y/N):"):
            base3_string = self.text_utils.string_to_base3(cipher_string)
            print("加密密文：", cipher_string)
            print("三进制密文：", base3_string)
            if self.text_utils.get_input("是否伪装成二维码(Y/N):"):
                if output_path is None:
                    output_path = input("请输入图片保存路径(默认output.png): ")
                if char_colors is None:
                    char_colors = input(
                        "请输入字符和颜色的映射字典（例如{'0': (0, 0, 0), '1': (128, 128, 128), '2': (255, 255, 255)}）: ")
                if horn_image_path is None:
                    horn_image_path = input("请输入外部方块图片路径(默认为img/horn.png): ")
                if background_color is None:
                    background_color = input("请输入新图像的背景颜色（默认为(255, 255, 255)）: ")
                if background_image_path is None:
                    background_image_path = input("请输入新图像的背景图片路径（默认为None）: ")

                # 将输入的字符串转换为相应的数据类型
                char_colors = eval(char_colors) if char_colors else None
                background_color = eval(background_color) if background_color else (255, 255, 255)
                background_image_path = background_image_path if background_image_path else None
                horn_image_path = horn_image_path if horn_image_path else None

                image_path = self.text_utils.base3_to_image(base3_string, output_path, char_colors, horn_image_path,
                                                            background_color, background_image_path)
                print(f'伪装成功，保存图片位于：{image_path}')
        else:
            print("加密密文：", cipher_string)
