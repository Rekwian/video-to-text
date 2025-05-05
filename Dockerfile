FROM oven/bun:1.1

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

WORKDIR /app

COPY . .

RUN bun install

CMD ["bun", "start"]
