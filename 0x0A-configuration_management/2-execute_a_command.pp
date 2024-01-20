# Create a manifest that kills a process named killmenow using puppet
exec { 'killmenow_process':
  command  => 'pkill -9 killmenow',
  path     => '/usr/bin:/bin',
  onlyif   => 'pgrep killmenow',

}
