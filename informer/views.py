from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views import View

from .git_wrapper import git


class InformerView(View):
    def get(self, request):
        current_commit_hash = git('rev-parse HEAD')
        commit_date = git(f'show -s --format=%ci "{current_commit_hash}"')
        branch = git('rev-parse --abbrev-ref HEAD')
        version = self._get_version(current_commit_hash)

        started = settings.START_DATETIME
        uptime_seconds = self._get_uptime(started)

        return JsonResponse({
            'commit': current_commit_hash,
            'commit_date': commit_date,
            'branch': branch,
            'version': version,
            'started': started,
            'uptime_seconds': uptime_seconds,
        })

    def _get_version(self, commit):
        all_tags = git('show-ref --tags').split('\n')
        tags_on_commit = filter(lambda s: s.startswith(commit), all_tags)
        prefix_length = len(' refs/tags/') + len(commit)
        tags = list(map(lambda s: s[prefix_length:], tags_on_commit))
        if tags:
            return sorted(tags, reverse=True)[0]
        return ''

    def _get_uptime(self, started):
        return int((timezone.now() - started).total_seconds())
