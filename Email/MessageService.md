# MessageServer使用说明  
## 1.data structure: 
### 1.1 e-mail  
 `{'flags': ['seen'], 'to': '"', 'subject': 're:辣鸡，Project 做完了吗?', 'cc': [], 'text': [{'text': '学业繁忙，告辞 \r\n\r\n\r\n------------------ 原始邮件 ------------------\r\n发件人: "pengym_111" <pengym_111@163.com>;\r\n发送时间: 2017年12月13日(星期三) 20:18\r\n收件人: "1048217874" <1048217874@qq.com>;\r\n主题: 辣鸡，Project 做完了吗?\r\n\r\n\r\n\r\nhhhhh', 'text_normalized': '学业繁忙，告辞 ------------------ 原始邮件 ------------------ 发件人: "pengym_111" <pengym_111@163.com>; 发送时间: 2017年12月13日(星期三) 20:18 收件人: "1048217874" <1048217874@qq.com>; 主题: 辣鸡，Project 做完了吗? hhhhh', 'links': []}], 'html': ['学业繁忙，告辞\r<br><br/><br/>------------------ 原始邮件 ------------------<br/><div style="font-size: 12px; background: none repeat scroll 0% rgb(239, 239, 239); padding: 8px;"><div id="menu_sender"><b>发件人:</b>&nbsp;"pengym_111" &lt;pengym_111@163.com&gt;;</div><div><b>发送时间:</b>&nbsp;2017年12月13日(星期三) 20:18</div><div><b>收件人:</b>&nbsp;"1048217874" &lt;1048217874@qq.com&gt;;</div><div><b>主题:</b>&nbsp;辣鸡，Project 做完了吗?</div></div><br/><br/>hhhhh<br  />'], 'headers': {'received': ['from qq.com (unknown [127.0.0.1])\r\n\tby smtp.qq.com (ESMTP) with SMTP\r\n\tid ; Wed, 13 Dec 2017 20:20:12 +0800 (CST)'], 'dkim-signature': ['v=1; a=rsa-sha256; c=relaxed/relaxed; d=qq.com; s=s201512;\r\n\tt=1513167613; bh=4a2itk5RIB/mLIKHbmf2Kfmxw8yG/jE4UHgudvEYEmo=;\r\n\th=From:To:Subject:Mime-Version:Content-Type:Content-Transfer-Encoding:Date:Message-ID;\r\n\tb=LwbvkDnQw7Uczp2JjKu70L0DYZGgqobFTPffX67ng78wghn1CADae/orZZCnuV3jB\r\n\t hC6Ky/Fu2hMqH1iDLbiPNm4wqCTXdKl/MPB18yvlXWlnO18E06xPqImtiFEDIYsr7Z\r\n\t x1cKdtAnLUUoPlJzLeLe+sLU6IsqErPyi0OCB9wM='], 'x-qq-mid': ['mb21t1513167612t7302471'], 'x-qq-ssf': ['0001000000000090F1100F00000000Z'], 'from': ['"=?utf-8?B?UGVuZ1lN?=" <13421022906@qq.com>'], 'to': ['"=?utf-8?B?cGVuZ3ltXzExMQ==?=" <pengym_111@163.com>'], 'subject': ['=?utf-8?B?cmU66L6j6bih77yMUHJvamVjdCDlgZrlrozkuoY=?=\r\n =?utf-8?B?5ZCXPw==?='], 'mime-version': ['1.0'], 'content-type': ['multipart/alternative;\r\n\tboundary="----=_NextPart_5A311AFC_0D2BA600_7BC73190"'], 'content-transfer-encoding': ['8Bit'], 'date': ['Wed, 13 Dec 2017 20:20:12 +0800'], 'x-priority': ['3'], 'message-id': ['<tencent_5EC10F6744CDEEEA28BF7A2B90B6CDE8EF05@qq.com>'], 'x-qq-mime': ['TCMime 1.0 by Tencent'], 'x-mailer': ['QQMail 2.x'], 'x-qq-mailer': ['QQMail 2.x'], 'x-qq-sendsize': ['520'], 'feedback-id': ['mb:qq.com:bgweb:bgweb156'], 'x-cm-transid': ['NcCowAA3++T9GjFaKVz+Cg--.65485S3'], 'authentication-results': ['mx3; spf=pass smtp.mail=13421022906@qq.com; dk\r\n\tim=pass header.i=@qq.com'], 'x-coremail-antispam': ['1Uf129KBjDUn29KB7ZKAUJUUUUU529EdanIXcx71UUUUU7v73\r\n\tVFW2AGmfu7bjvjm3AaLaJ3UbIYCTnIWIevJa73UjIFyTuYvjxU2J3vUUUUU']}, 'attachments': [], 'from_whom': '"PengYM"', 'from_email': '13421022906@qq.com', 'from': '"PengYM" <13421022906@qq.com>', 'date': 'Wed, 13 Dec 2017 20:20:12 +0800'}`  
 以上是一封邮件的实例，每个邮件是一个字典，实际中方法返回的一般是由许多个这样的邮件组成的list  
 ###1.2  user_config:  
 示例 为一个字典  
 ``user_config = {
        "account": "pengym_111@163.com",
        "password": "hvwoTxJndBEi8B4G",
        "imap_server": "imap.163.com",
        "imap_port": 993,
        "smtp_server": "smtp.163.com",
        "smtp_port": 25
    }``  
 ###1.3 构造方法  
 这个类通过一个user_config 实例化，会包含这个用户的私钥,后文以user指代。这个user就是当前正在使用这个应用的用户
 ## 2. 方法说明  
>1 `load_privkey(self, key_path)`  
key_path 是存储私钥的文件的路径，这个方法还没有完善，这个方法会得到rsa.PrivateKey对象  
  
>2 `_getuuid(self, accounts)`  
accounts 是收件方邮箱的一个list 比如：``['11510050@mail.sustc.edu.cn','wanggy97@gmail.com']`
这个方法会将user的用户名和这些邮箱地址作为种子，生成一个uuid，这样保证了包含同样的人的一个会话只会有一个uuid与之对应，相当于一个hash函数最终返回一个str类型的uuid  

>3 `send_message(self, receivers, message, attachments_path)`  
这个方法用来给receivers发送邮件，receivers 形如`['11510050@mail.sustc.edu.cn','wanggy97@gmail.com']`  
message就是一个str类型的文本，默认utf-8编码，会自动加密并且发送  
attachments_path 是附件的路径，现在附件不会被加密 
 
>4 `get_message(self, folder)`  
folder 是一个文件夹，比如INBOX, 已发送，垃圾箱 等。此方法会返回所有此folder下的mail，以一个列表的形式返回。  

>5 ``get_unseen_message(self, folder):``  
返回所有此folder下的未读邮件  

>6 `get_unanswered_message(self, folder)`  
返回所有此folder下的未回复邮件  

>7 `get_all_conversion(self, accounts):`  
返回所有收信箱和已发送信箱中与accounts的会话的所有邮件，这是通过uuid过滤出来的

>8 `get_unseen(self, accounts)`
 返回所有收信箱中与accounts的会话的所有未读邮件，这是通过uuid过滤出来的

>9 `get_sent(self, accounts)`  
 返回所有已发送中与accounts的会话的所有已发送邮件，这是通过uuid过滤出来的

*提示：返回的所有邮件都是以list形式返回的，里面的每一个元素形如开头交代的字典*