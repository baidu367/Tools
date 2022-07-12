# docker操作

## 1、安装
### 1.1卸载旧docker版本
```shell
yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
```
### 1.2安装gcc
```shell
yum -y install gcc
```
### 1.3安装gcc-c++
```shell
yum -y install gcc-c++
```
### 1.4扩展包
```shell
yum install -y yum-utils
```
### 1.5设置stable镜像仓库(阿里云)
```shell
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```
### 1.6更新yum软件包索引
```shell
yum makecache fast
```
### 1.7安装docker
```shell
yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
### 1.8启动docker
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
### 2.1停止docker
```shell
systemctl stop docker
```
### 2.2移除docker安装包
```shell
yum remove docker-ce docker-ce-cli containerd.io
```
### 2.3删除docker配置文件
```shell
rm -rf /var/lib/docker
rm -rf /var/lib/containerd
```

## 3、docker常用命令
### 3.1启动docker
```shell
systemctl start docker
```
### 3.2重启docker
```shell
systemctl REstart docker
```
### 3.3停止docker
```shell
systemctl stop docker
```
### 3.4查看docker状态
```shell
systemctl status docker
```
### 3.5开机启动docker
```shell
systemctl enable docker
```
### 3.6查看docker概要信息
```shell
docker info
```
### 3.7列出本地docker镜像
```shell
docker images
```
### 3.8列出本地docker镜像
```shell
docker images
```
    images 使用参数： 
        -a    列出所有镜像
        -q    只显示镜像ID

### 3.9查询某个镜像
```shell
docker search XXX
```
    search 使用参数：
        --limit 5   可以限制显示条数
### 3.10拉取某个镜像(不加版本号，默认拉取最新)
```shell
docker pull XXX
```
### 3.11查询镜像/镜像/数据卷所占的空间
```shell
docker system df
```
### 3.12删除某个镜像
```shell
docker rmi XXXX
```
    rmi 使用参数：
        -f    强制删除
### 3.13删除全部镜像
```shell
docker rmi $(docker images -qa)
```

## 4、docker容器命令
### 4.1新建+启动容器
```shell
docker run
```
    run 使用参数：
        --name  为容器指定新名称
        -d  后台运行容器
        -i 交互模式运行容器
        -t 为容器重新分配一个伪输入终端
        -p 端口映射 例：8000(宿主机端口):8000(容器端口)
        /bin/bash 进入交互式位终端 例：docker -it ubuntu /bin/bash
### 4.2列出所有正在运行的容器
```shell
docker ps
```
    ps 使用参数：
        -a  历史所有运行过的容器
        -i  显示最近创建的容器
        -n  显示最近n个创建的容器
        -q 只显示容器编号
### 4.3退出容器
run进入容器，exit退出，容器终止
```shell
exit
```
run进入容器，ctrl+p+q退出，容器终止
```shell
ctrl+p+q
```
### 4.4启动已经停止的容器
```shell
docker start 容器ID或容器名
```
### 4.5重启容器
```shell
docker restart 容器ID或容器名
```
### 4.6停止容器
```shell
docker stop 容器ID或容器名
```
### 4.7强制停止容器
```shell
docker kill 容器ID或容器名
```
### 4.8删除停止的容器
```shell
docker rm 容器ID或容器名
```
### 4.强制删除所有容器
```shell
docker rm -f $(docker ps -a -q)
```
```shell
docker ps -a -q|xargs docker rm
```

