docker build -t live-tmp -f live.Dockerfile .
docker run -p 8080:8080 -v ${PWD}/src:/app live-tmp

