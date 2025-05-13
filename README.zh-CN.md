# ai-infra-stack

[English](./README.md) | [简体中文](./README.zh-CN.md)

一个现代化、可扩展的 AI 应用基础设施栈。

## 特性
- 模块化的服务健康检查。
- 基于插件的架构，易于扩展。
- 为核心服务（MySQL, Redis, Elasticsearch, Neo4j）预配置了 Docker 环境。
- 为所有集成的服务提供了连接测试器。

## 开始使用

### 先决条件
- Docker 和 Docker Compose
- Python 3.8+ (推荐使用 Conda 进行环境管理)
- `uv` (可选，用于在 Conda 环境中加速包的安装)

### 安装
1. **启动基础设施服务：**
   所有后端服务均通过 Docker Compose 管理。
   ```bash
   docker-compose up -d
   ```

2. **设置 Python 环境：**
    ```bash
    # 克隆仓库
    $ git clone https://github.com/yourusername/ai-infra-stack.git
    $ cd ai-infra-stack

    # 创建并激活 Conda 环境 (可将 'ai-infra' 替换为您偏好的名称)
    $ conda create -n ai-infra python=3.11
    $ conda activate ai-infra

    # 安装依赖
    # 使用 uv 同步依赖 (请确保 requirements.txt 文件是最新的)
    $ uv sync
    ```

## 使用方法
在基础设施服务运行并且 Python 环境设置好之后，您可以运行连接测试：

```bash
# 运行所有服务的连接测试
$ python -m app.connection_tester
```

## 贡献
欢迎贡献！请提交 Issue 或 Pull Request。

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证
本项目基于 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式
如有问题或建议，请在 GitHub 上提交 Issue。 