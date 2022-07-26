# docker安装及使用

## 1、安装
### 1.1 卸载旧docker版本
```shell
yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
```
### 1.2 安装gcc
```shell
yum -y install gcc
```
### 1.3 安装gcc-c++
```shell
yum -y install gcc-c++
```
### 1.4 扩展包
```shell
yum install -y yum-utils
```
### 1.5 设置stable镜像仓库(阿里云)
```shell
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```
设置stable镜像仓库出现语法错误，可能是系统python2版本被修改，需要修改docker配置文件第一行python版本
```shell
vim /usr/bin/yum-config-manager
```
### 1.6 更新yum软件包索引
```shell
yum makecache fast
```
### 1.7 安装docker
```shell
yum -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
### 1.8 启动docker
```shell
systemctl start docker
```
### 1.9（可选）阿里云镜像加速器

加速器地址
https://XXXX.mirror.aliyuncs.com（登陆阿里云获取）

1. 安装／升级Docker客户端
推荐安装1.10.0以上版本的Docker客户端，参考文档docker-ce

2. 配置镜像加速器
针对Docker客户端版本大于 1.10.0 的用户

您可以通过修改daemon配置文件/etc/docker/daemon.json来使用加速器

```shell
sudo mkdir -p /etc/docker
```
```shell
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://XXXX.mirror.aliyuncs.com"]
}
EOF
```
```shell
sudo systemctl daemon-reload
```
```shell
sudo systemctl restart docker
```

## 2、卸载docker
### 2.1 停止docker
```shell
systemctl stop docker
```
### 2.2 移除docker安装包
```shell
yum remove docker-ce docker-ce-cli containerd.io
```
### 2.3 删除docker配置文件
```shell
rm -rf /var/lib/docker
rm -rf /var/lib/containerd
```

## 3、docker常用命令
### 3.1 启动docker
```shell
systemctl start docker
```
### 3.2 重启docker
```shell
systemctl restart docker
```
### 3.3 停止docker
```shell
systemctl stop docker
```
### 3.4 查看docker状态
```shell
systemctl status docker
```
### 3.5 开机启动docker
```shell
systemctl enable docker
```
### 3.6 查看docker概要信息
```shell
docker info
```
### 3.7 列出本地docker镜像
```shell
docker images
```
### 3.8 列出本地docker镜像
```shell
docker images
```
    images 使用参数： 
        -a    列出所有镜像
        -q    只显示镜像ID

### 3.9 查询某个镜像
```shell
docker search XXX
```
    search 使用参数：
        --limit 5   可以限制显示条数
### 3.10 拉取某个镜像(不加版本号，默认拉取最新)
```shell
docker pull XXX
```
### 3.11 查询镜像/镜像/数据卷所占的空间
```shell
docker system df
```
### 3.12 删除某个镜像
```shell
docker rmi XXXX
```
    rmi 使用参数：
        -f    强制删除
### 3.13 删除全部镜像
```shell
docker rmi $(docker images -qa)
```

## 4、docker容器命令
### 4.1 新建+启动容器
```shell
docker run
```
    run 使用参数：
        --name  为容器指定新名称
        -d  后台运行容器(守护式容器)
        -i 交互模式运行容器
        -t 为容器重新分配一个伪输入终端
        -p 端口映射 例：8000(宿主机端口):8000(容器端口)
        /bin/bash 进入交互式位终端 例：docker -it ubuntu /bin/bash（推荐加上参数 exec）
### 4.2 列出所有正在运行的容器
```shell
docker ps
```
    ps 使用参数：
        -a  历史所有运行过的容器
        -i  显示最近创建的容器
        -n  显示最近n个创建的容器
        -q 只显示容器编号
### 4.3 退出容器
run进入容器，exit退出，容器终止
```shell
exit
```
run进入容器，ctrl+p+q退出，容器终止
```shell
ctrl+p+q
```
### 4.4 启动已经停止的容器
```shell
docker start 容器ID或容器名
```
### 4.5 重启容器
```shell
docker restart 容器ID或容器名
```
### 4.6 停止容器
```shell
docker stop 容器ID或容器名
```
### 4.7 强制停止容器
```shell
docker kill 容器ID或容器名
```
### 4.8 删除停止的容器
```shell
docker rm 容器ID或容器名
```
### 4.9 强制删除所有容器
```shell
docker rm -f $(docker ps -a -q)
```
```shell
docker ps -a -q|xargs docker rm
```
### 4.10 查看容器日志
```shell
docker logs  容器ID
```
### 4.11 查看容器内部细节
```shell
docker inspect 容器ID
```
### 4.12 进入容器
```shell
docker exec -it 容器ID /bin/bash
```
```shell
docker attach 容器ID
```
不推荐使用：attach直接进入容器启动命令的终端，不会启动新的进程用ex 退出， 会导致容器的停止。

推荐使用：exec是在容器打开新的终端，并且可以启动新的进程用exit退出， 不会导致容器的停止。
### 4.13 从容器拷贝文件到宿主机
```shell
docker cp 容器ID：容器内路径 目的主机路径
```
### 4.14 （备份）导出容器的内容作为一个tar归档文件
```shell
docker export 容器ID > 文件名.tar
```
### 4.15 （还原备份）导入一个tar归档文件成为容器
```shell
cat 文件名.tar | docker import - 镜像用户/镜像包名:镜像版本号
```
### 4.16 提交容器副本使之成为一个新的镜像
```shell
docker commit -m='提交的描述信息' -a='作者' 容器ID 镜像用户/镜像包名:镜像版本号
```
### 4.17 添加容器数据卷持久化数据共享
```shell
docker run -it --privileged==true -v 宿主机绝对路径:/容器内路径 --name=别名 镜像名
```
### 4.18 网络配置
```shell
docker network 
```
    network 使用参数：
        ls  查看所有docker网络
        rm xxx  删除指定网络
        create xxx 创建网络
        inspect xxx 查看网络信息
