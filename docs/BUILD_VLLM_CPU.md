```bash
# 1.
git clone https://github.com/vllm-project/vllm.git

# 2.
run wsl

# 3.
cd vllm

#4.
docker image build -f docker/Dockerfile.cpu \
    --tag vllm-cpu-env \
    --target vllm-openai .
```

만약 빌드시 메모리 터진다면 로그 확인후 아래 작업 수행

빌드 명령어에 `--build-arg CMAKE_BUILD_PARALLEL_LEVEL=4` 추가 -> 난 여기서 해결됨

안되면 추가로 `--build-arg MAX_JOBS=4` 추가

안되면 **docker/Dockerfile.cpu** 에서 `max_jobs=4`로 변경

안되면 .wslconfig 수정 후 wsl **재시작** 후 **재빌드**

```bash
[wsl2]
memory=10GB
swap=8GB
processors=6
```
