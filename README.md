# infrastructure
Some infrastructure-related scripts and automations

# Installation

You should follow the guides of each tool to install them (but I suggest you use `make install` on the roles directory to install Ansible and Molecule).

- Ansible
- Molecule
- Vagrant
- Terraform
- Packer
- gocd cli

# Molecule

## Create new role

`ROLE=rolename DRIVER=vagrant make create-role`

## Testing it

You can test a role by using:

`ROLE=rolename make test` or `ROLE=rolename make test-no-destroy` (the latter won't destroy the instance after testing).

You can then destroy the instance by using:

`ROLE=rolename make destroy`