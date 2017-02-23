import sys
def output(caches):
    sys.stdout = open('teste2.txt','w')
    n_used_caches = 0
    for c in caches:
        if c.free_size < c.max_size:
            n_used_caches += 1
    print(n_used_caches)
    for cache in caches:
        if len(cache.videos)>0:
            print(str(cache.id) + ' ', end='')
            for i,video_id in enumerate(cache.videos):
                if i == len(cache.videos)-1:
                    print(video_id)
                else:
                    print(str(video_id) + ' ', end='')

