import input

def algorithm():

    V, E, R, C, X, caches, videos, endpoints, requests = input.input_parser()
    
    endpoint_statistics = {} 
    for r in requests:
        aux = {r.video: r.n_requests}
        endpoint_statistics.setdefault(r.endpoint, []).append(aux)

    #print (endpoint_statistics)
    for endpoint in endpoint_statistics:
        max = 0;
        sorted_videos = []
        for video in endpoint_statistics[endpoint]:
            for key, value in video.items():
                total = videos[key].size * value
                sorted_videos.append((total,  key))
        sorted_videos = sorted(sorted_videos, key=lambda tup: tup[0])
        
        for i in endpoints[endpoint].cache_latency:
            for idx, j in enumerate(sorted_videos):
                if caches[i].size > videos[j[1]].size:
                    caches[i].videos.append(j[1])
                    sorted_videos.pop(0)

        for i in caches:
            print(i)

            
    


if __name__ == '__main__':
    algorithm()
