from fabric.contrib.files import import append, exists, sed
from fabric.api import import env, local, run
import random

env.forward_agent = True
env.use_ssh_config = True

REPO_URL = 'https://github.com/deadlylaid/TDD_Test.git'

def deploy():

    run("sudo apt-get update")
    run("sudo apt-get upgrade -y")
    run("sudo apt-get install git nginx")
    project_folder = '/home/ubuntu/TDD_Test'
    _get_latest_source(project_folder)
    _update_settings(project_folder)
    _update_pyenv_virtualenv(project_folder)
    _update_static_files(project_folder)
    _update_database(project_folder)


def _get_latest_source(project_folder):

    if exists(project_folder + '/.git'):
        run('cd %s && git fetch' % (project_folder, ))
    else :
        run('git clone %s' %(REPO_URL))


def _update_settings(project_folder):

    settings_path = project_folder + '/superlists/superlists/settings.py'
    sed(settings_path, 'DEBUG = True', "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        'ALLOWED_HOSTS = ["tddgoat2.amull.net"]'
    )


def _update_pyenv_virtualenv(project_folder):

    bash_profile = '~/.bash_profile'

    if not exists(bash_profile):
        run('touch ~/.bash_profile')
    run('sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils')

    run('curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash')

    append(bash_profile, 'export PATH="~/.pyenv/bin:$PATH"')
    append(bash_profile, 'eval "$(pyenv init -)"')
    append(bash_profile, 'eval "$(pyenv virtualenv-init -)"')
    run('source .bash_profile')

#    run('pyenv install 3.5.1')
#    run('pyenv virtualenv 3.5.1 TDD_Test')
    run('source ~/.pyenv/versions/TDD_Test/bin/activate TDD_Test')
    run('cd TDD_Test && /home/ubuntu/.pyenv/versions/TDD_Test/bin/pip install -r requirements.txt')


def _update_static_files(project_folder):

    run('cd TDD_Test && ~/.pyenv/versions/TDD_Test/bin/python superlists/manage.py collectstatic --noinput')

def _update_database(project_folder):

    run('mkdir -p %s' % (project_folder + '/database'))
    run('cd %s && ~/.pyenv/versions/TDD_Test/bin/python superlists/manage.py makemigrations lists' % (project_folder,))
    run('cd %s && ~/.pyenv/versions/TDD_Test/bin/python superlists/manage.py migrate' % (project_folder,))
