# 使用步骤

1. 安装虚拟环境

```bash
poetry install
```

2. 将 `.env.example` 文件复制为 `.env` ，并填入相关变量

3. 将所需的合约文件放入 `contracts` 文件夹中（如果有必要的话）

4. 编写 `main.py` 脚本文件

5. 运行脚本

```bash
poetry run python main.py
```

或者：

```bash
poetry shell
python main.py
```

6. 运行日志会输出到 控制台 和 `logs` 文件夹中
