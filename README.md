1. devision是分开爬取下面4个大类的产品详情url
    apparel: 10
    Textiles & Leather Products: 8
    Fashion: 6
    Timepieces: 4

2. ali_contact.py
    爬取联系方式等信息

3. 注意
    一定要安装Firefox；爬联系方式时，第一个需要输入密码，仅第一次
    phone_url 会有过期，要隔几天换一次。换的标准是发现很多爬不了联系方式，就中断程序，更换phone_url

4. 思想
    为了防止中间意外事件导致程序中断 ，数据丢失，采取措施是每爬一个就写人硬盘。
    写文件是追加形式，不用担心覆盖。而且才用了断点续爬功能。第二次运行，不会爬之前爬过的url。
    devision_contact/make_txt  这个目录的功能就是爬数据存硬盘
    devision_contact/make_csv  这个目录的功能就是把根据txt文件内容生成csv
