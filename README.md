# CipherWen

CipherWen 是一个用于加密文章和问答对，同时支持将密文伪装成类二维码图片的Python程序。

## 部署与使用

可以通过以下步骤部署CipherWen：

1. 确保已安装 Python（建议使用 Python 3.x 版本）。
2. 拉取项目到本地
3. 在命令行中使用以下命令安装所需的依赖项：
```shell
pip install -r requirement.txt
```
### 可执行文件说明
如果您是 windows 用户，没有浏览项目代码需求 可以前往 [下载页面](https://github.com/aoguai/CipherWen/releases) 下载 解压后得到

## 配置与使用教程
请到 [wiki](https://github.com/aoguai/CipherWen/wiki) 查看具体配置与使用教程

## 程序说明

程序运行流程如下：

创建一个`CipherWen`对象并进行初始化：

```python
cipher_wen = CipherWen(articles_path='articles.txt', config_path='config.ini', article_separator="============", qa_separator="------------")
```

- `articles_path`：文章数据文件路径，默认为'articles.txt'。
- `config_path`：配置文件路径，默认为'config.ini'。
- `article_separator`：文章分隔符，默认为"============"。
- `qa_separator`：问答分隔符，默认为"------------"。

接下来，可以使用以下方法来处理文章数据：

### 打印文章数据

```python
cipher_wen.print_articles()
```

该方法将打印所有文章的内容以及对应的问题和答案。

### 打印密文数据

```python
cipher_wen.print_cipher_articles()
```

该方法将打印所有文章的密文以及对应的问题和答案的密文。

### 返回以密文开头的文章数据的字符串

```python
cipher_wen.print_articles_with_cipher_start()
```

该方法将返回以密文开头的文章数据的字符串。

### 进行加密操作

```python
cipher_wen.cipher(output_path=None, char_colors=None, horn_image_path=None, background_color=None, background_image_path=None)
```

该方法将对文章和问题的内容进行加密操作。

- `output_path`：图片保存路径，默认为None。
- `char_colors`：字符和颜色的映射字典，默认为None。
- `horn_image_path`：外部方块图片路径，默认为None。
- `background_color`：新图像的背景颜色，默认为None。
- `background_image_path`：新图像的背景图片路径，默认为None。

加密成功后，将显示加密密文。

如果选择将密文转换为三进制，并且选择伪装成二维码，则需要提供相应的参数。

伪装成功后，将保存生成的图片，并显示保存路径。

## 演示

![1](https://github.com/aoguai/CipherWen/blob/main/img/test.png)

## 注意事项

- 加密操作仅适用于具有可加密内容的文章和问题。
- 请确保提供正确的文件路径和配置文件。
- 请按照指定格式提供文章数据文件。

以上是使用CipherWen进行文章和问题加密的基本方法和注意事项。

您可以根据自己的需求进行定制和扩展。祝您使用愉快！

## 参考

程序的加密方式参考了这篇文章：
[你见过最高级的作假方式有哪些？ - 躺平理论V的回答 - 知乎](https://www.zhihu.com/question/542376923/answer/2575600675)

## 授权许可

此存储库遵循 [MIT](https://github.com/aoguai/CipherWen/blob/master/LICENSE) 开源协议，请务必理解。

我们严禁所有通过本程序违反任何国家法律的行为，请在法律范围内使用本程序。

默认情况下，使用此项目将被视为您同意我们的规则。请务必遵守道德和法律标准。

如果您不遵守，您将对后果负责，作者将不承担任何责任！