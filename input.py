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
        self.i = i

def input_parser():

