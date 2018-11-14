# 获取抖音广告数据

### 依赖抖音签名算法：
[https://github.com/CrawlData/douyin-sign](https://github.com/CrawlData/douyin-sign)

### 运行
```
python ./douyin.ad.py
```

### 注意

+ 经过大量测试，获取广告的间隔时间大约在2分钟。1天可获取24*30=720个；
+ 结合不同区域的IP来调用，基本可以获取抖音千人千面的广告数据； 
+ 代码内签名依赖的算法服务，最多可调用300次，过后失效。请联系作者。

### 效果
[广告实例](https://www.iesdouyin.com/share/video/6616234046789782797/?region=CN&mid=6616234052879911694&u_code=g935miig&titleType=title)

![抖音广告数据](./preview.png)
