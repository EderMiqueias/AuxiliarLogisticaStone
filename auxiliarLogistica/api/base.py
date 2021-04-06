import json
import falcon


class BaseResource(object):
    HELLO = {
        "message": "welcome to my falcon api",
        "county": "get funny :)",
    }

    def on_not_found(self, resp, message):
        resp.status = falcon.HTTP_404
        resp.body = self.to_json({
            "error": "not found error",
            "message": message,
        })

    def to_json(self, obj):
        return json.dumps(obj)

    def from_json(self, obj):
        return json.loads(obj)
