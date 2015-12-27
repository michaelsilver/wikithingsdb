from wikithingsdb import fetch
import time

"""
Fetch a bunch of types, classes, hypernyms, and redirects from
WikithingsDB for demoing, sanity checks, and testing.

By default prints to standard out, but the script is most useful when
piped into an output file like this:

   python sample.py > out.log

"""


def time_fetch(f, symbol):
    print "%s('%s')" % (f.__name__, symbol)  # prints out the function name
    start = time.time()
    print f(symbol)
    print " .. took: %s" % (time.time() - start)


def main():

    try:
        time_fetch(fetch.types_of_article, 'Brooklyn Bridge')
        time_fetch(fetch.classes_of_article, 'Brooklyn Bridge')
        time_fetch(fetch.hypernyms_of_article, 'Brooklyn Bridge')
        time_fetch(fetch.hypernyms_of_class, 'bridge')
        time_fetch(fetch.redirects_of_article, 'Brooklyn Bridge')
    except Exception, e:
        print e

    print "-----------------------"

    try:
        time_fetch(fetch.types_of_article, 'East River')
        time_fetch(fetch.classes_of_article, 'East River')
        time_fetch(fetch.hypernyms_of_article, 'East River')
        time_fetch(fetch.hypernyms_of_class, 'river')
        time_fetch(fetch.redirects_of_article, 'East River')
    except Exception, e:
        print e

    print "-----------------------"

    try:
        time_fetch(fetch.types_of_article, 'Bill Clinton')
        time_fetch(fetch.classes_of_article, 'Bill Clinton')
        time_fetch(fetch.hypernyms_of_article, 'Bill Clinton')
        time_fetch(fetch.hypernyms_of_class, 'president')
        time_fetch(fetch.redirects_of_article, 'Bill Clinton')
    except Exception, e:
        print e

    print "-----------------------"

    try:
        time_fetch(fetch.articles_of_type, 'officeholder')
        time_fetch(fetch.articles_of_class, 'officeholder')
        time_fetch(fetch.articles_of_hypernym, 'politician')
        time_fetch(fetch.classes_of_hypernym, 'place')
    except Exception, e:
        print e

    print "DONE"


if __name__ == '__main__':
    main()