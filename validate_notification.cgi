#!C:/Strawberry/perl/bin/perl.exe


use strict;
use warnings;
use CGI;

my $cgi = CGI->new;

# Read parameters from CGI
my $user_name = $cgi->param('user_name');
my $notify_me = $cgi->param('notify_me');

# Initialize result structure
my %results = (
    correct_params => [],
    incorrect_params => [],
    missing_params => [],
);

# Validate user_name (mandatory)
if (defined $user_name && $user_name ne '') {
    push @{$results{correct_params}}, 'user_name';
} else {
    push @{$results{missing_params}}, 'user_name';
}

# Validate notify_me (mandatory parameter name but optional value)
if (defined $notify_me) {
    # The value of notify_me can be empty or any other value
    push @{$results{correct_params}}, 'notify_me';
} else {
    push @{$results{missing_params}}, 'notify_me';
}

# Output results
print $cgi->header('text/plain');
print "Correct Parameters: ", join(", ", @{$results{correct_params}}), "\n";
print "Incorrect Parameters: ", join(", ", @{$results{incorrect_params}}), "\n";
print "Missing Parameters: ", join(", ", @{$results{missing_params}}), "\n";

__END__
