import json
from typing import Union


def a_avg(xs):
    return sum(xs)/len(xs)


def get_table_str(caption: str, data: dict[str,dict[str,str]]):
    headings = ["accuracy", "precision", "recall", "f1"]
    heading_str = f"& {' & '.join(headings)} \\\\"

    def get_cols_of_row(d):
        return ' & '.join(f"{d[k]:.3f}" for k in headings)

    data_strs = [f"{k} & {get_cols_of_row(v)} \\\\"
                 for k, v in data.items()]
    row_strs = "\n        ".join(data_strs)

    def get_cols_of_mean():
        return ' & '.join(f"{a_avg([v[k] for v in data.values()]):.3f}" for k in headings)
    mean_str = f"mean & {get_cols_of_mean()} \\\\"

    return f"""\\begin{{table}}[htb]
    \\caption{{{caption}}}
    \\centering
    \\begin{{tabular}}{{c | c c c c}}
        {heading_str}
        \\hline
        {row_strs}
        {mean_str}
    \\end{{tabular}}
\\end{{table}}"""


def get_val_test_tag_stats(db, model_id: Union[str, list[str]]
                           ) -> tuple[dict[str,dict[str,str]],dict[str,dict[str,str]]]:
    if isinstance(model_id, list):
        assert len(model_id) >= 2
        val_accs_all_epochs_all_models = [db[m_id]["history"]["validation_accuracies"]
                                          for m_id in model_id]
        val_accs_all_epochs = val_accs_all_epochs_all_models[0]

        for v in val_accs_all_epochs_all_models[1:]:
            for i, d in enumerate(v):
                val_accs_all_epochs[i].update(d)

        test_accs_all_models = [db[m_id]["testing"]["accuracy"]
                                for m_id in model_id]
        test_accs = test_accs_all_models[0]

        for v in test_accs_all_models[1:]:
            test_accs.update(v)

    else:
        val_accs_all_epochs = db[model_id]["history"]["validation_accuracies"]
        test_accs = db[model_id]["testing"]["accuracy"]

    val_accs_f1_means = [a_avg([prf1a["f1"] for prf1a in epoch.values()])
                         for epoch in val_accs_all_epochs]
    val_accs = val_accs_all_epochs[val_accs_f1_means.index(max(val_accs_f1_means))]

    return val_accs, test_accs


def print_tag_stats(db):
    model_stat_output_model_type_ids = {
        "BioBERT multi-head": "BioBERTv11_multi_output_v2_single_label_bio_bl05_k4_e36_2023-07-26_00-19",
        "BioClinicalBERT multi-head": "BioBERTv11_multi_output_v2_single_label_bio_bl05_k4_e36_2023-07-27_19-55",
        "BERTBase": "BERTBase_multi_output_v2_single_label_bio_bl05_k4_e36_2023-08-01_18-30",
        "BioBERT single-heads": [
            "BioBERTv11_category_v2_single_label_bio_bl05_k4_e36_2023-08-15_16-10",
            "BioBERTv11_perturbing_action_v2_single_label_bio_bl05_k4_e36_2023-08-15_18-42",
            "BioBERTv11_context_v2_single_label_bio_bl05_k4_e36_2023-08-15_21-15",
            "BioBERTv11_effect_v2_single_label_bio_bl05_k4_e36_2023-08-15_23-47",
            "BioBERTv11_phenotype_v2_single_label_bio_bl05_k4_e36_2023-08-17_16-12",
        ],
        "BioBERT link both heads": "BioBERTv11_link_both_heads_v2_bl05_k4_2023-07-25_15-24",
        "BioClinicalBERT link both heads": "BioBERTv11_link_both_heads_v2_bl05_k4_2023-07-27_15-24",
        "BERTBase link both heads": "BERTBase_link_both_heads_v2_bl05_k4_2023-08-01_13-59",
        "BioBERT link only": "BioBERTv11_link_only_v2_bl05_k4_2023-08-15_13-36",
    }

    for model_type, model_id in model_stat_output_model_type_ids.items():
        val_tag_stats, test_tag_stats = get_val_test_tag_stats(db, model_id)
        print(get_table_str(f"Validation stats for {model_type}", val_tag_stats))
        print("\n")
        print(get_table_str(f"Testing stats for {model_type}", test_tag_stats))
        print("\n")


if __name__ == "__main__":
    with open("outputs/outputs_db.json") as f:
        db = json.load(f)
    print_tag_stats(db)

