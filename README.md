![TouTiaoRobot](accessory/logo.png) 

使用今日头条web版自动发布机器人，涵盖账密登陆、滑动验证、头条号内容操作。支持定时器任务，又可以作为头条新闻文章爬虫，采集相关资讯存储。
默认使用 **MongoDB** 数据库进行存储

## 更新历史
* 2020/05/13 开始编写程序

----------
## 目录
- [项目结构](#h2-id1h2)
- [使用文档](#h2-id2h2)
  * [安装使用环境(**requirements.txt**)](#h3-id200-requirementstxth3)
  * [安装MongoDB数据库](#h3-id211-mongodbh3)
  * [chromedriver版本下载](#h3-id222-chromedriverh3)
  * [账密登陆](#h3-id233-h3)
  * [头条搜索(关键词综合、视频、用户搜索)](#h3-id244-h3)
  * [ 🚀 新闻爬取(45类新闻获取)](#h3-id255-h3)
  * [ 🚀 头条用户信息采集（无需登录）](#h3-id266-h3)
    * [x] [获取用户头像、id、粉丝数、关注数](#使用文档)
    * [x] [获取用户发布的所有/指定数量 的文章、视频、微头条](#使用文档)
    * [x] [获取用户关注列表的所有/指定数量 的头条账户的信息](#使用文档)
    * [x] [获取用户的粉丝列表 的头条账户信息](#使用文档)
  * [ 🚀 用户链式采集](#使用文档)
  * [ 🚀 登陆用户操作（需登录）](#使用文档)
     * [x] [获取账户基本信息、状态](#使用文档)
     * [x] [发微头条（图文皆可）](#使用文档)
     * [x] [发布头条号图文作品](#使用文档)
     * [x] [获取某个头条媒体的可见评论](#使用文档)
     * [x] [获取拉黑用户列表](#使用文档)
     * [x] [获取头条号订阅者列表](#使用文档)
     * [x] [获取我的收藏列表](#使用文档)
     * [x] [获取账户悟空问答草稿列表](#使用文档)
     * [x] [获取发布的所有/指定数量 的微头条、转发](#使用文档)
     * [x] [获取发布的所有/指定数量 的视频](#使用文档)
     * [x] [获取发布的所有/指定数量 的图文作品](#使用文档)
     * [x] [获取互动粉丝排行榜](#使用文档)
     * [x] [获取头条号素材库图片](#使用文档)
     * [x] [获取账户登陆操作日志](#使用文档)
     * [x] [获取账户敏感操作日志](#使用文档)
     * [x] [上传图片至头条号素材库](#使用文档)
  * [ 🚀 定时器](#使用文档)
     * [定时器使用](#使用文档)
     * [编写定时器任务](#使用文档)
- [后续TODO](##后续TODO)
- [免责声明](##免责声明)

## <h2 id='1'>项目结构</h2>
```
│  ─ config.py             #项目配置文件
│  ─ README.md
│  ─ requirements.txt      #第三方依赖包
├─ accessory             #附件
│      ─ chromedriver      /usr/local/bin/chromedriver chromedriver地址
│      ─ logo.png          #logo
├─ component             #项目主体
│      ─ account.py        #登陆账户操作类模块
│      ─ log.py            #日志记录模块
│      ─ sliderlogin.py    #滑动验证登陆模块   
│      ├─ img              #滑动验证图片保存文件夹
│      ├─ log              #项目日志保存文件夹
├─ deco                  #component中各个模块的装饰器
│      ─ login.py
└─ util                  #项目工具函数类，对应各个模块
       ─ slider.py     
      
```
## <h2 id='2'>使用文档</h2>
> 以下所有的数据采集均默认使用**MongoDB**数据库进行保存

### <h3 id='2.0'>0. 安装使用环境(requirements.txt)</h3>
安装项目需要的第三方模块，在确保本机安装的python版本为3.x后，使用命令行:
```commandline
pip install -r requirements.txt
```
###  <h3 id='2.1'>1. 安装MongoDB数据库</h3>
> * [Windows 平台安装 MongoDB](https://www.runoob.com/mongodb/mongodb-window-install.html)
> * [Linux平台安装MongoDB](https://www.runoob.com/mongodb/mongodb-linux-install.html)
> * [Mac OSX 平台安装 MongoDB](https://www.runoob.com/mongodb/mongodb-osx-install.html)

Python 要连接 MongoDB 需要 MongoDB 驱动，这里我们使用 PyMongo 驱动来连接，安装pymongo(requirement.txt已经包含),
若自行安装，使用命令行:
```commandline
pip install pymongo
