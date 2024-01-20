# Install flask from provider pip3 using puppet
# The flask should be of v2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
