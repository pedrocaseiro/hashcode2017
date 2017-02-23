import sys
def output(caches):
    sys.stdout = open('kittens_out.txt','w')
    n_used_caches = 0
    for c in caches:
        if c.free_size < c.max_size:
            n_used_caches += 1
    print(n_used_caches)
    for cache in caches:
        print(cache.id)
        for video_id in cache.videos:
            print(video_id, sep=' ', end='', flush=True)
