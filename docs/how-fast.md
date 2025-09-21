# Performance  

## HTTP

Over http, we were able to achive P99 of `18ms` with `1K QPS` on just `1vCPU` of for API and `0.5 vCPU` for `Redis`

```bash
# http
oha -z 25s -c 5 --rand-regex-url \
"http://localhost:8085/nu'/random\\?num=[1-9]{1,4}"

# grpc
ghz --insecure --proto src/worldpop/pb/random_city.proto --call randomcity.RandomCityService.GetRandomCity -d '{"num": 500 }' -c 5 -r 1000 -n 25000 localhost:51 
```

| Commit  | Http                      | Grpc                      |
|---------|---------------------------|---------------------------|
| 8ff45db | ![Http Perf](http.png)    | ![GRPC Perf](grpc.png)    |

-----

### Round 1

| Percentile       | gRPC (ms) | HTTP (FastAPI) (ms) | Difference (ms) |
|------------------|-----------|---------------------|-----------------|
| 10th             | 1.39      | 3.3                 | -1.91           |
| 25th             | 2.03      | 4.1                 | -2.07           |
| 50th (Median)    | 3.01      | 5.2                 | -2.19           |
| 75th             | 4.46      | 7.0                 | -2.54           |
| 90th             | 6.28      | 9.1                 | -2.82           |
| 95th             | 7.77      | 11.3                | -3.53           |
| 99th             | 11.87     | 19.1                | -7.23           |

------;

### Round 2

See [d8302c7](https://github.com/sahiljambhekar/fast-api-playground/commit/d8302c7d92dabbcc10cbfdb54d12a6ea712b5b21)

Switched Uvicorn with Hypercorn, and saw quite a difference in performance just over http 1.1
Then tried http2 over hypercorn, and saw degradation.

| **Metric**       | **Hypercorn (HTTP)** | **Hypercorn (HTTP/2 + SSL)** | **gRPC**       | **Uvicorn (HTTP)** |
|------------------|-----------------------|------------------------------|----------------|--------------------|
| **Requests/sec** | 1143.45              | 600.71                       | 999.84         | 825.43             |
| **Success Rate** | 100.00%              | 99.90%                       | 100.00%        | 100.00%            |
| **Average Latency (ms)** | 4.4          | 4.9                          | 3.57           | 6.0                |
| **10th Percentile (ms)** | 3.1          | 3.6                          | 1.39           | 3.3                |
| **25th Percentile (ms)** | 3.4          | 3.9                          | 2.03           | 4.1                |
| **50th Percentile (Median)** | 3.8      | 4.5                          | 3.01           | 5.2                |
| **75th Percentile (ms)** | 4.6          | 5.4                          | 4.46           | 7.0                |
| **90th Percentile (ms)** | 5.7          | 6.6                          | 6.28           | 9.1                |
| **95th Percentile (ms)** | 6.4          | 7.6                          | 7.77           | 11.3               |
| **99th Percentile (ms)** | 8.6          | 10.2                         | 11.87          | 19.1               |
| **Slowest Response (ms)** | 1152.7      | 48.9                         | 30.39          | 72.7               |
| **Fastest Response (ms)** | 1.5         | 1.7                          | 0.60           | 1.0                |
