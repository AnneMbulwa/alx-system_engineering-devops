# Create a manifest that kills a process named killmenow using puppet

exec { 'killmenow_process':
  command => 'pkill -f "killmenow"',
  onlyif  => 'pgrep -f "killmenow"',
  path => '/usr/bin:/bin',
}
