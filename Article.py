class QA:
    def __init__(self, question_text: str, answer_text: str) -> None:
        """
        初始化问题答案对象。

        :param question_text: 问题文本
        :type question_text: str
        :param answer_text: 答案文本
        :type answer_text: str
        """

        self.question_text = question_text
        self.cipher_question_text = ''
        self.answer_text = answer_text
        self.cipher_answer_text = ''


class Article:
    def __init__(self, text: str) -> None:
        """
        初始化文章对象。

        :param text: 文章文本
        :type text: str
        """

        self.text = text
        self.cipher_text = ''
        self.qa_pairs = []

    def add_qa_pair(self, qa_pair: QA) -> None:
        """
        添加问题答案对到文章对象。

        :param qa_pair: 问题答案对对象
        :type qa_pair: QA
        """

        self.qa_pairs.append(qa_pair)
