import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def iauthfunctions_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "iauthfunctions_get_sum": iauthfunctions_get_sum,
    }
