# IM-over-Emai
IM over Email with encryption

## 项目详细报告
[Finial report](./Report)

## 准备环境  
* Python3
* rsa  
* cryptography  
* imapy  
* smtplib  
* PyQt5  

## 运行说明  
运行UI下的main.py即可  

## 注意事项  
登陆用户名是邮箱地址，密码是允许imapy登陆SMTP服务器的密码，比如163邮箱的授权码，不一定是邮箱客户端的登陆密码。新用户登陆时会生成新的公钥和私钥，以及这个用户的数据库。数据库，私钥（用登陆密码加密）存在本地，公钥上传到服务器，如果服务器上已经存在这个用户的公钥则会被顶替掉，所以要接受邮件一定要保证自己现在的私钥和服务器上的公钥匹配。  
登陆已有用户，一开始不会显示记录，任意点击一个对话就可以显示出数据库中聊天记录  
登陆邮箱，可以看到这个应用发送接受的消息和附件都是被加密过的  

## 如何测试
例如用邮箱A，B测试：  
### 第一次测试以及收发消息
>1. 检查并先删除项目下的A，B用户文件夹（如果存在)
>2. 检查并删除Main下的main.db中A,B的记录（否则应用会认为A，B时老用户而造成异常）
>3. 登陆A邮箱（SMTP服务密码，如163邮箱的授权码，不是客户端密码）
>4. 登陆B邮箱，这样保证了服务器上存储了最新的A，B的公钥，与本地匹配
>5. 运行两次UI下的main.py,分别登陆邮箱A，B  
>6. A界面，点击add contact 填入B的邮箱和你想要的名字  
>7. A界面，点击creat group 勾选刚才添加的A，并*命名群聊名称，不能有相同的群聊名称*  
>8. 点击左侧的对话，发送消息并点击send，文本框中的文字过一小段会消失（代表发送成功）  
>9. 等待一会，会发现A，B两个界面出现刚才A发送的消息并且B会自动创建一个对话（但是不会添加联系人）  
### 扩展功能的测试    
#### 1.群聊  
>1. 点击creat group 勾选多个联系人，其余相同  
#### 2.发送图片或附件  
>1. 发送文本框 send 按钮左上，选择一个文件（图片），点击确定并且发送  
>2. 登陆任意收信人账户（可能是群聊），等待一会检查该账户文件夹下FileRecv文件夹，收到的附件会存放在此  
#### 3.block unblock联系人  
>1. 双击任意会话，会弹出一个显示这个群聊所有成员的对话框  
>2. 右击想要屏蔽的邮箱地址，点击block
>3. 点击ok返回，再次单机此对话，发现该用户的消息不再显示  
>4. 再次双击此对话，右击刚才屏蔽的邮箱地址，点击unblock  
>5. 点击ok返回，再次单机此对话，发现该用户的消息重新显示  
## 测试邮箱提供  
这些邮箱是设置好的，可以直接使用  
本应用用 smtp password 登陆，直接登陆邮箱用login password登陆  
可能有很多人同时使用这些邮箱测试，请确保按照说明进行  
user_config = {  
        "account": "gywang97@163.com",  
        "smtp password": "1207wang",  
        "login password": "wang1207",  
        "imap_server": "imap.163.com",  
        "imap_port": 993,  
        "smtp_server": "smtp.163.com",  
        "smtp_port": 25  
    }  
    
user_config = {  
        "account": "gywang97_2@163.com",  
        "smtp password": "1207wang",  
        "login password": "wang1207",  
        "imap_server": "imap.163.com",  
        "imap_port": 993,  
        "smtp_server": "smtp.163.com",  
        "smtp_port": 25  
    }   
    
user_config = {  
        "account": "m13751098406_2@163.com",  
        "smtp password": "m1234567",  
        "login password": "m13751098406"  
        "imap_server": "imap.163.com",  
        "imap_port": 993,  
        "smtp_server": "smtp.163.com",  
        "smtp_port": 25  
    }  
    
user_config = {  
        "account": "pengym_111@163.com",  
        "smtp password": "hvwoTxJndBEi8B4G",  
        "login password":"zSuKvfnUuqr5pUj",  
        "imap_server": "imap.163.com",  
        "imap_port": 993,  
        "smtp_server": "smtp.163.com",  
        "smtp_port": 25  
   }  
## 联系我们：  
有任何问题请发送至下面邮箱：
[11510050@mail.sustc.edu.cn](11510050@mail.sustc.edu.cn)

[11510035@mail.sustc.edu.cn](11510035@mail.sustc.edu.cn)
