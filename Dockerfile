FROM python:3.9-slim

ARG GRADIO_SERVER_PORT=8000
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

WORKDIR /workspace

ADD ./ /workspace/

RUN pip install -r /workspace/requirements.txt

CMD ["python", "/workspace/app_live.py"]