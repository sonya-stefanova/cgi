#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

# Create a new CGI object
my $cgi = CGI->new();

# Send the HTTP header with status 200 OK and content type text/html
print $cgi->header(
    -type => 'text/html',
    -status => '200 OK'
);

# Retrieve the author parameter from the GET request
my $author = $cgi->param('author') || '';

# Hardcoded list of posts (In real-world applications, this data would come from a database)
my @posts = (
    { title => 'Post 1', author => 'John', content => 'This is the first post.' },
    { title => 'Post 2', author => 'Jane', content => 'This is the second post.' },
    { title => 'Post 3', author => 'John', content => 'This post is about Perl.' },
    { title => 'Post 4', author => 'Alice', content => 'Learn about CGI scripting.' },
);

# Filter posts based on the author using foreach
my @filtered_posts;
foreach my $post (@posts) {
    if ($author eq '' || $post->{author} =~ /\Q$author\E/i) {
        push @filtered_posts, $post;
    }
}

# Print the HTML content
print <<HTML;
<!doctype html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
HTML

if (@filtered_posts) {
    print "<ul>\n";
    foreach my $post (@filtered_posts) {
        print "<li><strong>Title:</strong> $post->{title}<br>\n";
        print "<strong>Author:</strong> $post->{author}<br>\n";
        print "<strong>Content:</strong> $post->{content}</li><br><br>\n";
    }
    print "</ul>\n";
} else {
    print "<p>No posts found matching your criteria.</p>\n";
}

print <<HTML;
</body>
</html>
HTML
