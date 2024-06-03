# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir streamlit ping3

# 暴露 Streamlit 默认的运行端口
EXPOSE 8501

# 设置环境变量，避免 Streamlit 模式为开发模式
ENV STREAMLIT_RUN_ON_SAVE=""
ENV PYTHONUNBUFFERED=1

# 添加 Streamlit 默认配置以便在 Docker 中运行
RUN mkdir -p ~/.streamlit && \
    echo "\
    [server]\n\
    headless = true\n\
    enableCORS = false\n\
    port = 8501\n\
    " > ~/.streamlit/config.toml

# 启动 Streamlit 应用
CMD ["streamlit", "run", "main.py"]
