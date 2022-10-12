import os
import re

f = input('Path to the SVGs?: ')
regex = re.compile(r'<path(?=\s)(?!(?:[^>"\']|"[^"]*"|\'[^\']*\')*?(?<=\s)(?:term|range)\s*=)(?!\s*/?>)\s+(?:".*?"|\'.*?\'|[^>]*?)+>', re.IGNORECASE)


def camel_case(s):
    regex_file = re.compile(r'(_|-)+', re.IGNORECASE)
    s = re.sub(regex_file, " ", s).title().replace(" ", "")
    return ''.join([s[0].upper(), s[1:]])

for dir_path, dir_names, file_names in os.walk(f):
    files = [file for file in file_names if file.endswith(".svg")]
    for f_name in files:
        file_path = os.path.join(dir_path, f_name)

        with open(file_path, 'rb') as r:
            if (r == ".DS_Store"):
                continue

            svg = r.read().decode('UTF-8').replace('\n', '')
            path_tag = re.search(regex, svg)
            new_filename = camel_case(f_name).replace('.Svg', '.vue')

            new_path = os.path.join(dir_path, 'vue')
            os.makedirs(new_path, exist_ok=True)
            new_file_path = os.path.join(new_path, new_filename)

            with open(new_file_path, 'w') as new_file:
                file_template = f"""<script setup></script>
<template>
  <svg
    v-bind="$attrs"
    viewBox="0 0 100 100"
    xmlns="http://www.w3.org/2000/svg"
    xml:space="preserve"
    style="fill-rule: evenodd; clip-rule: evenodd; stroke-linejoin: round; stroke-miterlimit: 2"
  >
    {path_tag[0]}
  </svg>
</template>"""
                new_file.write(file_template)


