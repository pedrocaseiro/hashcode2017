class Video:
    def __init__(self, size, id):
        self.size = size
        self.id = id

class Endpoint:
    def __init__(self, latency, n_conn_caches, cache_latency, id):
        self.latency = latency
        self.n_conn_caches = n_conn_caches
        self.cache_latency = cache_latency
        self.id = id

class Request:
    def __init__(self, video, endpoint, n_requests, id):
        self.video = video
        self.endpoint = endpoint
        self.n_requests = n_requests
        self.id = id

def input_parser():
    V, E, R, C, X = map(int, input().split()) 

    videos = []
    for id, size in enumerate(map(int, input().split())):
        videos.append(Video(id, size))

    endpoints = []
    for i in range(E):
        endpoint_to_datacenter_latency, n_caches = map(int, input().split())
        caches_latency = {}
        for j in range(n_caches):
            cache_id, cache_latency = map(int, input().split())
            caches_latency.update({cache_id: cache_latency})
        endpoints.append(Endpoint(endpoint_to_datacenter_latency, n_caches, caches_latency, i))

    requests = []
    for i in range(R):
        video_id, endpoint_id, n_requests = map(int, input().split())
        requests.append(Request(video_id, endpoint_id, n_requests, i))
