# install flask from provider pip3 using puppet

pack { 'flask':
  ensure  => '2.1.0',
  provider => pip3,
}
