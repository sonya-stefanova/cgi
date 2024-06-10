#!C:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new();
print $cgi->header(
    -type => 'text/html',
    -status => '200 OK'
);

my $name = $cgi->param('name') || 'Guest';
my $gender = $cgi->param('gender') || 'Not specified';
my $profession = $cgi->param('profession') || 'Not specified';
my @sports = $cgi->param('sport');

my $list;

if (@sports) {
    $list = join ', ', @sports;
} else {
    $list = 'Not provided';
}

print <<HTML;
<!doctype html>
<html>
<head>
    <title>Hello CGI</title>
</head>
<body>
    <h1>Hello, $name!</h1>
    <p>You have Submitted the following Data:</p>
    <table border="1">
        <tr>
            <td>Name:</td>
            <td>$name</td>
        </tr>
        <tr>
            <td>Gender:</td>
            <td>$gender</td>
        </tr>
        <tr>
            <td>Profession:</td>
            <td>$profession</td>
        </tr>
        <tr>
            <td>Sports:</td>
            <td>$list</td>
        </tr>
    </table>
</body>
</html>
HTML
