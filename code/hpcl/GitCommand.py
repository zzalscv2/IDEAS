        
        os.chdir(self.tmpdir) 
        
        os.chdir(self.tmpdir)   
        if not os.path.exists(filepath): 
            return '',getYears(reponame) 
    def getRepoCommitData(self, reponame, includebranches = False):
                commitid = commitid.strip('\n')
                branches = ''
                if includebranches:
                    retcode, branches, err = Command.Command('git branch -a --contains %s' % commitid).run()
                    try:
                        diff = next(lines)
                        while len(diff) > 0 and diff.startswith(b'\\') == False:
                            if diff.startswith(b'diff'):
                                #next(lines)
                                #next(lines)
                                #next(lines)
                                filenameline = diff.decode("utf-8")
                                filename = filenameline[11:len(filenameline)]
                                #print('FILENAME '+ filename)
                         
                                line = next(lines)

                                #skip extra line if this line is seen
                                    if diff.startswith(b'diff'): 
                                        break
                                
                                if not line.startswith(b'deleted file mode') and not line.startswith(b'old mode'): 
                                  
                                    #skip just one line if this line is seen
                                    if line.startswith(b'new file mode'):
                                        next(lines)

                                    else:
                                        next(lines)
                                        next(lines)

                                    #skip ahead until see first + or -
                                    diff = next(lines)
                                    while not (diff.startswith(b'+') or diff.startswith(b'-')) or (diff.startswith(b'+++') or diff.startswith(b'---')) :
                                        diff = next(lines)
                                    diffinfo = []
                                    while len(diff) >= 1:
                                        if (diff.startswith(b'+') or diff.startswith(b'-')):
                                            diffinfo.append(diff.decode("utf-8", errors='ignore')) 
                                        elif diff.startswith(b'diff'): 
                                            break
                                        elif len(diff) < 2:
                                            try:
                                                diff = next(lines)
                                                if len(diff) < 2:
                                                    break
                                            except:
                                                break
                                        
                                    diffs.append({'filename':filename, 'diff':diffinfo})
                                                                
                                #else:
                                    #ignore deleted files for now   
                            else:
                                try:
                                    diff = next(lines)
                                except:
                                    break
                    except:
                        print('Done with commits from this repo.')                
                    
    def getAllCommits(self, reponame, includebranches = False):
                commitid = commitid.strip('\n')
                branches = ''
                if includebranches:
                    retcode, branches, err = Command.Command('git branch -a --contains %s' % commitid).run()
                    try:
                        diff = next(lines)
                        while len(diff) > 0 and diff.startswith(b'\\') == False:
                            if diff.startswith(b'diff'):
                                #next(lines)
                                #next(lines)
                                #next(lines)
                                filenameline = diff.decode("utf-8")
                                filename = filenameline[11:len(filenameline)]
                                #print('FILENAME '+ filename)
                         
                                line = next(lines)

                                #skip extra line if this line is seen
                                    if diff.startswith(b'diff'): 
                                        break
                                
                                if not line.startswith(b'deleted file mode') and not line.startswith(b'old mode'): 
                                  
                                    #skip just one line if this line is seen
                                    if line.startswith(b'new file mode'):
                                        next(lines)

                                    else:
                                        next(lines)
                                        next(lines)

                                    #skip ahead until see first + or -
                                    diff = next(lines)
                                    while not (diff.startswith(b'+') or diff.startswith(b'-')) or (diff.startswith(b'+++') or diff.startswith(b'---')) :
                                        diff = next(lines)
                                    diffinfo = []
                                    while len(diff) >= 1:
                                        if (diff.startswith(b'+') or diff.startswith(b'-')):
                                            diffinfo.append(diff.decode("utf-8", errors='ignore')) 
                                        elif diff.startswith(b'diff'): 
                                            break
                                        elif len(diff) < 2:
                                            try:
                                                diff = next(lines)
                                                if len(diff) < 2:
                                                    break
                                            except:
                                                break
                                        
                                    diffs.append({'filename':filename, 'diff':diffinfo})
                                                                
                                #else:
                                    #ignore deleted files for now   
                            else:
                                try:
                                    diff = next(lines)
                                except:
                                    break
                    except:                
                        print('Done with commits for this repo.')
                    



                    