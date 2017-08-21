## 1. devision是分开爬取下面4个大类的产品详情url

   - apparel: 10

   - Textiles & Leather Products: 8

   - Fashion: 6

   - Timepieces: 4

## 2. 思想

   为了防止突发事件导致程序中断，数据丢失，采取措施是每爬取一个就写入硬盘。
   写文件是追加形式。采用了断点续爬功能，第二次运行，不会爬之前爬过的url。

   devision_contact/make_txt：爬数据存硬盘。

   devision_contact/make_csv：根据txt文件内容生成csv。

## 3. 注意

   一定要安装Firefox；爬联系方式时，第一次需要输入密码。
