import os
import configparser


class Config:
    def __init__(self, config_path, article_separator, qa_separator):
        """
        初始化配置对象。

        :param config_path: 配置文件路径
        :type config_path: str
        :param article_separator: 文章分隔符
        :type article_separator: str
        :param qa_separator: 问题答案分隔符
        :type qa_separator: str
        """

        self.config_path = config_path
        self.article_separator = article_separator
        self.qa_separator = qa_separator
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        """
        加载配置文件。
        """

        if os.path.exists(self.config_path):
            self.config.read(self.config_path, encoding='utf-8')
            self.article_separator = self.config.get('Separator', 'article')
            self.qa_separator = self.config.get('Separator', 'qa')
        else:
            self.save_config()

    def save_config(self):
        """
        保存配置文件。
        """

        self.config['Separator'] = {
            'article': self.article_separator,
            'qa': self.qa_separator
        }
        with open(self.config_path, 'w', encoding='utf-8') as config_file:
            self.config.write(config_file)
