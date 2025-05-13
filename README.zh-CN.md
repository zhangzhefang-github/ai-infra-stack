# ai-infra-stack

[English](./README.md) | [简体中文](./README.zh-CN.md)

一个现代化、可扩展的 AI 应用基础设施栈。

## 特性
- 模块化的服务健康检查
- 基于插件的架构
- 易于扩展和维护

## 开始使用

### 先决条件
- Python 3.8+
- Redis (用于测试 Redis 连接性)

### 安装
```bash
# 克隆仓库
$ git clone https://github.com/yourusername/ai-infra-stack.git
$ cd ai-infra-stack

# (可选) 创建虚拟环境
$ python3 -m venv venv
$ source venv/bin/activate

# 安装依赖
$ pip install -r requirements.txt
```

## 使用方法
你可以运行服务测试器，或使用自己的插件扩展此栈。

```bash
# 示例：运行所有服务测试
$ python app/main.py
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