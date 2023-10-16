FROM python:3.10-slim
ENV TOKEN = '(your token here)'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py