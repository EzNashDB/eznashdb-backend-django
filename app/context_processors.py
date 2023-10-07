from collections import namedtuple


def navbar(request):
    NavbarItem = namedtuple("NavbarItem", "label view_name")
    current_app_name = request.resolver_match.app_names[0]
    current_url_name = request.resolver_match.url_name
    return {
        "current_view_name": f"{current_app_name}:{current_url_name}",
        "navbar_items": [
            NavbarItem("Shuls", "eznashdb:shuls"),
            NavbarItem("Map", "eznashdb:shuls_map"),
            NavbarItem("Add a Shul", "eznashdb:create_shul"),
        ],
    }
