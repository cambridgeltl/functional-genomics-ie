
def check_model(config):
    pass


def check_data(config):
    pass


def check_training(config):
    pass


def check_mode_train(config):
    valid_data = {
        "MODEL": check_model,
        "DATA": check_data,
        "TRAINING": check_training
    }

    for k, f in valid_data.items():
        try:
            subconfig = config[k]
            f(subconfig)
        except KeyError:
            raise Exception(f"{k} data not found, this is required for training mode")


def check_config_based_on_parameter(config, param_key, valid_data):
    try:
        param_val = config[param_key]
    except KeyError:
        raise Exception(f"Key {param_key} was not found in (sub)config, found keys were {'\n'.join(config.keys())}")

    try:
        valid_data[param_val](config)
    except KeyError:
        raise Exception(f"{param_val} is not a valid parameter for {param_key}, valid parameters: {'\n'.join(valid_data.keys())}")


# Start point
def check_config(config):
    valid_mode_data = {
        "train": check_mode_train
    }
    check_config_based_on_parameter(config, "MODE", valid_mode_data)

