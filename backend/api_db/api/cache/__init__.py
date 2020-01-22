from django.core.cache import cache
from django.conf import settings

from api_basebone.utils.redis import redis_client


class BaseCache:
    """缓存基础类"""

    def set_cache(self, key, content, pipe=None):
        key = cache.make_key(key)
        pipe = pipe if pipe else redis_client
        pipe.set(key, content)
        cache_time = getattr(settings, 'API_CACHE_TIME', 1 * 60)
        pipe.expire(key, cache_time)

    def get_cache(self, key, pipe=None):
        key = cache.make_key(key)
        pipe = pipe if pipe else redis_client
        return pipe.get(key)

    def delete_cache(self, key, pipe=None):
        key = cache.make_key(key)
        pipe = pipe if pipe else redis_client
        pipe.delete(key)


class ApiCache(BaseCache):
    API_KEY = "api:slug:{}"

    def set_api_config(self, slug, api_config, pipe=None):
        """缓存api配置"""
        self.set_cache(self.API_KEY.format(slug), api_config, pipe)

    def get_api_config(self, slug, pipe=None):
        """读api缓存"""
        return self.get_cache(self.API_KEY.format(slug), pipe)

    def delete_api_config(self, slug, pipe=None):
        """清api缓存"""
        self.delete_cache(self.API_KEY.format(slug), pipe)


class TriggerCache(BaseCache):
    TRIGGER_KEY = "trigger:slug:{}"

    def set_config(self, slug, config, pipe=None):
        """缓存trigger配置"""
        self.set_cache(self.TRIGGER_KEY.format(slug), config, pipe)

    def get_config(self, slug, pipe=None):
        """读trigger缓存"""
        return self.get_cache(self.TRIGGER_KEY.format(slug), pipe)

    def delete_config(self, slug, pipe=None):
        """清trigger缓存"""
        self.delete_cache(self.TRIGGER_KEY.format(slug), pipe)


api_cache = ApiCache()
trigger_cache = TriggerCache()