# FileTrans
一键翻译批量文件工具


## 使用 How

### 前提  

项目需要访问百度翻译API，`APPID` 以及 `secretKey` 的获取方式如下：
>1.使用您的百度账号登录[百度翻译开放平台](http://api.fanyi.baidu.com/)；  
2.注册成为开发者，获得 APPID ；  
3.进行开发者认证；  
4.开通通用翻译API服务：[开通链接](https://fanyi-api.baidu.com/choose)。   

服务免费，放心使用。更多详情可访问 [百度翻译开放平台官网](http://api.fanyi.baidu.com/product/11)  

将获得的 `APPID` 和 `secretKey` 填入 `config.json`
```
{
    "appid" : "your APPID", 
    "secretKey" : "your secretKey"
}
```

### 运行  
**1. 前往[releases](https://github.com/cyh1998/FileTrans/releases)下载 FileTrans 可执行文件**  

下载运行即可，若无法运行可使用下面的方法

**2. 前往[releases](https://github.com/cyh1998/FileTrans/releases)下载源码 `FileTrans.py`**  
```
python FileTrans.py
```
拥有 `python3` 环境即可运行，无需额外库  

### 支持语种
| 名称        |    代码    | 名称        |    代码    | 名称         |    代码    |
| ----------- | :--------: | ----------- | :--------: | ------------ | :--------: |
| 中文        |     zh     | 希腊语      |     el     | 繁体中文     |     cht    |
| 英语        |     en     | 荷兰语      |     nl     | 西班牙语     |     spa    |
| 日语        |     jp     | 波兰语      |     pl     | 阿拉伯语     |     ara    |
| 韩语        |     kor    | 丹麦语      |     dan    | 葡萄牙语     |     pt     |
| 法语        |     fra    | 芬兰语      |     fin    | 意大利语     |     it     |
| 泰语        |     th     | 捷克语      |     cs     | 匈牙利语     |     hu     |
| 俄语        |     ru     | 瑞典语      |     swe    | 保加利亚语   |     bul    |
| 德语        |     de     | 越南语      |     vie    | 爱沙尼亚语   |     est    |
|             |            |             |            | 罗马尼亚语   |     rom    |
|             |            |             |            | 斯洛文尼亚语 |     slo    |

## 感谢 Thanks  

[百度通用文本翻译API](http://api.fanyi.baidu.com/product/11)
