# Convert SVG files into Vue3 (Composition API) Components

The problem was, that there were alot of SVG not only to be convertet into Vue components, but alsoo the SVG code needed to be cleaned up.

So I automated this task with Python.

## Usage
``python3 convert_svg_into_vue.py``

You will be promted with: ``Path to the SVGs?:``
Just put the path to the folder that includes the SVGs.
Within the given folder the script will create a subfolder named 'vue'.

## SVG cleanup
Most of the SVG codes contain unnessacary chunks. The script converts this:

``` HTML
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
    <g id="arrow-top" transform="matrix(-1.53081e-16,-2.5,-2.5,1.53081e-16,100,100)">
        <path d="M20,0C25.304,0 30.391,2.107 34.142,5.858C37.893,9.609 40,14.696 40,20C40,25.304 37.893,30.391 34.142,34.142C30.391,37.893 25.304,40 20,40C14.696,40 9.609,37.893 5.858,34.142C2.107,30.391 0,25.304 0,20C0,14.696 2.107,9.609 5.858,5.858C9.609,2.107 14.696,0 20,0ZM4,20C4,24.244 5.686,28.313 8.686,31.314C11.687,34.314 15.757,36 20,36C24.244,36 28.313,34.314 31.314,31.314C34.314,28.313 36,24.244 36,20C36,15.757 34.314,11.687 31.314,8.686C28.313,5.686 24.244,4 20,4C15.757,4 11.687,5.686 8.686,8.686C5.686,11.687 4,15.757 4,20ZM25.08,21.4L18,28.5L15.18,25.68L20.8,20L15.2,14.34L18,11.52L26.48,20L25.08,21.4Z" style="fill-rule:nonzero;"/>
    </g>
</svg>
```

into this:

``` HTML
  <svg
    v-bind="$attrs"
    viewBox="0 0 100 100"
    xmlns="http://www.w3.org/2000/svg"
    xml:space="preserve"
    style="fill-rule: evenodd; clip-rule: evenodd; stroke-linejoin: round; stroke-miterlimit: 2"
  >
    <path d="M20,0C25.304,0 30.391,2.107 34.142,5.858C37.893,9.609 40,14.696 40,20C40,25.304 37.893,30.391 34.142,34.142C30.391,37.893 25.304,40 20,40C14.696,40 9.609,37.893 5.858,34.142C2.107,30.391 0,25.304 0,20C0,14.696 2.107,9.609 5.858,5.858C9.609,2.107 14.696,0 20,0ZM4,20C4,24.244 5.686,28.313 8.686,31.314C11.687,34.314 15.757,36 20,36C24.244,36 28.313,34.314 31.314,31.314C34.314,28.313 36,24.244 36,20C36,15.757 34.314,11.687 31.314,8.686C28.313,5.686 24.244,4 20,4C15.757,4 11.687,5.686 8.686,8.686C5.686,11.687 4,15.757 4,20ZM25.08,21.4L18,28.5L15.18,25.68L20.8,20L15.2,14.34L18,11.52L26.48,20L25.08,21.4Z" style="fill-rule:nonzero;"/>
  </svg>
```

## The component
The component mainly consits of a template providing the SVG.

``` javascript
<script setup></script>
<template>
  <svg
    v-bind="$attrs"
    viewBox="0 0 100 100"
    xmlns="http://www.w3.org/2000/svg"
    xml:space="preserve"
    style="fill-rule: evenodd; clip-rule: evenodd; stroke-linejoin: round; stroke-miterlimit: 2"
  >
    <path d="M20,0C25.304,0 30.391,2.107 34.142,5.858C37.893,9.609 40,14.696 40,20C40,25.304 37.893,30.391 34.142,34.142C30.391,37.893 25.304,40 20,40C14.696,40 9.609,37.893 5.858,34.142C2.107,30.391 0,25.304 0,20C0,14.696 2.107,9.609 5.858,5.858C9.609,2.107 14.696,0 20,0ZM4,20C4,24.244 5.686,28.313 8.686,31.314C11.687,34.314 15.757,36 20,36C24.244,36 28.313,34.314 31.314,31.314C34.314,28.313 36,24.244 36,20C36,15.757 34.314,11.687 31.314,8.686C28.313,5.686 24.244,4 20,4C15.757,4 11.687,5.686 8.686,8.686C5.686,11.687 4,15.757 4,20ZM25.08,21.4L18,28.5L15.18,25.68L20.8,20L15.2,14.34L18,11.52L26.48,20L25.08,21.4Z" style="fill-rule:nonzero;"/>
  </svg>
</template>
```

## The Filename
The script converts the given file name into camel case. Therefore it removes all hyphens, pipes and underscrores. I prefer to have a prefix of 'Icon'. So `icon-whatsapp.svg` becomes `IconWhatsapp.vue`