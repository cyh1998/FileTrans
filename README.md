# FileTrans
一键翻译批量文件工具


## 使用 How

### 前提  

项目需要访问百度翻译API，`APPID` 以及 `secretKey` 的获取方式如下：
>1.使用您的百度账号登录[百度翻译开放平台](http://api.fanyi.baidu.com/)；  
2.注册成为开发者，获得 APPID ；  
3.进行开发者认证；  
4.开通通用翻译API服务：[开通链接](https://fanyi-api.baidu.com/choose)。   

服务免费，放心使用。更多详情可访问[百度翻译开放平台官网](http://api.fanyi.baidu.com/product/11)  

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


## 更新 Update  

- [ ] 合并文件名调用，减少API调用次数  
- [ ] 支持多语言翻译选择  
- [ ] 支持文件翻译后导出指定路径


## 感谢 Thanks  

[百度通用文本翻译API](http://api.fanyi.baidu.com/product/11)
