# ai-infra-stack

[English](./README.md) | [简体中文](./README.zh-CN.md)

A modern, extensible infrastructure stack for AI applications.

## Features
- Modular service health checking
- Plugin-based architecture
- Easy to extend and maintain

## Getting Started

### Prerequisites
- Python 3.8+
- Redis (for testing Redis connectivity)

### Installation
```bash
# Clone the repository
$ git clone https://github.com/yourusername/ai-infra-stack.git
$ cd ai-infra-stack

# (Optional) Create a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

## Usage
You can run the service testers or extend the stack with your own plugins.

```bash
# Example: Run all service tests
$ python app/main.py
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
