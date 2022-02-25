from cache_data import cache_data

class Cache:

    # Check if key in cache
    def is_key_in_cache(key):
        if key not in cache_data:
            return False
        return True

    # Delete key in cache
    def delete_key_in_cache(key):
        cache_data.pop(key, None)
        return

    # Get value from cache
    def get_val_in_cache(key):
        val = cache_data.get(key, None)
        return val