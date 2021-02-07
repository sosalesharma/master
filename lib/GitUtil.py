import json
import sys
import logging as logger
import git
import re
import lib.CommonUtil as utility
from git import Repo
from git import RemoteProgress

class GitUtility():

    def verify_git_branch(self, repo_path, git_branch, git_branch_re):
        status = False
        git_repo = git.Repo(repo_path)
        if git_repo:
            git_status = (git_repo.git.status())
            reg_result = re.search(git_branch_re, git_status)
            if git_branch == reg_result.group(1):
                print(reg_result.group(1))
                print("Git repo is in %s branch and is mapped to valid branch" % reg_result.group(1))
                status = True
            else:
                print("Git repo is in %s branch and is not valid branch, checking out to valid branch" % reg_result.group(1))
                git_repo.git.checkout(git_branch)
                git_status = (git_repo.git.status())
                reg_result = re.search(git_branch_re, git_status)
                if git_branch == reg_result.group(1):
                    print(reg_result.group(1))
                    print("Git repo is in %s branch and is mapped to valid branch" % reg_result.group(1))
                    status = True
                else:
                    print("Git repo is in %s branch and is not valid branch. Abort !!!" % reg_result.group(1))
        else:
            print("Not a git repository, please set valid repository")
        return status


    def git_pull_oper(self, repo_path, git_branch, git_branch_re, git_pull_success_status):
        status = False
        git_repo = git.Repo(repo_path)
        if GitUtility.verify_git_branch(repo_path, git_branch, git_branch_re):
            git_pull_status = git_repo.git.pull()
            if git_pull_success_status in git_pull_status:
                print("Git branch %s is up to date" % git_branch)
                status = True
            else:
                print("Operation git pull failed, Abort !!! ")
        else:
            print("Directory is not a git repo or git repo is not mapped to appropriate branch")
        return status

    def git_push_oper(self, repo_path, jira_ticket):
            status = False
            git_repo = git.Repo(repo_path)
            git_status = (git_repo.git.status())
            #track_files = ['CommonUtil.py', 'variableFile.py']
            #re_add_files = '((?:[A-Za-z_]+\/){1,10}[A-Za-z]+(?:(?:.json)|(?:.xml)))'
            re_add_files = '((?:[A-Za-z_]+\/){1,10}[A-Za-z]+(?:(?:.py)))'
            git_add_files = re.findall(re_add_files, git_status)
            for files in git_add_files:
                git_repo.git.add(files)

            git_repo.git.commit(m=jira_ticket)
            origin = git_repo.remote(name='origin')
            git_push_status = origin.push()
            return git_push_status