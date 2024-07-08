from jinja2 import Template
import codecs
import json
from pathlib import Path
from slugify import slugify
from tqdm import tqdm
import os
import shutil
import matplotlib.pyplot as plt

slugs = []
blacklist = [
    "PCI\VEN_1002&DEV_164E&SUBSYS_D0001458&REV_C2 Ryzen",
    "PCI\VEN_1002&DEV_164E&SUBSYS_D0001458&REV_C3 Ryzen",
    "PCI\VEN_1002&DEV_164E&SUBSYS_D0001458&REV_C6 Ryzen",
    "PCI\VEN_1002&DEV_164E&SUBSYS_D0001458&REV_C7 Ryzen",
]

for item in os.listdir("../content"):
        item_path = os.path.join("../content", item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)

with open("gpu_data.json", "r") as handle:
    gpu_data_list = json.loads(handle.read())["data"]

for gpu_data in tqdm(gpu_data_list):
    if "name" not in gpu_data:
        continue
    if "g3d" not in gpu_data:
        continue
    if gpu_data["name"] in blacklist:
        continue

    template_data = {}
    template_data["gpu_name"] = gpu_data["name"]
    template_data["score"] = int(gpu_data["g3d"].replace(",", ""))
    percentage = int(gpu_data['g3d'].replace(',', '')) / 38743 * 100
    template_data["percentage"] = f"{percentage:.2f}"

    classroom_render_time_current_classroom = int(20 * 38743 / template_data["score"])
    hours_classroom = int(classroom_render_time_current_classroom / 60)
    minutes_classroom = classroom_render_time_current_classroom - 60 * hours_classroom
    template_data["classroom_render_time_current"] = f"{hours_classroom if hours_classroom > 0 else ''}{'h ' if hours_classroom > 0 else ''}{minutes_classroom} minutes"
    template_data["classroom_render_time_gtx_1080"] = "50 minutes"
    template_data["classroom_render_time_rtx_2060"] = "55 minutes"
    template_data["classroom_render_time_rtx_4090"] = "20 minutes"
    template_data["classroom_render_time_renderlab"] = "4 minutes"
    template_data["classroom_price_renderlab"] = "$0.00"

    classroom_render_time_current_architecture = int(15 * 38743 / template_data["score"])
    hours_architecture = int(classroom_render_time_current_architecture / 60)
    minutes_architecture = classroom_render_time_current_architecture - 60 * hours_architecture
    template_data["architecture_render_time_current"] = f"{hours_architecture if hours_architecture > 0 else ''}{'h ' if hours_architecture > 0 else ''}{minutes_architecture} minutes"
    template_data["architecture_render_time_gtx_1080"] = "37 minutes"
    template_data["architecture_render_time_rtx_2060"] = "41 minutes"
    template_data["architecture_render_time_rtx_4090"] = "15 minutes"
    template_data["architecture_render_time_renderlab"] = "3 minutes"
    template_data["architecture_price_renderlab"] = "$0.00"


    with open("template.md", "r") as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(template_data=template_data)

    count = 1
    while True:
        slug = slugify(gpu_data["name"])
        if count > 1:
            slug += f"-{count}"

        if slug in slugs:
            count += 1
            continue

        slugs.append(slug)
        break

    Path(f"../content/{slug}").mkdir(parents=True, exist_ok=True)

    output_file = codecs.open(f"../content/{slug}/index.md", "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()
    output_file.close()

    # potting
    data = [
        [template_data["gpu_name"], template_data["score"]],
        ["GeForce GTX 1080", 15526],
        ["GeForce RTX 2060", 14149],
        ["GeForce RTX 4090", 38743],
    ]

    labels = [item[0] for item in data]
    values = [item[1] for item in data]

    colors = ['orange'] + ['blue'] * (len(data) - 1)

    # Creating the bar plot
    plt.bar(labels, values, color=colors)

    # Labeling the axes
    plt.xlabel('GPUs')
    plt.ylabel('3DMark Score')

    plt.xticks(rotation=90, ha='left')

    plt.tight_layout()

    plt.savefig(f"../content/{slug}/comparison.svg", transparent=True)

    plt.show()
