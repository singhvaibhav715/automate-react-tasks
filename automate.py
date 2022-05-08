import sys
import os
from typing import final
n = len(sys.argv)


def insert_boilerplate_code(path, componentName, isCss):
    code_with_css = f"""
    import React from 'react'
import "./{componentName}.css"
const {componentName} = () => {{
    return (
        <div></div>
    )
}}

export default {componentName}
    
    """
    code_without_css = f"""
    import React from 'react'
const {componentName} = () => {{
    return (
        <div></div>
    )
}}

export default {componentName}
    
    """

    with open(path, 'a') as file:
        if isCss:
            file.write(code_with_css.strip())
        else:
            file.write(code_without_css.strip())


def create_component_with_css(path, component):
    create_dir_cmd = 'mkdir ' + path + '\\' + component
    create_file = "type NUL > " + path + "\\" + \
        component+"\\"+component.capitalize()
    create_js_cmd = create_file+".js"
    create_css_cmd = create_file+".css"
    os.system(create_dir_cmd)
    os.system(create_js_cmd)
    os.system(create_css_cmd)
    new_path = "/".join(path.split("\\"))
    insert_boilerplate_code(
        new_path + "/" + component+"/"+component.capitalize()+".js", component.capitalize(), True)
    print(component, "Component Created...")


def create_component_without_css(path, component):
    create_dir_cmd = 'mkdir ' + path + '\\' + component
    create_file = "type NUL > " + path + "\\" + \
        component+"\\"+component.capitalize()
    create_js_cmd = create_file+".js"
    os.system(create_dir_cmd)
    os.system(create_js_cmd)
    new_path = "/".join(path.split("\\"))
    insert_boilerplate_code(
        new_path + "/" + component+"/"+component.capitalize()+".js", component.capitalize(), False)
    print(component, "Component Created...")


if sys.argv[1] == "default-path":
    if sys.argv[2] == "include-css":
        for component in sys.argv[3:]:
            create_component_with_css("src\\components", component)

    if sys.argv[2] == "no-css":
        for component in sys.argv[3:]:
            create_component_without_css("src\\components", component)

if sys.argv[1] == "custom-path":
    path = sys.argv[2].split(">")
    final_path = "\\".join(path)
    if sys.argv[3] == "include-css":
        for component in sys.argv[4:]:
            create_component_with_css(final_path, component)
    if sys.argv[3] == "no-css":
        for component in sys.argv[4:]:
            create_component_without_css(final_path, component)
