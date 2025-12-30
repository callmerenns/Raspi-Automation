#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from ruamel.yaml import YAML
from jsonpointer import resolve_pointer, set_pointer
import os

yaml = YAML()
yaml.preserve_quotes = True     # Penting! menjaga kutip
yaml.indent(mapping=2, sequence=4, offset=2)


def main():
    module_args = dict(
        src=dict(type='path', required=True),
        edits=dict(type='list', required=True)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    src = module.params['src']
    edits = module.params['edits']

    if not os.path.exists(src):
        module.fail_json(msg=f"Source file {src} not found")

    try:
        with open(src, "r") as f:
            data = yaml.load(f)
    except Exception as e:
        module.fail_json(msg=f"Failed loading YAML: {e}")

    changed = False

    for edit in edits:
        op = edit["op"]
        path = edit["path"]
        value = edit["value"]

        if isinstance(value, str):
            value = f'{value}'  # pastikan tetap string

        try:
            # Check existing value
            try:
                current = resolve_pointer(data, path)
            except:
                current = None

            if op == "replace":
                if current != value:
                    set_pointer(data, path, value, inplace=True)
                    changed = True

        except Exception as e:
            module.fail_json(msg=f"Error applying patch {edit}: {e}")

    if changed:
        try:
            with open(src, "w") as f:
                yaml.dump(data, f)
        except Exception as e:
            module.fail_json(msg=f"Failed writing YAML: {e}")

    module.exit_json(changed=changed, msg="YAML updated successfully")


if __name__ == '__main__':
    main()
