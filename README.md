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

## 关于默认值

可以通过*set_default*方法来初始化配置实例的默认值

> config("server").set_default()

如若想检查目前的设定是否是默认值，可以使用*is_default*方法

> c = config("server")
> 
> c.set_default()
> 
> c.is_default()
> 
> c.is_default('ip')

如果仅希望检查某个配置是否为默认值，把该配置项作为参数传递给*is_default*方法，默认不传递参数的情况下，将会对所有配置项进行检查

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