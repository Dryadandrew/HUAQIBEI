# 需求文档
***
## 项目名称：针对初创企业财务评估与预测平台
***
### 项目背景：
&emsp;2020年4月2日，瑞幸咖啡发布公告，承认虚假交易22亿人民币，股价暴跌86%，一时间掀起轩然大波，财务造假话题引起社会各界广泛关注。市场监管体系宽松，企业造假成本低，是近年来财务造假发生的主要原因。自2014年首次提出“大众创业万众创新”至今，“双创”已经成为社会经济发展的主题词之一。根据天眼查专业版数据显示，全国小微企业数量达到8000万家，约占全国企业总数的70%左右，2017-2019年，全国每年新增小微企业数量都超过1000万家，每年得到天使投资的企业有上万甚至几十万家，客户量极大。根据我们对投资人的采访，90%以上的投资公司没有自动化获取被投资公司财务信息的工具并且对这种工具有很大需求。对于被投资的初创企业，几乎全都会将财务外包，并且无法获得业绩预测、以及同行业其他初创企业的数据信息。   
&emsp;为解决以上问题，本项目希望能够通过展示企业现金流的标化研究报告，借助python爬虫定期从银行端爬取企业的账单流水以及市场可获取的其他企业的大数据，结合（）方法得到关于该初创企业未来现金流量的预测报告，进一步利用机器学习的手段分析该初创企业存在现金流欺诈行为的可能性。在解决会计师事务所低效且易错的人工对账的同时，帮组初创企业管理自身现金流对账，为投资者和初创企业提供高效可信任的对接合作的可能，帮组投资人实现高效且低风险的投后管理，有效提高投资的产出质量与速度。   
&emsp;此外，企业签署协议提供银行流水权限给自动化数据平台即时掌握企业的银行流水，使企业很难造假，降低初创企业与投资人的信任成本。我们的项目定位于监督初创企业，通过建立一个保障创业公司与投资人之间财务透明的数据平台，使投资人对企业投资后，能够及时了解企业的现金支出；我们的数据平台还提供了自动对账功能、企业现金流预测功能和企业现金流风险欺诈检测功能，可以为投资人、初创企业、会计事务所等多种用户提供服务。
***
## 爬虫内容和数据分析部分
>通过爬取初创企业的银行流水数据，获取并预测企业未来现金流趋势，分析企业是否存在可能的财务欺诈行为。
***
### 企业信息
- 企业日常现金流
-	同行业企业日常现金流
- 同行业企业资产负债表
***
## 需求说明
***
### 一、数据需求：
1. 通过Web的形式表现出来平台的分析结果以及建议，投资者可以轻松访问Web并获取所需要的信息。 
2. 爬虫分为两部分
> 一部分以7天周期爬取授权给平台的所有企业的现金流
		另一部分，以一个季度周期爬取各企业所属行业的公司的季度报表
3. 平台支持登录访问，登录需要注册账户，分为企业/投资人账户两种
>投资人账户需要缴纳一定会费注册认证后使用全部功能（（75元/月；189元/季；360元/半年；1080元/两年）
>> 功能包括：
>> - 比对企业银行流水与日记账
>> - 所投资的企业的现金流预测
>> - 所投资的企业的财务欺诈风险分析

>企业账号在通过认证后能够入驻平台免费使用记账功能，在与投资人达成一致后可授予平台调取银行流水的权限
***
### 二、网站功能需求
> 平台网站主要分为三大板块：
1.	固定功能板块
用户在浏览网页时，无论浏览什么板块功能，都可以访问到此板块，此板块包括以下功能：
  - 1.1	网页左上角 主页 图标，可以直接返回主页板块
  - 1.2	网页右上角 登录 图标，可以直接进入登录界面，能够登录数据需求中提到的2中不同类型的账号。
  - 1.3	网页下方 网站基本信息 区域，包括以下内容：
    - 网站功能。网站功能的简单介绍
    - 合作站点。与我们合作的网站网址
    - 联系我们。我们的联系方式
2.	投资人板块
> 这个板块供投资人进行账目比对，现金流预测以及财务欺诈风险分析功能的使用。
  - 2.1	网页上方 点击上传 图标，可以分别传入企业银行流水以及企业日记账
  - 2.2	网页中间 确认提交 图标，可以进入账目比对阶段，等待后进入企业的账目比对与未来现金流预测报告页面：
    - 账目比对结果以及未比对成功的数据条目
    - 未来一个季度、半年、一年的现金流预测值

  - 2.3	网页下方 财务风险分析 图标，可以进入财务分析界面：
    - 2.3.1	网页上方 点击上传 图标，传入企业的资产负债表，现金流表以及利润表
    - 2.3.2	网页中间 确认提交 图标，可以进入企业财务风险分析阶段，等待后进入报告界面
    	- 输出企业财务造假概率值
      
3.	企业板块
> 这个板块供企业提供自己的银行流水数据
  - 3.1	网页上方 认证 图标，可以进入企业认证界面：
    - 3.1.1 网页上方 点击上传 图标，上传企业相关身份认证文件
    - 3.1.2	网页下方 授权投资人 图标，授予投资人企业的银行流水数据
  - 3.2	网页下方 点击上传 图标，上传企业的日记账文件
***
## 运行环境
任何能够访问网页的平台，如Windows操作系统、Linux操作系统、Android、IOS等。
***
## 开发限制
爬虫需要在腾讯云学生服务器上长期稳定运行，在无人看守的情况下不能中断。
所有内容需要在Web中访问，Web界面布局情况另行讨论。
