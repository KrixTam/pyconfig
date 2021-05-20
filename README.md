# ni-config

把json文件当作配置文件使用时，为了方便对配置文件进行操作而创建的配置文件类库

配置文件的内容为json格式。

规范化json内容的实现层面上，主要通过 [JSON Schema](https://json-schema.org/) 对配置文件的json结构进行定义并进行校验实现的。

## 安装

> pip install ni-config

## 构建实例

> from config import config
> 
> c = config(desc)

| desc | 说明 |
| --- | --- |
| str | 不含扩展名的文件名，一般为当前目录下、以”desc“为后缀的文件名，如：server.desc |
| dict | 包含“name”、“default”、“schema”定义的词典 |

## validate

校验配置文件的内容是否与定义的一致。

> config("server").validate()

## load_config

加载配置文件内容，并对内容进行校验，如果校验失败，则回退到原来的配置内容。

> config("server").load_config("slaver.cfg")

## dump

把配置内容输出到指定文件

> config("server").dump()
> 
> config("server").dump("master.cfg")

## Get + Set

对config对象中的配置进行修订、设置，或者获取相关配置项的信息；进行修改/设置时，会对变更后的配置内容进行有效性校验，如果校验失败，则回退到原来的配置内容。

> c = config("server")
> 
> c["ip"] = "192.168.1.101"
> 
> print(c["ip"])
> 
> "192.168.1.101"