class FilterByLoggedUserMixin:
    def get_queryset(self):
        profiles = super().get_queryset()
        public_id = str(self.request.user.public_id)
        return profiles.filter(user_id__public_id=public_id)
