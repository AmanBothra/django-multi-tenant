def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    print(hostname, "=====hostname")
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)


def get_tenants_map():
    """
    returns the two sites
    """
    return {
        "company2.myapp.local": "company2",
        "company3.myapp.local": "company3",
    }
