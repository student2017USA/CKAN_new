import ckan.plugins.toolkit as tk
import ckanext.iauthfunctions.logic.schema as schema


@tk.side_effect_free
def iauthfunctions_get_sum(context, data_dict):
    tk.check_access(
        "iauthfunctions_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.iauthfunctions_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'iauthfunctions_get_sum': iauthfunctions_get_sum,
    }
