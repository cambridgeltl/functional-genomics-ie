from matplotlib import pyplot as plt
import matplotlib
import json
import numpy as np

from util.core import printv, ensure_file_ext
from src.misc import txt_str_to_md


styles = ["r-", "b-", "g-", "y-", "k-",
          "r--", "b--", "g--", "y--", "k--",
          "r:", "b:", "g:", "y:", "k:",
          "r-.", "b-.", "g-.", "y-.", "k-.",
          "m-", "m--", "m:", "m-.",
          "c-", "c--", "c:", "c-."]

lb = '\n'  # For f-strings


head_combine_funcs = {"sum": sum,
                      "mean": np.mean,
                      "a_mean": np.mean,
                      "g_mean": lambda x: np.exp(np.log(x).mean())}


def cycle_list(_list):
    return _list[1:] + [_list[0]]


def is_num(x):
    try:
        float(x)
    except (ValueError, TypeError):
        return False
    return True


def get_models_history(config):
    with open(config["PATH"]) as f:
        data = json.load(f)
    return {k: v["history"] for k, v in data.items() if k in config["MODELS"]}


def get_data(history_data, config):
    r_vals = {}

    # Iterate through each model and add relevant entries to graph
    for m_name, m_data in history_data.items():

        # Iterate through each value we want to plot
        for k, k2s in config["VALUES"].items():

            if not isinstance(m_data[k], list):
                continue

            # Value has no sub-values
            if k2s is None:

                has_valid_heads = isinstance(m_data[k][0], dict) and is_num(list(m_data[k][0].values())[0])

                # Check if we are plotting for different heads or just overall
                if "HEAD_NAMES" in config.keys() and has_valid_heads:

                    # Iterate through each head
                    for h_name in config["HEAD_NAMES"]:
                        try:
                            vals = [entry[h_name] for entry in m_data[k]]
                            name = f"{m_name} {k} {h_name}"
                            r_vals[name] = vals
                        except KeyError:
                            print(f"[W] {h_name} not found for {m_name}")

                elif is_num(m_data[k][0]):
                    vals = m_data[k]
                    name = f"{m_name} {k}"
                    r_vals[name] = vals

                # Check if we need to plot combined heads
                if "HEAD_COMBINE" in config.keys() and has_valid_heads:
                    func = head_combine_funcs[config["HEAD_COMBINE"]]
                    vals = [func(entry.values()) for entry in m_data[k]]
                    name = f"{m_name} {k} {config['HEAD_COMBINE']}"
                    r_vals[name] = vals

            # Sub values present
            else:

                # Iterate through them
                for k2 in k2s:

                    has_valid_heads = isinstance(m_data[k][0], dict) and isinstance(list(m_data[k][0].values())[0], dict) and is_num(list(list(m_data[k][0].values())[0].values())[0])

                    # Check if we are plotting for different heads or just overall
                    if "HEAD_NAMES" in config.keys() and has_valid_heads:

                        # Iterate through each head
                        for h_name in config["HEAD_NAMES"]:
                            try:
                                vals = [entry[h_name][k2] for entry in m_data[k]]
                                name = f"{m_name} {k} {h_name} {k2}"
                                r_vals[name] = vals
                            except KeyError:
                                print(f"[W] {h_name} not found for {m_name}")

                    elif isinstance(m_data[k][0], dict) and is_num(list(m_data[k][0].values())[0]):
                        vals = [entry[k2] for entry in m_data[k]]
                        name = f"{m_name} {k} {k2}"
                        r_vals[name] = vals

                    # Check if we need to plot combined heads
                    if "HEAD_COMBINE" in config.keys() and has_valid_heads:
                        func = head_combine_funcs[config["HEAD_COMBINE"]]
                        vals = [func([x[k2] for x in entry.values()]) for entry in m_data[k]]
                        name = f"{m_name} {k} {k2} {config['HEAD_COMBINE']}"
                        r_vals[name] = vals
    return r_vals


def plt_graph(history_data, config, output="show", save_folder=None):
    matplotlib.rc('font', size=8)
    title = config["TITLE"]
    plt.clf()
    plt_styles = styles[:]

    plot_vals = get_data(history_data, config).items()
    plots = sorted(plot_vals, key=lambda x: x[0])

    for name, vals in plots:
        plt.plot(vals, plt_styles[0], label=name)
        plt_styles = cycle_list(plt_styles)

    plt.title(title)
    plt.xlabel("Epoch")
    plt.legend()

    if output == "save":
        fig = plt.gcf()
        fig.set_size_inches(12, 9)
        plt.savefig(f"{save_folder}/{config['TITLE']}", dpi=100)


def graphing(history_data, config):
    for graph_cfg in config["GRAPHS"]:
        save_folder = config["FOLDER"] if "FOLDER" in config.keys() else None
        plt_graph(history_data, graph_cfg, output=config["OUTPUT"], save_folder=save_folder)


def get_report(history_data, config):
    report_vals = get_data(history_data, config)
    b_is_min = config.get("BEST_IS_MIN", False)
    entry_data = {}

    overall_b = None
    overall_b_epoch = None
    overall_b_name = None

    for k, v in report_vals.items():
        b = min(v) if b_is_min else max(v)  # Best
        eb = v.index(b)  # Best epoch
        l = v[-1]  # Last
        el = len(v)  # Last epoch

        entry_data[k] = {"b": b, "eb": eb, "l": l, "el": el}

        if overall_b is None or (b < overall_b and b_is_min) or (b > overall_b and not b_is_min):
            overall_b = b
            overall_b_epoch = eb
            overall_b_name = k

    entry_strs = [f"{k}:\nBest (Epoch {v['eb']}): {v['b']}\nLast (Epoch {v['el']}): {v['l']}"
                  for k, v in entry_data.items()]

    if overall_b is not None:
        entry_strs.append(f"Overall best:\nName: {overall_b_name}\nValue (Epoch {overall_b_epoch}): {overall_b}")

    return f"{config['TITLE']}\n\n{(lb*2).join(entry_strs)}"



def report(history_data, config):
    reports = [get_report(history_data, cfg) for cfg in config["REPORTS"]]
    report_str = f"{config['TITLE']}\n\n\n{(lb*3).join(reports)}"

    if config["OUTPUT"] == "print":
        print(report_str)

    elif config["OUTPUT"] == "txt":
        p = ensure_file_ext(config["PATH"], "txt")
        with open(p, 'w') as f:
            f.write(report_str)

    elif config["OUTPUT"] == "md":
        p = ensure_file_ext(config["PATH"], "md")
        with open(p, 'w') as f:
            f.write(txt_str_to_md(report_str, bullet_consecutive_lines=True))


def analyse(history_data, config):
    if "GRAPHING" in config.keys():
        graphing(history_data, config["GRAPHING"])
    if "REPORT" in config.keys():
        report(history_data, config["REPORT"])



def analyse_mode(config):
    v = True
    printv("[I] In analyse mode", verbose_flag=v)

    printv("[I] Fetching history data...", verbose_flag=v)
    history_data = get_models_history(config["HISTORY_DATA"])

    printv("[I] Analysing...", verbose_flag=v)
    analyse(history_data, config["ANALYSIS"])

