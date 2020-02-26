#!/usr/bin/env python3
import sys, os
import Input
import ls
import lsl
import cat
import head
import tail
import passw
import grep
import wc
#import cd
import mkdir
import rm
import history
import who
import exit
import shlex
#from CommandHelper import CommandHelper


class CommandHelper(object):
  def __init__(self):
      self.commands = {}
      self.commands['ls'] = ls.ls
      self.commands['ls-a'] = lsl.ls
      self.commands['cat'] = cat.cat
      self.commands['head'] = head.head
      self.commands['tail'] = tail.tail
      self.commands['pwd'] = passw.pwd
      self.commands['grep'] = grep.grep
      self.commands['wc'] = wc.wc
      #self.commands['cd'] = cd.cd
      self.commands['mkdir'] = mkdir.mkdir
      self.commands['rm'] = rm.rm
      self.commands['history'] = history.history
      self.commands['who'] = who.who
      self.commands['x'] = exit.exit

  def invoke(self, **kwargs):
      if 'cmd' in kwargs:
          cmd = kwargs['cmd']
      else:
          cmd = ''

      if 'params' in kwargs:
          params = kwargs['params']
      else:
          params = []

      if 'flags' in kwargs:
          flags = kwargs['flags']
      else:
          flags = []

      if 'thread' in kwargs:
          thread = kwargs['thread']
      else:
          thread = False

      # One way to invoke using dictionary
      if not thread:
          params[:] = [p.lower() for p in params]     
          self.commands[cmd](params=params,flags=flags)
      # else:
      #     # Using a thread ****** broken right now *********
      #     if len(params) > 0:
      #         c = threading.Thread(target=self.commands[cmd], args=tuple(kwargs))
      #     else:
      #         c = threading.Thread(target=self.commands[cmd])

          # c.start()
          # c.join()
      
  def exists(self, cmd):
      return cmd in self.commands


ch = CommandHelper()

while 1: 
    command_input = input('% ')

    Input.recordHistory(command_input)
    
    command = command_input.split()[0]

    #shlex helps split on strings with quotes around it.
    #example - file names with spaces - "some file.txt"
    cmd_params = shlex.split(' '.join(command_input.split()[1:],)) #, posix=False

    #cmd_params = command_input.split()[1:]

    flag_params = []
    
    for flag in cmd_params:
        if '-' in flag:
            flag_params.append(flag)
            cmd_params.remove(flag)


    # if command exists in our shell
    if ch.exists(command):
        ch.invoke(cmd=command, params=cmd_params, flags=flag_params, thread=False)
    else:
        print("Error: command %s doesn't exist." % (command))

    path = os.getcwd() # use .getcwd to get the path of current location