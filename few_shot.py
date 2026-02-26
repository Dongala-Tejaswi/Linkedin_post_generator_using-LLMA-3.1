import json

class FewShotPosts:

    def __init__(self):
        with open("data/processed_posts.json", encoding="utf-8") as f:
            self.posts = json.load(f)

    def get_filtered_posts(self, length, language, tag):
        filtered = []

        for post in self.posts:
            if (
                post.get("length") == length and
                post.get("language") == language and
                tag in post.get("tags", [])
            ):
                filtered.append(post)

        return filtered

    def get_tags(self):
        tags = set()

        for post in self.posts:
            for tag in post.get("tags", []):
                tags.add(tag)

        return list(tags)