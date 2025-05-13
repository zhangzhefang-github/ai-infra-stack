# ai-infra-stack

[English](./README.md) | [简体中文](./README.zh-CN.md)

A modern, extensible infrastructure stack for AI applications.

## Features
- Modular service health checking.
- Plugin-based architecture for easy extension.
- Pre-configured Docker environment for essential services: MySQL, Redis, Elasticsearch, and Neo4j.
- Connection testers for all integrated services.

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.8+ (Conda is recommended for environment management)
- `uv` (optional, for faster package installation within a Conda environment)

### Installation
1. **Start the infrastructure services:**
   All backend services are managed by Docker Compose.
   ```bash
   docker-compose up -d
   ```

2. **Set up the Python environment:**
   ```bash
   # Clone the repository
   $ git clone https://github.com/yourusername/ai-infra-stack.git
   $ cd ai-infra-stack

   # Create and activate a Conda environment (replace 'ai-infra' with your preferred name)
   $ conda create -n ai-infra python=3.11
   $ conda activate ai-infra

   # Install dependencies
   # Sync dependencies using uv (ensure requirements.txt is up-to-date)
   $ uv sync
   ```

## Usage
Once the infrastructure services are running and the Python environment is set up, you can run the connection tests:

```bash
# Run connection tests for all services
$ python -m app.connection_tester
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, please open an issue on GitHub.
