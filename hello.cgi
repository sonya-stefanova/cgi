#!C:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new();
print $cgi->header('text/html');

my $name = $cgi->param('name') || 'Guest';

print <<HTML;
<!doctype html>
<html>
<head>
    <title>Hello CGI</title>
</head>
<body>
    <h1>Hello, $name!</h1>
</body>
</html>
HTML
