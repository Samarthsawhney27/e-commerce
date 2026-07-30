def auth_middleware(request):
    token = request.headers.get("Authorization")
    if not token:
        raise Exception("Unauthorized")
    return True
