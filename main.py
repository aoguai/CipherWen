from CipherWen import CipherWen

print("———————欢迎使用，本程序免费请勿用于商业用途———————")
print("——————————————CipherWenV1.0————————————————")
print("项目地址：https://github.com/aoguai/CipherWen\n")
cw = CipherWen(articles_path=input("请输入文章数据:\n"))
cw.cipher()
