import src.gitutils.command as command
from src.gitutils.utils import *

        os.chdir(self.tmpdir)
        if not os.path.exists(filepath):
            return '',getYears(reponame)
    # TODO: default args for since and until
    def getRepoCommitData(self, reponame, includebranches = False, since = None, until = None):
        for version in versions:


        retcode, out, err = command.Command(f'git log -p --date=iso-strict-local --function-context --since {since} --until {until}').run()
            #If the line is an author, then start to piece together the commit
                commitid = commitid.decode('utf-8')
                    else:
                        try:
                            m = ''

                                    if diff.startswith(b'diff'):

                                if not line.startswith(b'deleted file mode') and not line.startswith(b'old mode'):

                                            diffinfo.append(diff.decode("utf-8", errors='ignore'))
                                        elif diff.startswith(b'diff'):


                                    #ignore deleted files for now
                        print('Done with commits from this repo.')


                #ignore anything else until next author line
        for version in versions:


            #If the line is an author, then start to piece together the commit
                        try:
                            m = ''

                                    if diff.startswith(b'diff'):

                                if not line.startswith(b'deleted file mode') and not line.startswith(b'old mode'):

                                            diffinfo.append(diff.decode("utf-8", errors='ignore'))
                                        elif diff.startswith(b'diff'):


                                    #ignore deleted files for now
                    except:


                #ignore anything else until next author line
