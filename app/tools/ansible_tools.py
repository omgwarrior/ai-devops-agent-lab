def ansible_nginx_playbook_tool():
    return {
        "tool": "ansible_nginx_playbook_tool",
        "description": "Generates a basic Ansible playbook to install and start nginx.",
        "playbook": """---
- name: Install and start nginx
  hosts: web
  become: true

  tasks:
    - name: Install nginx
      ansible.builtin.package:
        name: nginx
        state: present

    - name: Start and enable nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
"""
    }


def ansible_inventory_skeleton_tool():
    return {
        "tool": "ansible_inventory_skeleton_tool",
        "description": "Generates a basic Ansible inventory skeleton.",
        "inventory": """all:
  children:
    web:
      hosts:
        web01:
          ansible_host: 10.0.1.10
        web02:
          ansible_host: 10.0.1.11

    database:
      hosts:
        db01:
          ansible_host: 10.0.2.10
"""
    }
