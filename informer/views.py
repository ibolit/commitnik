from rest_framework.response import Response
from rest_framework.views import APIView

from .git_wrapper import git


class InformerView(APIView):
    def get(self, request):
        current_commit_hash = git('rev-parse HEAD')
        commit_date = git(f'show -s --format=%ci "{current_commit_hash}"')
        branch = git('rev-parse --abbrev-ref HEAD')
        version = self.get_version(current_commit_hash)

        started = None
        uptime_seconds = None

        return Response({
            'commit': current_commit_hash,
            'commit_date': commit_date,
            'branch': branch,
            'version': version,
            'started': started,
            'uptime_seconds': uptime_seconds,
        })

    def get_version(self, commit):
        all_tags = git(f'tag -l').split('\n')
        return all_tags[-1]
