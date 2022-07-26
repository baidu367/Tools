# Dockerfile指令说明

## 1. From
基础镜像
```dockerfile
FROM ubuntu 
```
## 2. MAINTAINER
镜像维护者姓名和邮箱地址
```dockerfile
MAINTAINER 
```
## 3. RUN
容器构建时执行，命令行指令(shell格式, exec格式)
```dockerfile
RUN yum update
```
## 4. EXPOSE
当前容器暴露的端口
```dockerfile
EXPOSE 端口号
```
## 5. ENV
添加运行时环境环境
```dockerfile
ENV MY_PATH /usr/mytest
```
## 6. WORKDIR
进入容器后所在位置
```dockerfile
WORKDIR $MY_PATH
```
## 7. USER
使用权限，默认root
```dockerfile
USER root
```
## 8. ADD
将宿主机目录下的文件拷贝进镜像且会自动处理url和解压tar压缩包
```dockerfile
ADD file
```
## 9. COPY
类似ADD， 拷贝文件和目录到镜像中
```dockerfile
COPY file /home
```
## 10. CMD
容器启动后执行,docker run命令会覆盖cmd命令
```dockerfile
CMD['执行文件','使用的参数']
```
## 11. ENTRYPOINT
与 run、cmd功能相似， 但是可以传递可变参数
```dockerfile
ENTRYPOINT
```



