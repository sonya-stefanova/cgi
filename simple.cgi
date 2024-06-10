#!C:/Strawberry/perl/bin/perl.exe

use strict;
use warnings;
use CGI;

my $cgi = CGI->new;

# Expected values for favorite_color
my @valid_colors = qw(red green blue);

# Read parameters from CGI
my $user_name      = $cgi->param('user_name');
my $age            = $cgi->param('age');
my $favorite_color = $cgi->param('favorite_color');

# Initialize results
my %results = (
    correct_params    => [],
    incorrect_params  => [],
    missing_params    => [],
    unexpected_params => [],
);

# Validate user_name (mandatory)
if (defined $user_name && $user_name ne '') {
    push @{$results{correct_params}}, 'user_name';
} else {
    push @{$results{missing_params}}, 'user_name';
}

# Validate age (mandatory)
if (defined $age && $age ne '') {
    push @{$results{correct_params}}, 'age';
} else {
    push @{$results{missing_params}}, 'age';
}

# Validate favorite_color (optional but with mandatory value if provided)
if (defined $favorite_color) {
    if ($favorite_color eq '') {
        push @{$results{incorrect_params}}, 'favorite_color';
    } elsif (!grep { $_ eq $favorite_color } @valid_colors) {
        push @{$results{incorrect_params}}, 'favorite_color';
    } else {
        push @{$results{correct_params}}, 'favorite_color';
    }
}

# Output results
print $cgi->header('text/plain');
print "Correct Parameters: ", join(", ", @{$results{correct_params}}), "\n";
print "Incorrect Parameters: ", join(", ", @{$results{incorrect_params}}), "\n";
print "Missing Parameters: ", join(", ", @{$results{missing_params}}), "\n";

__END__
