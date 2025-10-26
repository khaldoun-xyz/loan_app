FROM condaforge/miniforge3:latest

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  && rm -rf /var/lib/apt/lists/* \
  && curl -fsSL https://pixi.sh/install.sh | bash \
  && mv /root/.pixi/bin/pixi /usr/local/bin/pixi

ENV PATH="/root/.local/bin:$PATH"

COPY pixi.toml pixi.lock ./

RUN pixi install --locked

COPY . .

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=loan_app.settings

EXPOSE 8001

CMD ["/app/.pixi/envs/default/bin/python", "loan_app/manage.py", "runserver", "0.0.0.0:8001"]
