FROM python as builder

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

FROM python
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY docker/entrypoint.sh .

CMD ./entrypoint.sh
