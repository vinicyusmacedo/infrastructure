DRIVER=vagrant

install:
	pip install -r requirements.txt

create-role:
	cd ${PWD}/ansible/roles && molecule init role -r ${ROLE} -d ${DRIVER}

converge:
	cd ${PWD}/ansible/roles && molecule converge

test:
	cd ${PWD}/ansible/roles/${ROLE} && molecule test

test-no-destroy:
	cd ${PWD}/ansible/roles/${ROLE} && molecule test --destroy never

verify:
	cd ${PWD}/ansible/roles/${ROLE} && molecule verify

destroy:
	cd ${PWD}/ansible/roles/${ROLE} && molecule destroy

login:
	cd ${PWD}/ansible/roles/${ROLE} && molecule login

start-vagrant:
	cd ${PWD}/ansible/${PLAYBOOK} && ANSIBLE_ROLES_PATH=${PWD}/ansible/roles vagrant up --provision

ssh-vagrant:
	cd ${PWD}/ansible/${PLAYBOOK} && vagrant ssh

destroy-vagrant:
	cd ${PWD}/ansible/${PLAYBOOK} && vagrant destroy

check-gocd:
	gocd configrepo syntax --yaml ${FILENAME}
