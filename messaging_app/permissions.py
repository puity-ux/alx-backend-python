from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Allows access only to participants of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are: GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS or request.method in ['PUT', 'PATCH', 'DELETE', 'POST']:
            return request.user == obj.sender or request.user == obj.recipient
        return False
